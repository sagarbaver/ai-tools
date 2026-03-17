# GTD System Design

A sustainable Getting Things Done (GTD) system designed for AI-assisted weekly planning.

## Core Principles

1. **Separate execution from thinking** — Apple Notes for fast capture, Notion for planning and
   context
2. **Do not mix cognitive modes** — Tasks, decisions, research, and someday items each have their
   own space
3. **Calendar items should not live in task lists** — If it must happen on a specific date, schedule
   it
4. **Reviews and decisions are different** — Reviews understand state; decisions change state
5. **Keep the execution layer small** — The daily action list contains only real next actions
6. **Every project needs ONE next action** — No project without a defined next physical step

## System Architecture (4 Layers)

### Layer 1: Calendar = Time Boundaries

- Work calendar: meetings, auto-generated focus blocks (tied to employer)
- Personal calendar (iCloud): Ideal Week blocks — fitness, learning, chores, relationships, weekly
  planning
- Personal blocks are portable and survive job changes

### Layer 2: Notion Weekly Planner = Daily Execution Plan

- The primary "what am I doing today" view
- Created each week during the Sunday planning session
- Day-by-day layout with pomodoro time budgets
- Daily themes following the Trident system: Work, Personal, Relationships
- Max 3-5 items per category per day

### Layer 3: Apple Notes = Capture Only

- **Inbox** — Quick capture for voice memos, ideas, obligations
- Processed weekly during the Sunday planning session
- Should contain max 10-15 items at any time

### Layer 4: Notion GTD Pages = Reference & Thinking

- Domain checklists with cadence tracking ("Last Done On")
- Project plans with defined next actions
- Someday/Maybe for non-urgent ideas
- Reviewed during weekly planning to surface items for the week

## GTD Category Taxonomy

### Execution (Apple Notes + Notion Weekly Planner)

| Category       | Purpose                               | Review Cadence  |
|----------------|---------------------------------------|-----------------|
| Inbox          | Raw capture before processing         | Weekly (Sunday) |
| Next Actions   | Concrete, physically executable tasks | Daily           |
| Weekly Planner | Day-by-day assigned actions           | Daily           |

### Tracking (Notion)

| Category    | Purpose                                  | Review Cadence |
|-------------|------------------------------------------|----------------|
| Waiting For | Items dependent on others                | Weekly         |
| Projects    | Multi-step outcomes with ONE next action | Weekly         |

### Recurring Reference (Notion GTD Pages)

| Category                    | Purpose                            | Review Cadence |
|-----------------------------|------------------------------------|----------------|
| [Work] Operational Hygiene  | Recurring work maintenance tasks   | Weekly         |
| [Personal] Admin            | Life logistics, account management | Weekly         |
| [Personal] Home Maintenance | Physical upkeep of living space    | Weekly         |
| [Personal] Personal Care    | Grooming, health maintenance       | Weekly         |
| [Health] Fitness Routines   | Exercise plans and tracking        | Weekly         |

### Thinking & Incubation (Notion)

| Category            | Purpose                                                | Review Cadence    |
|---------------------|--------------------------------------------------------|-------------------|
| Someday/Maybe       | Ideas, curiosities, possibilities — not commitments    | Monthly           |
| Decisions Backlog   | Questions requiring deliberation, phrased as decisions | Monthly/Quarterly |
| Explorations        | Learning backlog, courses, tools to try                | Monthly           |
| Career Goals        | IDP goals with next actions + mentorship               | Monthly           |
| Career Evidence Log | Self-assessment data points and testimonials           | Monthly           |

### Context Lists (Notion)

| Category | Purpose                                 | Review Cadence   |
|----------|-----------------------------------------|------------------|
| India    | Location-specific tasks for India trips | Before each trip |

## David Allen's Five-Step Workflow Mapped to Tools

| GTD Step     | Tool                              | What Happens                                                   |
|--------------|-----------------------------------|----------------------------------------------------------------|
| **Capture**  | Apple Notes Inbox                 | Quick dump — voice memos, thoughts, obligations                |
| **Clarify**  | Weekly Planning Session           | Process each inbox item: actionable? <2 min? project? someday? |
| **Organize** | Notion GTD pages + Weekly Planner | Items land in the right place                                  |
| **Reflect**  | Weekly Review (AI-assisted)       | Review all lists, check cadence, surface what matters          |
| **Engage**   | Notion Weekly Planner + Calendar  | Look at today's plan, do the work                              |

## Energy-Based Context Tags

Following David Allen's evolved context-aware approach (energy/mindset over location):

| Context    | When to Use                       | Example Tasks                    |
|------------|-----------------------------------|----------------------------------|
| @DeepWork  | Morning focus blocks, high energy | Coding, design, writing          |
| @QuickHits | Between meetings, low energy      | Slack processing, email, admin   |
| @Calls     | Relationship blocks               | Family calls, social check-ins   |
| @Errands   | Out of the house                  | Groceries, pickups, appointments |
| @LowEnergy | Evening wind-down                 | YouTube playlist, light reading  |

## Weekly Planning Session (60 minutes)

| Time      | Step                         | What Happens                                                 |
|-----------|------------------------------|--------------------------------------------------------------|
| 0-15 min  | Process Inbox + Waiting For  | Classify items, route to GTD categories, check pending items |
| 15-30 min | Review Checklists + Projects | Surface overdue recurring items, check project next actions  |
| 30-40 min | Review Calendar              | Map availability, identify conflicts, plan around meetings   |
| 40-60 min | Build Weekly Planner         | Create Notion page, assign tasks to days, set themes         |

Monthly add-on (first Sunday): Review Someday/Maybe, Decisions Backlog, Career Evidence (+30 min)

## Trident Calendar System Integration

Based on Ali Abdaal's three-level time management:

| Level                        | Implementation                                                  |
|------------------------------|-----------------------------------------------------------------|
| **Macro** (Year at a Glance) | Annual calendar with holidays, trips, and major milestones      |
| **Meso** (Ideal Week)        | Recurring personal blocks on iCloud calendar                    |
| **Micro** (Daily Quests)     | 3 daily themes in weekly planner: Work, Personal, Relationships |