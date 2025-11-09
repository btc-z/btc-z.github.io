# How to Use This Template - Step by Step Guide

This guide will walk you through creating your own blog using this cookiecutter template.

## Step 1: Install Cookiecutter

First, you need to install cookiecutter, a tool that generates projects from templates.

```bash
# Using pip
pip install cookiecutter

# Or using pipx (recommended)
pipx install cookiecutter
```

## Step 2: Generate Your Blog

Run cookiecutter with this template:

```bash
# If the template is on GitHub (replace with actual URL):
cookiecutter https://github.com/YOUR-USERNAME/mkdocs-blog-template

# Or if you have it locally:
cookiecutter /path/to/mkdocs-blog-template
```

## Step 3: Answer the Prompts

Cookiecutter will ask you several questions. Here's what each one means:

### Basic Information

**full_name** (e.g., "Jane Smith")
- Your full name that will appear in the copyright and author fields

**email** (e.g., "jane@example.com")
- Your email address for the project metadata

**github_username** (e.g., "janesmith")
- Your GitHub username (important for GitHub Pages URL)

**project_name** (e.g., "My Awesome Blog")
- The name of your blog project
- This will be converted to a folder name automatically

**site_name** (e.g., "Jane's Blog")
- The display name that appears on your website

**site_description** (e.g., "Personal blog about tech and life")
- A brief description of your blog

### Domain Configuration

**domain_name** (e.g., "janeblog.com")
- Your custom domain if you have one
- If you don't have one yet, just use a placeholder like "myblog.com"

**use_custom_domain**
- Select `yes` if you have a custom domain configured
- Select `no` if you'll use GitHub Pages default URL (username.github.io)

### Analytics (Optional)

**use_analytics**
- Select `yes` if you want to track visitors with Google Analytics
- Select `no` to skip this (you can add it later)

**google_analytics_id** (e.g., "G-XXXXXXXXXX")
- Your Google Analytics tracking ID
- Get this from https://analytics.google.com/
- Only needed if you selected `yes` for use_analytics

### Customization

**primary_color**
- Choose your theme color from the list:
  - lime (default, bright green)
  - indigo (blue-purple)
  - purple
  - pink
  - red
  - orange
  - amber (yellow-orange)
  - teal (blue-green)
  - cyan (light blue)
  - blue

**python_version**
- Default is 3.13, just press Enter unless you need a different version

## Step 4: Navigate to Your New Blog

```bash
cd my-awesome-blog  # Replace with your actual project name
```

## Step 5: Install Poetry (if not already installed)

Poetry is a Python package manager that makes dependency management easy.

```bash
# On macOS/Linux/WSL
curl -sSL https://install.python-poetry.org | python3 -

# On Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

After installation, close and reopen your terminal.

## Step 6: Install Blog Dependencies

```bash
poetry install
```

This will create a virtual environment and install all necessary packages (MkDocs, Material theme, plugins, etc.).

## Step 7: Start Local Development Server

```bash
# Activate the virtual environment
poetry shell

# Start the server
make serve
```

Open your browser and go to `http://127.0.0.1:8000/` to see your blog!

Press `Ctrl+C` to stop the server when you're done.

## Step 8: Customize Your Blog

### Update the Homepage

Edit `docs/index.md` to customize your welcome message and about section.

### Delete Sample Posts

```bash
rm docs/posts/reflections/welcome.md
rm docs/posts/books/sample-book-review.md
```

### Add Your First Post

Create a new file, for example `docs/posts/reflections/my-first-post.md`:

```yaml
---
draft: false
date: 2024-01-15
categories:
    - reflections
---

# My First Post

This is my first blog post! I'm excited to start sharing my thoughts.

## What I'll Write About

- Technology
- Books I'm reading
- Personal reflections

Stay tuned for more!
```

### Update Homepage Links

Edit `docs/index.md` to link to your new post:

```markdown
### :ocean: Reflections

- **2024-01-15 :sparkles: [My First Post](posts/reflections/my-first-post.md)**
```

## Step 9: Deploy to GitHub Pages

GitHub Pages is a free hosting service from GitHub that lets you host your blog directly from a GitHub repository.

### IMPORTANT: Repository Naming

**For your main personal/organization site:**
- Repository name MUST be: `yourusername.github.io`
- Example: If your GitHub username is `janesmith`, the repo must be `janesmith.github.io`
- Your site will be at: `https://janesmith.github.io/`

**For a project site (alternative):**
- Repository name can be anything: `my-blog`, `personal-site`, etc.
- Your site will be at: `https://yourusername.github.io/repository-name/`
- Note: You'll need to adjust the `site_url` in `mkdocs.yml` for project sites

### Create a GitHub Repository

1. **Go to** https://github.com/new

2. **Repository name:**
   - **Recommended:** `yourusername.github.io` (replace `yourusername` with your actual GitHub username)
   - Example: `janesmith.github.io`

3. **Settings:**
   - Make it **Public** (required for free GitHub Pages)
   - **DO NOT** check "Add a README file" (we already have one)
   - **DO NOT** add .gitignore (we already have one)
   - **DO NOT** choose a license yet (optional, can add later)

