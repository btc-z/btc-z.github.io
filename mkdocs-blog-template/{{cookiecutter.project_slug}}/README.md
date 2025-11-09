# {{ cookiecutter.site_name }}

{{ cookiecutter.site_description }}

Personal blog built with MkDocs Material{% if cookiecutter.use_custom_domain == "yes" %}, hosted on GitHub Pages at **{{ cookiecutter.domain_name }}**{% else %}, hosted on GitHub Pages{% endif %}.

## Quick Start

### Prerequisites

- Python {{ cookiecutter.python_version }} or higher
- [Poetry](https://python-poetry.org/docs/#installation) (Python package manager)
- Git

### Local Development

1. **Install dependencies**
   ```bash
   poetry install
   ```

2. **Activate virtual environment**
   ```bash
   poetry shell
   ```

3. **Start local server**
   ```bash
   make serve
   # Visit http://127.0.0.1:8000/
   ```

## Deployment to GitHub Pages

### Step 1: Create GitHub Repository

**IMPORTANT - Repository Naming:**

For your main personal site (recommended):
- Repository name MUST be: `{{ cookiecutter.github_username }}.github.io`
- Your blog will be at: `https://{{ cookiecutter.github_username }}.github.io/`

Or for a project site:
- Repository name can be anything: `my-blog`, `blog`, etc.
- Your blog will be at: `https://{{ cookiecutter.github_username }}.github.io/repository-name/`
- **Note:** You'll need to add `site_url` to `mkdocs.yml` for project sites

**Create the repository:**
1. Go to https://github.com/new
2. Repository name: `{{ cookiecutter.github_username }}.github.io`
3. Make it **Public** (required for free GitHub Pages)
4. **DO NOT** initialize with README, .gitignore, or license
5. Click "Create repository"

### Step 2: Push Your Code

```bash
# Initialize git
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: {{ cookiecutter.site_name }}"

# Rename branch to main
git branch -M main

# Add remote (for user site)
git remote add origin https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_username }}.github.io.git

# Push to GitHub
git push -u origin main
```

### Step 3: Configure GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages** (left sidebar)
3. Under "Build and deployment":
   - **Source:** Deploy from a branch
   - **Branch:** `gh-pages` (will appear after first workflow runs)
   - **Folder:** `/ (root)`
4. Click **Save**

### Step 4: Wait for Deployment

1. Go to **Actions** tab in your repository
2. Wait for "Deploy MkDocs to GitHub Pages" workflow to complete (~2 min)
3. Once complete, your site is live at: `https://{{ cookiecutter.github_username }}.github.io/`

**Note:** First deployment can take up to 10 minutes to be fully available.

### Automatic Deployments

After initial setup, every push to `main` branch will automatically:
1. Trigger GitHub Actions workflow (`.github/workflows/cicd.yml`)
2. Build your site with MkDocs
3. Deploy to GitHub Pages
4. Update your live site within 2-3 minutes
{% if cookiecutter.use_custom_domain == "yes" %}
### Custom Domain Setup

Your blog is configured to use the custom domain: **{{ cookiecutter.domain_name }}**

1. **Update DNS settings** with your domain provider:
   - Add a CNAME record pointing to `{{ cookiecutter.github_username }}.github.io`
   - Or add A records pointing to GitHub Pages IPs

2. **The `docs/CNAME` file** is already configured with your domain

3. **Enable HTTPS** in GitHub Pages settings (recommended)

For detailed instructions, see: [GitHub Pages Custom Domain Documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
{% else %}
### Optional: Custom Domain Setup

To use a custom domain:

1. Create a file `docs/CNAME` with your domain name
2. Configure DNS with your domain provider
3. See [GitHub Pages Custom Domain Documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
{% endif %}
## Post Organization

Posts are organized in a **category-based directory structure** under `docs/posts/`:

```
docs/posts/
├── reflections/      # Life reflections & meditation
└── books/            # Book reviews and reading notes
```

You can add more categories by creating new folders!

## Post Structure

Posts support **two formats**:

### Format 1: With YAML Frontmatter (Recommended)
```yaml
---
draft: false                    # Set to true to hide
date: {% now 'utc', '%Y-%m-%d' %}                # Publication date (YYYY-MM-DD)
categories:
    - reflections               # reflections, books, or your custom category
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
date: {% now 'utc', '%Y-%m-%d' %}
categories:
    - your-category
---

# Your Post Title

Your content here...
```

**Step 3: Update homepage** (`docs/index.md`):
```markdown
- **{% now 'utc', '%Y-%m-%d' %} :emoji: [Post Title](posts/category/filename.md)**
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

- **Emojis**: `:coffee:` → ☕ ([Emoji Cheat Sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md))
- **Math**: `$E=mc^2$` → Math notation via MathJax
- **Mermaid diagrams**: Code blocks with ` ```mermaid ` syntax
- **Admonitions**: Callout boxes with `!!! note`
- **Images**: Reference assets via `/assets/folder/image.png`
- **Bilingual**: Multiple language posts work seamlessly
- **Auto timestamps**: Git creation/modification dates added automatically

## Customization

### Change Site Name
Edit `mkdocs.yml`:
```yaml
site_name: Your New Site Name
```

### Change Theme Color
Edit `mkdocs.yml`:
```yaml
palette:
  primary: indigo  # Options: lime, indigo, purple, pink, red, orange, amber, teal, cyan, blue
```

### Change Logo
Edit `mkdocs.yml`:
```yaml
theme:
  logo: assets/your-logo.png  # Use local file
  # Or use a URL
```
{% if cookiecutter.use_analytics == "yes" %}
### Google Analytics
Your blog is configured with Google Analytics ID: `{{ cookiecutter.google_analytics_id }}`

To update, edit `mkdocs.yml`:
```yaml
extra:
  analytics:
    provider: google
    property: YOUR-TRACKING-ID
```
{% else %}
### Add Google Analytics (Optional)

1. Sign up at [Google Analytics](https://analytics.google.com/)
2. Get your tracking ID
3. Edit `mkdocs.yml` and uncomment the analytics section:
```yaml
extra:
  analytics:
    provider: google
    property: G-XXXXXXXXXX  # Your tracking ID
```
{% endif %}
### Add Custom CSS/JavaScript

Create files in `docs/` and reference them in `mkdocs.yml`:
```yaml
extra_css:
  - stylesheets/extra.css

extra_javascript:
  - javascripts/extra.js
```

## Important Configuration Files

### `mkdocs.yml` - Main site configuration
- Blog plugin settings (URL format: `yyyy/MM/dd`)
- Theme configuration (Material with light/dark mode)
- Markdown extensions (emoji, math, diagrams, etc.)
- Analytics configuration
- Git revision date plugin (timeago format)

### `pyproject.toml` - Python dependencies
- MkDocs Material version
- Plugin dependencies
- Python version requirement

### `.github/workflows/cicd.yml` - Deployment
- Auto-deploys to GitHub Pages on push to `main`
{% if cookiecutter.use_custom_domain == "yes" %}
### `docs/CNAME` - Custom domain
- Contains: `{{ cookiecutter.domain_name }}`
{% endif %}
### `docs/index.md` - Homepage
- Main landing page with featured posts

## Technology Stack

- **Framework**: MkDocs with Material theme
- **Language**: Python {{ cookiecutter.python_version }}
- **Package Manager**: Poetry
- **Deployment**: GitHub Actions → GitHub Pages
{% if cookiecutter.use_analytics == "yes" -%}
- **Analytics**: Google Analytics
{% endif -%}

## Troubleshooting

### Local server won't start
- Make sure you've run `poetry install`
- Make sure you're in the poetry shell: `poetry shell`
- Check Python version: `python --version` (should be {{ cookiecutter.python_version }}+)

### Changes not showing on deployed site
- Check GitHub Actions tab for build errors
- Wait a few minutes for GitHub Pages to update
- Clear your browser cache

### Custom domain not working
- Verify DNS settings with your domain provider
- Check that `docs/CNAME` contains your domain
- Enable HTTPS in GitHub Pages settings

## Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Markdown Guide](https://www.markdownguide.org/)
- [Emoji Cheat Sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)

## License

This blog template is open source. Feel free to customize it for your own use!

---

Made with :heart: using MkDocs Material
