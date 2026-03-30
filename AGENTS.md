# ai-tools

Personal AI tools, skills, and productivity automation.

## Weekly Planner Skill

Located at `.claude/skills/weekly-planner/SKILL.md`. Invoke with `/weekly-planner` for a 60-minute AI-assisted GTD weekly planning session.

### How It Works
This skill implements David Allen's Getting Things Done (GTD) five-step workflow — Capture, Clarify, Organize, Reflect, Engage — as a guided weekly planning session. It reads your Notion GTD pages, processes your inbox, reviews recurring checklists for overdue items, and builds a filled-out weekly planner in Notion.

### Required Integrations
- **Notion** — for reading/writing GTD pages and weekly planner pages

### Private Configuration
- `gtd/.local-config.md` — Local configuration: calendar ICS path, Notion page IDs (gitignored). Copy `gtd/.local-config.example.md` and populate with your own values.

### Public Reference
- `gtd/gtd-system-design.md` — System architecture and GTD methodology