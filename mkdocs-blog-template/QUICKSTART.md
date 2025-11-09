# Quick Start - Get Your Blog Running in 5 Minutes

## Prerequisites
- Python 3.13+
- Git

## Step 1: Install Tools (2 min)
```bash
# Install cookiecutter
pip install cookiecutter

# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -
```

## Step 2: Generate Blog (1 min)
```bash
cookiecutter /path/to/mkdocs-blog-template
```

Answer the prompts (example):
```
full_name: Jane Smith
email: jane@example.com
github_username: janesmith
project_name: My Blog
site_name: Jane's Blog
site_description: Personal blog and reflections
domain_name: myblog.com
use_custom_domain: no
use_analytics: no
primary_color: lime
python_version: 3.13
```

## Step 3: Setup & Run (2 min)
```bash
cd my-blog
poetry install
poetry shell
make serve
```

Visit `http://127.0.0.1:8000/` - Your blog is running!

## Step 4: Deploy to GitHub Pages

### A. Create Repository
1. Go to https://github.com/new
2. **Repository name:** `yourusername.github.io` (replace with YOUR GitHub username!)
3. **Public** repository
4. **DO NOT** check any boxes (no README, no .gitignore)
5. Click "Create repository"

### B. Push Code
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/yourusername.github.io.git
git push -u origin main
```

### C. Enable GitHub Pages
1. Go to repo **Settings** → **Pages**
2. Wait for workflow to run (check **Actions** tab)
3. Once workflow completes, go back to Pages settings
4. Select Branch: **`gh-pages`** / Folder: **`/ (root)`**
5. Click **Save**

**Your blog will be live at `https://yourusername.github.io/` in 2-3 minutes!**

## Next Steps

1. Edit `docs/index.md` - Customize your homepage
2. Delete sample posts in `docs/posts/`
3. Create your first post in `docs/posts/reflections/`
4. Update homepage links to your new posts
5. Push changes: `git add . && git commit -m "first post" && git push`

See `USAGE_GUIDE.md` for detailed instructions!
