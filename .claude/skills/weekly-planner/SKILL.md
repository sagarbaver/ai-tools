---
name: weekly-planner
description: Use when the user says "weekly plan", "plan my week", "Sunday review", "GTD review", "weekly planning session", or wants to process their inbox into next actions. Guides a 60-minute AI-assisted weekly planning session following the GTD methodology. Creates a Notion weekly planner page with assigned next actions, reviews recurring checklists, and processes the Apple Notes inbox.
allowed-tools: mcp__notion__notion-fetch, mcp__notion__notion-search, mcp__notion__notion-create-pages, mcp__notion__notion-update-page, AskUserQuestion, Read, Bash(date:*), Bash(grep:*), Bash(wc:*)
---

# Weekly Planning Session (60 minutes)

## Overview

This skill guides a structured weekly planning session based on David Allen's GTD methodology:
**Capture → Clarify → Organize → Reflect → Engage**

The session produces a filled-out Notion weekly planner page with concrete next actions assigned to
specific days, matched to calendar availability and energy levels.

## Before Starting

1. Read the local configuration from `gtd/.local-config.md` in this repository (calendar path, Notion page IDs)
2. Greet the user and confirm which week we're planning (default: the upcoming week)
3. **Present the prerequisite checklist below** and ask the user to prepare everything before
   proceeding. Do NOT start Step 1 until the user confirms they have all items ready.

### Prerequisite Checklist

> Before we begin, please have the following ready:
>
> 1. **Apple Notes Inbox** — Open your "Getting Things Done - Inbox" note, ready to paste
> 2. **Calendar export** — Export your Apple Calendar as an ICS file to the path configured in
>    `gtd/.local-config.md` (replace the existing file with a fresh export covering the planning week)
> 3. **Reminders** — Ask Siri / Apple Intelligence to summarize your reminders for the week and
>    paste the summary (Apple Reminders are not included in ICS exports)
>
> These three inputs feed the entire session. Having them ready upfront keeps the conversation
> cohesive.

---

## Step 1: Process Inbox + Waiting For (15 min)

### 1a. Process the Inbox

Ask the user to paste their Apple Notes Inbox (the GTD Personal capture note).

For each item, classify using David Allen's Clarify workflow:

- **Is it actionable?**
    - YES → What's the next physical action?
        - Takes <2 min? → Tell user to do it now
        - Is it a multi-step project? → Create in Notion [3] Projects with ONE next action
        - Single action → Add to this week's Next Actions
    - NO → Is it reference, someday/maybe, or trash?
        - Reference → Route to appropriate Notion GTD page
        - Someday/Maybe → Add to Notion [GTD] Someday/Maybe
        - Decision question → Add to Notion [GTD] Decisions Backlog
        - Trash → Tell user to delete it

Present the classification as a table for user approval before making any Notion changes.

### 1b. Review Waiting For

Fetch the Notion `[GTD] Waiting For` page.
For each item ask the user:

- Has this resolved? → Remove it
- Need to follow up? → Convert to a Next Action for this week
- Still waiting? → Leave it, update the follow-up date if needed

---

## Step 2: Review GTD Checklists + Projects (15 min)

### 2a. Review Recurring Checklists

Fetch each Notion [GTD] page and check "Last Done On" dates against cadence:

| Cadence   | Overdue if "Last Done On" is older than |
|-----------|-----------------------------------------|
| Daily     | Yesterday                               |
| Weekly    | 7 days ago                              |
| Biweekly  | 14 days ago                             |
| Monthly   | 30 days ago                             |
| Quarterly | 90 days ago                             |

Surface overdue items to the user: *"[Item] was last done on [date] and is on a [cadence] schedule —
add to this week?"*

Let the user choose which overdue items to include this week. Not everything overdue needs to be
done immediately.

### 2b. Review Projects

Fetch the Notion `[3] Projects` page and the All Projects database.
For each active project:

- What's the ONE next action? (David Allen's rule)
- Is it stalled? (No activity in 2+ weeks)
- Should a next action surface this week?

---

## Step 3: Review Calendar (10 min)

Read the calendar ICS path from `gtd/.local-config.md` (the user should have exported a fresh copy as
part of the prerequisite checklist).

Run the calendar parser script to generate the day-by-day summary:

```bash
python3 .claude/skills/weekly-planner/parse_calendar.py <ics_path> <week_start_YYYYMMDD> <week_end_YYYYMMDD>
```

Review the output and identify:

- **Meeting-heavy days** (>4 hours of meetings) — plan lighter personal tasks
- **Free focus blocks** — assign deep work here
- **Personal time blocks** (from iCloud Home calendar) — respect these as defended time
- **Conflicts** — where work overflows into personal blocks

Present a day-by-day availability summary.

---

## Step 4: Build the Weekly Planner (20 min)

### 4a. Create the Notion Page

Create a new page under `[1] Weekly Plans` using the template structure:

- Title: `Mon DD - Mon DD Week Planner` (matching the existing naming convention)
- Icon: 🗓️
- Use the exact Notion markdown structure from the Week Planner Template (fetch it for reference)

### 4b. Assign Items to Days

For each day, assign tasks following these principles:

**Energy matching (David Allen's context-aware approach):**

- @DeepWork (morning focus blocks) → Jira tickets, coding, design work
- @QuickHits (between meetings, low energy) → Slack processing, email, admin tasks
- @Calls (relationship blocks) → Family calls, social check-ins

**Trident daily quests (Ali Abdaal):**
Each day gets 3 themes:

- **Work:** The main work focus for the day
- **Personal:** The personal task or chore focus
- **Relationships:** An intentional social touchpoint

**Capacity rules:**

- Max 3-5 items per category per day
- Weekdays: prioritize work + one personal maintenance task
- Weekends: prioritize chores, projects, relationships
- Friday: lighter load, learning-focused (Focus Friday)
- Include pomodoro estimates (🍅 = 30 min)

### 4c. Present for Review

Show the user the draft planner day-by-day. Ask for adjustments before committing to Notion.

---

## Monthly Add-On (First Sunday of the Month)

If it's the first Sunday of the month, add 30 extra minutes:

1. **Review Someday/Maybe** — Fetch the page. Ask: *"Anything here you want to activate as a
   project?"*
2. **Review Decisions Backlog** — Fetch the page. Ask: *"Any decisions you're ready to make?"*
3. **Review Career Evidence Log** — Ask: *"Any recent wins or testimonials to log?"*
4. **Audit "Last Done On" dates** — Scan all GTD pages for stale dates and update them

---

## After the Session

Summarize what was accomplished:

- Items processed from inbox: X
- Items added to this week's planner: X
- Overdue recurring items surfaced: X
- Waiting For items resolved/followed up: X
- Next week's planner page: [link]

Remind the user:

- Their Apple Notes Inbox should now be empty (everything processed)
- Their Notion weekly planner is their daily command center for the week
- Capture new items in Apple Notes Inbox throughout the week — they'll be processed next Sunday
