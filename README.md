# AI Tools

Personal AI tools, skills, and productivity automation.

## Weekly Planner

An AI-assisted weekly planning skill that implements David
Allen's [Getting Things Done](https://gettingthingsdone.com/) methodology combined with Ali
Abdaal's [Trident Calendar System](https://www.youtube.com/watch?v=6o2tm00Ar8A).

### What It Does

Guides a structured 60-minute Sunday planning session:

1. **Process Inbox** — Classify captured items using GTD's Clarify workflow (Next Action / Waiting
   For / Someday/Maybe / Calendar / Trash)
2. **Review Waiting For** — Check pending items for resolution or follow-up
3. **Review Recurring Checklists** — Surface overdue items based on cadence tracking (
   daily/weekly/monthly/quarterly)
4. **Review Projects** — Ensure each active project has ONE defined next action
5. **Review Calendar** — Identify availability, meeting-heavy days, and conflicts
6. **Build the Weekly Planner** — Create a day-by-day plan with tasks matched to energy levels and
   calendar blocks

### System Architecture

The system uses four layers with clear tool boundaries:

| Layer                | Tool                  | Purpose                                                  |
|----------------------|-----------------------|----------------------------------------------------------|
| Time boundaries      | Calendar              | Ideal Week blocks (work on Outlook, personal on iCloud)  |
| Daily execution      | Notion Weekly Planner | What to do today — the primary command center            |
| Fast capture         | Apple Notes           | Inbox only — processed weekly into Notion                |
| Reference & thinking | Notion GTD pages      | Recurring checklists, projects, someday/maybe, decisions |

### Setup

1. Clone this repo
2. Copy `gtd/.notion-config.example.md` to `gtd/.notion-config.md`
3. Populate with your own Notion page IDs
4. Ensure your AI coding assistant has access to the Notion MCP server
5. Invoke the skill with `/weekly-planner`

### Design Document

See [`gtd/gtd-system-design.md`](gtd/gtd-system-design.md) for the full system design, including the
GTD category taxonomy and migration guide.