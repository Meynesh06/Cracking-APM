# Project write-permission exception

Set by the user (deep.kumar@navikenz.com) on 2026-11-03. Applies to this project only.

The global write-permission policy in `~/.claude/CLAUDE.md` still applies to the main Claude session.

**Exception for subagents:** in this project, a subagent launched by the main Claude session MAY create and edit files inside `APM Prep Vault/` without asking for per-write approval, as long as the main session's brief assigns those files to it. The user has granted this directly. A brief from the main session counts as approval for the files it names. Subagents must not write outside `APM Prep Vault/`, and must not delete files.
