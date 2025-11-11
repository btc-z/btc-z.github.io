# CLAUDE.md

## Project Overview

This is a personal blog built with MkDocs Material, deployed to GitHub Pages at **zihan.us**. The repository serves two purposes:
1. The main blog content (root level)
2. A cookiecutter template for creating similar blogs (`mkdocs-blog-template/`)

## Development Commands

### Local Development
```bash
poetry install             # Install dependencies (first time setup)
poetry env activate        # Activate virtual environment
make serve                 # Start development server at http://127.0.0.1:8000/
```

### Deployment
Deployment is fully automated via GitHub Actions. Pushing to `main` branch triggers `.github/workflows/cicd.yml` which:
- Installs dependencies (mkdocs-material, mkdocs-git-revision-date-localized-plugin, mkdocs-redirects)
- Runs `mkdocs gh-deploy --force` to deploy to GitHub Pages

## Architecture

### Multilingual Blog Structure
The blog uses MkDocs Material with **dual blog plugin instances** for Chinese (default) and English versions. Chinese content is served at the root, with English content under `/en/`.

```
docs/
├── index.md              # Chinese homepage (default, 中文主页)
├── CNAME                 # Custom domain: zihan.us
├── assets/               # Shared images and media
│   └── vipassana/
├── javascripts/          # Custom JavaScript
│   └── mathjax.js       # Math rendering configuration
├── posts/                # Chinese blog posts (default)
│   ├── reflections/     # 生活感悟
│   └── books/           # 读书笔记
└── en/                   # English version
    ├── index.md         # English homepage
    └── posts/
        ├── reflections/ # Life reflections & meditation
        └── books/       # Book reviews and reading notes
```

### Post Workflow

**For new Chinese posts (default):**
1. **Create post**: Add markdown file to `docs/posts/reflections/` or `docs/posts/books/`
2. **Frontmatter**: Include YAML frontmatter with `draft`, `date`, and `categories`
3. **Update homepage**: Manually add entry to `docs/index.md` with emoji, date, and link
4. **Optional translation**: Create corresponding English version in `docs/en/posts/`
5. **Preview**: Run `make serve` to test locally
6. **Deploy**: Commit and push to `main` - GitHub Actions handles deployment

**For new English posts:**
- Same workflow, but use `docs/en/posts/` and update `docs/en/index.md`

### Language Switcher
- Homepage defaults to Chinese (`/`)
- Language switcher in header allows toggling between 中文 and English
- Configured via `extra.alternate` in mkdocs.yml:
  - Chinese: `/` (default)
  - English: `/en/`

### Post File Structure vs URL Format
- **File structure**: Posts stored in language-specific category folders:
  - Chinese (default): `docs/posts/reflections/post-name.md`
  - English: `docs/en/posts/reflections/post-name.md`
- **Generated URLs**: Blog plugin generates date-based URLs:
  - Chinese: `/posts/2024/11/01/post-title`
  - English: `/en/posts/2024/11/01/post-title`
  - Based on the `date` field in frontmatter (configured via `post_url_date_format: yyyy/MM/dd` in mkdocs.yml)

**Blog plugin documentation**: https://squidfunk.github.io/mkdocs-material/plugins/blog/

### Blog Index Redirects
- `docs/posts/index.md`: Auto-redirects to `index.md` (Chinese homepage)
- `docs/en/posts/index.md`: Auto-redirects to `en/index.md` (English homepage)

## Key Configuration

### mkdocs.yml
- **Blog plugin (dual instances)**:
  - Chinese blog (default): `blog_dir: posts`, date-based URLs, archive disabled
  - English blog: `blog_dir: en/posts`, date-based URLs, archive disabled
- **Language switcher**: `extra.alternate` configures language switcher in header
  - Chinese: `/` (default)
  - English: `/en/`
- **Redirects plugin**: Routes blog index pages to language homepages
  - `posts/index.md` → `index.md` (Chinese homepage)
  - `en/posts/index.md` → `en/index.md` (English homepage)
- **Git revision date plugin**: Shows "timeago" format timestamps (e.g., "2 days ago")
- **Theme**: Material with Roboto Mono font, lime primary color, light/dark mode toggle
- **Analytics**: Google Analytics enabled (G-X956BD08NG)
- **Markdown extensions**: emoji, math (MathJax), mermaid diagrams, admonitions, footnotes

### pyproject.toml
- Python version: `^3.13.1`
- Package manager: Poetry
- Dependencies: mkdocs-material, mkdocs-git-revision-date-localized-plugin, mkdocs-redirects, cookiecutter

### MathJax Configuration
Math rendering is configured via `docs/javascripts/mathjax.js` (referenced in `mkdocs.yml` but file may not exist - MathJax is loaded from CDN)

## Cookiecutter Template

The `mkdocs-blog-template/` directory contains a cookiecutter template for generating new blogs with similar structure. Key files:
- `cookiecutter.json`: Template variables
- `{{cookiecutter.project_slug}}/`: Template directory structure
- Multiple documentation files (QUICKSTART.md, USAGE_GUIDE.md, etc.) explaining template usage

## Multilingual Support

The blog has full multilingual support with Chinese as the default language and English as an alternative:
- **Default language**: Chinese content at root (`/`)
- **Alternative language**: English content at `/en/`
- **Architecture**: Uses dual blog plugin instances for independent language sections
- **Language switcher**: Header switcher allows toggling between 中文 and English
- **Translations**: All posts are translated between languages:
  - Chinese posts (default) in `docs/posts/`
  - English posts in `docs/en/posts/`
- **Navigation**: Each language has its own homepage, blog structure, and post organization

## Custom Domain

The `docs/CNAME` file contains `zihan.us` for GitHub Pages custom domain routing.

## Commit Convention

Based on git history, commits follow pattern: `type: description`
- Examples: `post: 理想的生活`, `chore: update note to readers`, `cookiecutter`
