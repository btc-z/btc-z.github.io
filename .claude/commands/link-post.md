---
description: Add a post link to its category index
---

Add a link to a post in its category index file.

## Instructions

1. **Auto-detect new posts**: Run `git status` to find new/untracked posts in `docs/posts/*/`
2. **Interactive prompt**: If multiple new posts found, use `AskUserQuestion` tool to let user select which post to link
   - If only one new post, ask for confirmation before proceeding
   - If no new posts, ask user to provide the post name/path
3. **Extract category**: Get category from post path `docs/posts/{category}/{post-name}.md`
4. **Add link**: Update `docs/{category}.md` after the header with:
   ```markdown
   - [{post-name}](posts/{category}/{post-name}.md)
   ```
5. **Verify**: Confirm link was added successfully

## Example

Post: `docs/posts/想法/居住地.md`
→ Add to `docs/想法.md`: `- [居住地](posts/想法/居住地.md)`

**Note**: Link text is ONLY the post name (without .md), no descriptions.
