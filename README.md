# ZLAB Personal Blog

Personal blog built with MkDocs Material, hosted on GitHub Pages at **zihan.us**.

## Local Development

1. Run `poetry install` to install necessary dependencies
2. Run `poetry shell` to start python virtual environment
3. Run `make serve` to start local server: `http://127.0.0.1:8000/`

## Post Organization

Posts are organized in a **category-based directory structure** under `docs/posts/`:

```
docs/posts/
├── reflections/      # Life reflections & meditation
└── books/            # Book reviews and reading notes
```

## Post Structure

Posts support **two formats**:

### Format 1: With YAML Frontmatter (Recommended)
```yaml
---
draft: false                    # Set to true to hide
date: 2024-11-01                # Publication date (YYYY-MM-DD)
categories:
    - meditation                # meditation, books, philosophy, etc.
---

# Post Title

Your content here...
```

### Format 2: Simple Markdown
```markdown
# Post Title

Content here...
```

## How to Add a New Post

**Step 1: Create the markdown file**
```bash
# Choose appropriate category folder:
docs/posts/reflections/   # For life reflections & meditation
docs/posts/books/         # For book reviews
```

**Step 2: Write your post** with frontmatter (recommended):
```yaml
---
draft: false
date: 2025-11-09
categories:
    - your-category
---

# Your Post Title

Your content here...
```

**Step 3: Update homepage** (`docs/index.md`):
```markdown
- **2025-11-09 :emoji: [Post Title](posts/category/filename.md)**
```

**Step 4: Preview locally**
```bash
make serve
# Visit http://127.0.0.1:8000/
```

**Step 5: Commit and push**
```bash
git add .
git commit -m "post: your post title"
git push
```

GitHub Actions will automatically build and deploy to GitHub Pages.

## Available Features in Posts

- **Emojis**: `:coffee:` → ☕ (Material emoji extension)
- **Math**: `$E=mc^2$` → Math notation via MathJax
- **Mermaid diagrams**: Code blocks with ` ```mermaid ` syntax
- **Admonitions**: Callout boxes with `!!! note`
- **Images**: Reference assets via `/assets/folder/image.png`
- **Bilingual**: Chinese and English posts work seamlessly
- **Auto timestamps**: Git creation/modification dates added automatically

## Important Configuration Files

### `mkdocs.yml` - Main site configuration
- Blog plugin settings (URL format: `yyyy/MM/dd`)
- Theme configuration (Material with light/dark mode)
- Markdown extensions (emoji, math, diagrams, etc.)
- Analytics (Google Analytics)
- Git revision date plugin (timeago format)

### `pyproject.toml` - Python dependencies
- MkDocs Material version
- Plugin dependencies
- Python version requirement

### `.github/workflows/cicd.yml` - Deployment
- Auto-deploys to GitHub Pages on push to `main`

### `docs/CNAME` - Custom domain
- Contains: `zihan.us`

### `docs/index.md` - Homepage
- Manual index of featured posts with emojis and dates

## Technology Stack

- **Framework**: MkDocs with Material theme
- **Language**: Python 3.13.1
- **Package Manager**: Poetry
- **Deployment**: GitHub Actions → GitHub Pages
- **Analytics**: Google Analytics