4. Click **"Create repository"**

### Push Your Code to GitHub

Copy the commands from GitHub's quick setup page, or use these:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: My new blog"

# Rename branch to main (if not already)
git branch -M main

# Add GitHub as remote (REPLACE 'yourusername' with your actual username!)
git remote add origin https://github.com/yourusername/yourusername.github.io.git

# Push to GitHub
git push -u origin main
```

**IMPORTANT:** Replace `yourusername` with your actual GitHub username in the remote URL!

### Configure GitHub Pages

After pushing, the GitHub Actions workflow will run automatically, but you need to enable GitHub Pages:

1. **Go to your repository** on GitHub

2. **Click "Settings" tab** (top right)

3. **Click "Pages"** in the left sidebar (under "Code and automation")

4. **Under "Build and deployment":**
   - **Source:** Select "Deploy from a branch"
   - **Branch:** Select `gh-pages` (this will appear after the first workflow runs)
   - **Folder:** Select `/ (root)`

5. **Click "Save"**

### Wait for Deployment

1. **Go to the "Actions" tab** in your repository (top menu)

2. You should see a workflow called "Deploy MkDocs to GitHub Pages" running

3. **Wait for it to complete** (usually 1-2 minutes)
   - Green checkmark ✓ = Success
   - Red X = Failed (click to see error logs)

4. **Go back to Settings → Pages**
   - You should see: "Your site is live at https://yourusername.github.io/"

5. **Click the URL** or visit `https://yourusername.github.io/`

### Troubleshooting Deployment

**"gh-pages branch not showing up":**
- Wait for the first GitHub Actions workflow to complete
- The workflow automatically creates the `gh-pages` branch
- Refresh the Pages settings page after the workflow finishes

**"404 - Page not found":**
- Wait a few minutes (can take up to 10 minutes for first deployment)
- Make sure you selected the `gh-pages` branch (not `main`)
- Check that the repository is Public
- Clear your browser cache

**"Workflow failed":**
- Go to Actions tab and click on the failed workflow
- Read the error message
- Common issues:
  - Python version mismatch
  - Missing dependencies
  - Syntax errors in `mkdocs.yml`

**"Site is blank/not styled":**
- If using a project site (not username.github.io), you need to set `site_url` in `mkdocs.yml`
- Example: `site_url: https://yourusername.github.io/repository-name/`

## Step 10: Set Up Custom Domain (Optional)

If you selected `yes` for custom domain:

1. **Buy a domain** from a provider like:
   - Namecheap
   - Google Domains
   - Cloudflare

2. **Configure DNS** with your domain provider:
   - Add a CNAME record:
     - Name: `www` (or `@` for apex domain)
     - Value: `yourusername.github.io`

3. **Update GitHub Pages**:
   - Go to Settings → Pages
   - Under "Custom domain", enter your domain
   - Check "Enforce HTTPS"

4. **Wait for DNS propagation** (can take up to 48 hours)

## Step 11: Regular Workflow

Once everything is set up, your regular workflow will be:

1. **Start local server**: `poetry shell` → `make serve`
2. **Create new post**: Add markdown file in `docs/posts/`
3. **Update homepage**: Add link to new post in `docs/index.md`
4. **Preview locally**: Check `http://127.0.0.1:8000/`
5. **Commit changes**: `git add .` → `git commit -m "post: title"`
6. **Push to GitHub**: `git push`
7. **Wait for deployment**: Check Actions tab (automatic)

## Common Commands

```bash
# Start virtual environment
poetry shell

# Start local server
make serve

# Build site locally
make build

# Clean build files
make clean

# Exit virtual environment
exit
```

## Tips for Success

1. **Always preview locally** before pushing
2. **Use descriptive commit messages** (e.g., "post: My thoughts on Python")
3. **Use YAML frontmatter** in all posts for proper metadata
4. **Add images to `docs/assets/`** and reference them with `/assets/image.png`
5. **Check the GitHub Actions tab** if your site doesn't update
6. **Read the generated README.md** for more detailed customization options

## Getting Help

- Check the generated `README.md` in your blog
- Read [MkDocs Material docs](https://squidfunk.github.io/mkdocs-material/)
- Check [GitHub Pages docs](https://docs.github.com/en/pages)
- Look at the sample posts for markdown examples

## Troubleshooting

### "poetry: command not found"
- Reinstall Poetry using the official installer
- Make sure Poetry is in your PATH
- Close and reopen your terminal

### Local server won't start
- Make sure you're in the poetry shell: `poetry shell`
- Check Python version: `python --version` (should be 3.13+)
- Try reinstalling: `poetry install`

### Changes not showing on live site
- Check GitHub Actions for build errors
- Wait a few minutes for GitHub Pages to update
- Clear your browser cache
- Check if you pushed to the correct branch (`main`)

### Custom domain not working
- Wait up to 48 hours for DNS propagation
- Check DNS settings with your domain provider
- Make sure `docs/CNAME` contains your domain
- Check GitHub Pages settings

---

Congratulations! You now have a beautiful blog. Happy writing! ✨
