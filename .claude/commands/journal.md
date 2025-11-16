---
description: Create a new daily journal entry
---

Creates a new daily journal entry with proper structure and updates the journal index.

## Steps

1. **Determine date**: Use today's date or ask user for specific date
2. **Check if exists**: See if journal post already exists
3. **Create post file**: Generate `docs/posts/journal/YYYY-MM-DD.md` with template
4. **Update index**: Add entry to `docs/journal.md` at the top of the month section
5. **Verify**: Confirm file created and index updated

## Post Template

```markdown
---
draft: false
date: YYYY-MM-DD
categories:
  - journal
---

# YYYY/MM/DD

## ✅ Today's Tasks

- [ ] Task 1
- [ ] Task 2
- [ ] Task 3

<!-- more -->

## 💭 Reflections

What went well, what to improve...

## 📝 Notes

Random thoughts and observations.
```

## Index Entry Format

Add to `docs/journal.md` under the appropriate month heading:

```markdown
- **YYYY-MM-DD [Daily Journal - YYYY-MM-DD](posts/journal/YYYY-MM-DD.md)**
```

## Instructions

1. Ask user if they want to create journal for today or specify a date
2. Extract date in YYYY-MM-DD format
3. Check if `docs/posts/journal/YYYY-MM-DD.md` exists
   - If exists, ask if they want to open it or overwrite
   - If not, proceed to create
4. Create the journal post file with proper frontmatter and template
5. Read `docs/journal.md` to understand current structure
6. Determine the month section (e.g., "### January 2025")
   - If month section doesn't exist, create it
7. Add the new entry as the FIRST item under that month section
8. Report success and provide link to the created file

## Important Notes

- Always use today's date by default for convenience
- Keep month sections in reverse chronological order (newest first)
- Entries within each month should also be newest first
- Use interactive prompts to confirm actions
- The title in the markdown file should use forward slashes (YYYY/MM/DD)
- The frontmatter date should use hyphens (YYYY-MM-DD)
