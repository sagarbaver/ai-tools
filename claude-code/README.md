# Claude Code Settings

Symlink `settings.json` to `~/.claude/settings.json`:

```bash
ln -sf "$(pwd)/settings.json" ~/.claude/settings.json
```

## Hooks

### SessionStart

Automatically loads project context files (`AGENTS.md` and `CLAUDE.md`) from the current project
directory at the start of each session.

## Status Line

A custom status line that displays real-time session info. Example output:

```
my-project (main) [planning] claude-opus-4-6 high 142K tokens 87% ctx $0.52
```

### Segments (left to right)

| Segment      | Color      | Source                                                                       | Description                                                |
|--------------|------------|------------------------------------------------------------------------------|------------------------------------------------------------|
| Directory    | Cyan       | `workspace.current_dir`                                                      | Basename of the working directory                          |
| Git branch   | Green      | `git branch --show-current`                                                  | Current branch, or `(detached)`                            |
| Session name | Magenta    | `CLAUDE_SESSION_NAME` env var > `/rename` name > first 8 chars of session ID | Identifies the session in brackets                         |
| Model        | Light cyan | `model.id`                                                                   | Active model ID                                            |
| Effort       | Yellow     | `thinking_effort`                                                            | Current thinking effort level                              |
| Tokens       | Yellow     | `total_input_tokens + total_output_tokens`                                   | Total token usage in thousands                             |
| Context      | Blue       | `remaining_percentage`                                                       | Remaining context window percentage                        |
| Cost         | Purple     | Computed                                                                     | Estimated cost (`$input * 3 + $output * 15` per 1M tokens) |

### Session Naming with `@name`

Add this wrapper function to `~/.zshrc` to name sessions from the command line:

```zsh
claude() {
  local session_name=""
  local args=()
  for arg in "$@"; do
    if [[ "$arg" == @* ]]; then
      session_name="${arg#@}"
    else
      args+=("$arg")
    fi
  done
  if [[ -n "$session_name" ]]; then
    CLAUDE_SESSION_NAME="$session_name" command claude "${args[@]}"
  else
    command claude "$@"
  fi
}
```

Usage:

```bash
claude @planning          # status line shows [planning]
claude @debug --verbose   # named session with flags passed through
claude                    # no name, falls back to /rename name or session ID
```

This is useful when running multiple parallel sessions (planning, execution, debugging) to tell them
apart at a glance.

## Other Settings

| Setting          | Description                                     |
|------------------|-------------------------------------------------|
| `effortLevel`    | Sets the default thinking effort level (`high`) |
| `enabledPlugins` | Marketplace plugins to enable                   |