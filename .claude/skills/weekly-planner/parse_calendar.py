#!/usr/bin/env python3
"""Parse an ICS calendar file and summarize events for a given week.

Usage:
    python3 parse_calendar.py <ics_path> <week_start_YYYYMMDD> <week_end_YYYYMMDD>

Example:
    python3 parse_calendar.py /path/to/calendar.ics 20260323 20260329

Outputs:
    - Day-by-day event listing with times and durations
    - Recurring weekly events that land in the target week
    - Meeting load summary per day (LIGHT / MODERATE / HEAVY)
"""

import re
import sys
from datetime import datetime, timedelta


def parse_events(content, week_start, week_end):
    """Parse VEVENT blocks and return events within the target week."""
    events = content.split("BEGIN:VEVENT")
    results = []

    for event in events[1:]:
        summary_match = re.search(r"SUMMARY:(.*?)(?:\r?\n)", event)
        dtstart_match = re.search(r"DTSTART(?:;[^:]*)?:(.*?)(?:\r?\n)", event)
        dtend_match = re.search(r"DTEND(?:;[^:]*)?:(.*?)(?:\r?\n)", event)

        if not summary_match or not dtstart_match:
            continue

        summary = summary_match.group(1).strip()
        dtstart_str = dtstart_match.group(1).strip()
        dtend_str = dtend_match.group(1).strip() if dtend_match else None

        try:
            if "T" in dtstart_str:
                if dtstart_str.endswith("Z"):
                    dt = datetime.strptime(dtstart_str, "%Y%m%dT%H%M%SZ")
                    dt = dt - timedelta(hours=7)  # UTC to PDT — adjust for your timezone
                else:
                    dt = datetime.strptime(dtstart_str[:15], "%Y%m%dT%H%M%S")

                if dtend_str:
                    if dtend_str.endswith("Z"):
                        dt_end = datetime.strptime(dtend_str, "%Y%m%dT%H%M%SZ")
                        dt_end = dt_end - timedelta(hours=7)
                    else:
                        dt_end = datetime.strptime(dtend_str[:15], "%Y%m%dT%H%M%S")
                else:
                    dt_end = dt + timedelta(hours=1)

                # Cap single-event duration at 12 hours to handle multi-day or malformed events
                duration_min = min((dt_end - dt).total_seconds() / 60, 720)
                is_allday = False
            else:
                dt = datetime.strptime(dtstart_str[:8], "%Y%m%d")
                duration_min = 0
                is_allday = True
        except (ValueError, IndexError):
            continue

        if week_start <= dt < week_end:
            day_name = dt.strftime("%A %b %d")
            if is_allday:
                time_str = "All day"
                dur_str = ""
            else:
                time_str = f"{dt.strftime('%I:%M %p')}-{dt_end.strftime('%I:%M %p')}"
                dur_str = f" ({int(duration_min)} min)"

            results.append({
                "dt": dt,
                "day": day_name,
                "time": time_str,
                "duration_str": dur_str,
                "summary": summary,
                "duration_min": duration_min,
                "is_allday": is_allday,
            })

    results.sort(key=lambda x: x["dt"])
    return results


def parse_recurring(content, week_start, week_end):
    """Extract weekly recurring events that may land in the target week."""
    events = content.split("BEGIN:VEVENT")
    results = []

    for event in events[1:]:
        rrule_match = re.search(r"RRULE:(.*?)(?:\r?\n)", event)
        if not rrule_match:
            continue

        summary_match = re.search(r"SUMMARY:(.*?)(?:\r?\n)", event)
        dtstart_match = re.search(r"DTSTART(?:;[^:]*)?:(.*?)(?:\r?\n)", event)
        if not summary_match:
            continue

        summary = summary_match.group(1).strip()
        rrule = rrule_match.group(1).strip()
        dtstart_str = dtstart_match.group(1).strip() if dtstart_match else "N/A"

        if "FREQ=WEEKLY" not in rrule:
            continue

        # Check if the recurrence has expired
        until_match = re.search(r"UNTIL=(\d{8})", rrule)
        if until_match:
            until = datetime.strptime(until_match.group(1), "%Y%m%d")
            if until < week_start:
                continue

        byday_match = re.search(r"BYDAY=([A-Z,]+)", rrule)
        if byday_match:
            days = byday_match.group(1)
            interval_match = re.search(r"INTERVAL=(\d+)", rrule)
            interval = int(interval_match.group(1)) if interval_match else 1
            freq_label = f"every {interval} weeks" if interval > 1 else "weekly"
            results.append(f"{summary} — {days} ({freq_label}, from {dtstart_str[:8]})")

    return results


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)

    ics_path = sys.argv[1]
    week_start = datetime.strptime(sys.argv[2], "%Y%m%d")
    week_end = datetime.strptime(sys.argv[3], "%Y%m%d")

    with open(ics_path, "r") as f:
        content = f.read()

    # One-off events
    events = parse_events(content, week_start, week_end)
    day_meeting_hours = {}
    current_day = ""

    for e in events:
        if e["day"] != current_day:
            if current_day:
                print()
            current_day = e["day"]
            print(f"=== {e['day']} ===")
        print(f"  {e['time']}{e['duration_str']} — {e['summary']}")

        if not e["is_allday"]:
            day_meeting_hours.setdefault(e["day"], 0)
            day_meeting_hours[e["day"]] += e["duration_min"]

    # Recurring events
    recurring = parse_recurring(content, week_start, week_end)
    if recurring:
        print("\n=== RECURRING EVENTS (may land this week) ===")
        for r in recurring:
            print(f"  {r}")

    # Summary
    print("\n=== MEETING LOAD SUMMARY ===")
    for day in sorted(day_meeting_hours.keys()):
        mins = day_meeting_hours[day]
        hours = mins / 60
        label = "HEAVY" if hours > 4 else "MODERATE" if hours > 2 else "LIGHT"
        print(f"  {day}: {hours:.1f}h [{label}]")


if __name__ == "__main__":
    main()
