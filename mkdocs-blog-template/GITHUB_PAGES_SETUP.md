# GitHub Pages Setup Guide - Visual Walkthrough

This guide will help you deploy your blog to GitHub Pages so it's accessible at `https://yourusername.github.io/`

## Prerequisites

- [ ] You have a GitHub account
- [ ] You know your GitHub username
- [ ] You've generated your blog using the cookiecutter template
- [ ] You've tested it locally with `make serve`

## Understanding GitHub Pages

**GitHub Pages** is a free web hosting service from GitHub that:
- Hosts static websites directly from a GitHub repository
- Is completely free for public repositories
- Provides HTTPS by default
- Updates automatically when you push changes

## Repository Naming - CRITICAL!

### For Your Main Personal Website (Recommended)

**Repository name MUST be:** `<your-github-username>.github.io`

**Example:**
- GitHub username: `janedoe`
- Repository name: `janedoe.github.io` ✅
- Website URL: `https://janedoe.github.io/`

**Why this matters:**
- This exact naming format tells GitHub this is your user site
- The URL will be clean: `yourusername.github.io` (no extra path)
- You can only have ONE user site per account

### Alternative: Project Site

If you already have a `username.github.io` repo, you can create a project site:

**Repository name:** Any name (e.g., `my-blog`, `personal-blog`)

**Example:**
- GitHub username: `janedoe`
- Repository name: `my-blog`
- Website URL: `https://janedoe.github.io/my-blog/`

**Note:** Project sites require additional configuration in `mkdocs.yml`:
```yaml
site_url: https://yourusername.github.io/repository-name/
```

## Step-by-Step Setup

### Step 1: Create GitHub Repository

1. **Open your browser** and go to: https://github.com/new

2. **Repository name:**
   - Type: `yourusername.github.io`
   - **IMPORTANT:** Replace `yourusername` with YOUR actual GitHub username
   - Example: If your username is `janedoe`, type `janedoe.github.io`

3. **Repository settings:**
   - Description: (optional) "Personal blog built with MkDocs Material"
   - **Public** ← MUST be public for free GitHub Pages
   - **DO NOT** check "Add a README file"
   - **DO NOT** check "Add .gitignore"
   - **DO NOT** choose a license

4. **Click "Create repository"**

You'll see a page with setup instructions - we'll use some of these!

### Step 2: Connect Your Local Blog to GitHub

Open your terminal in your blog directory:

```bash
# Make sure you're in the blog directory
cd my-blog  # Replace with your actual directory name

# Initialize git (if not already done)
git init

# Add all files
git add .

# Create your first commit
git commit -m "Initial commit: My blog"

# Rename branch to main (GitHub's default)
git branch -M main

# Connect to GitHub (REPLACE 'yourusername' and 'repo-name'!)
git remote add origin https://github.com/yourusername/yourusername.github.io.git

# Push to GitHub
git push -u origin main
```

**IMPORTANT:** In the `git remote add origin` command, replace:
- `yourusername` with your GitHub username (twice!)
- The full URL should match your repository

**Example:**
```bash
git remote add origin https://github.com/janedoe/janedoe.github.io.git
```

### Step 3: Wait for GitHub Actions

1. **Go to your repository** on GitHub: `https://github.com/yourusername/yourusername.github.io`

2. **Click the "Actions" tab** at the top

3. You should see a workflow called **"Deploy MkDocs to GitHub Pages"** running

4. **Wait for it to complete** (usually 1-2 minutes)
   - Yellow circle ⚪ = Running
   - Green checkmark ✅ = Success! Continue to next step
   - Red X ❌ = Failed - click on it to see error details

**What's happening?**
The GitHub Actions workflow automatically:
- Installs Python and dependencies
- Builds your MkDocs site
- Creates a `gh-pages` branch
- Pushes the built site to that branch

### Step 4: Configure GitHub Pages

1. **Go to your repository** on GitHub

2. **Click "Settings"** tab (top right)

3. **In the left sidebar**, scroll down and click **"Pages"** (under "Code and automation")

4. **Under "Build and deployment":**

   **Source:**
   - Select **"Deploy from a branch"**

   **Branch:**
   - Dropdown 1: Select **`gh-pages`** (not `main`!)
   - Dropdown 2: Select **`/ (root)`**

5. **Click "Save"**

6. **Wait for the page to refresh** - you should see a message:
   ```
   Your site is live at https://yourusername.github.io/
   ```

### Step 5: Visit Your Live Site

1. **Wait 1-2 minutes** for the deployment to complete

2. **Open your browser** and go to:
   ```
   https://yourusername.github.io/
   ```
   (Replace `yourusername` with your GitHub username)

3. **Your blog is live!** 🎉

## How Future Updates Work

After this initial setup, publishing new posts is simple:

```bash
# 1. Create or edit posts in docs/posts/
# 2. Preview locally
make serve

# 3. Commit your changes
git add .
git commit -m "post: My new blog post"

# 4. Push to GitHub
git push

# 5. Wait 2-3 minutes - your site updates automatically!
```

**No need to:**
- Re-configure GitHub Pages
- Manually build the site
- Deploy anything yourself

GitHub Actions handles everything!

## Visual Checklist

Use this checklist to verify your setup:

- [ ] Created repository named `yourusername.github.io`
- [ ] Repository is **Public**
- [ ] Pushed code to GitHub successfully
- [ ] GitHub Actions workflow completed successfully (green checkmark)
- [ ] Configured Pages to use `gh-pages` branch
- [ ] Can see "Your site is live at..." message in Pages settings
- [ ] Can access blog at `https://yourusername.github.io/`

## Troubleshooting

### Problem: "gh-pages branch not available in dropdown"

**Solution:**
- Wait for the GitHub Actions workflow to complete first
- The workflow creates the `gh-pages` branch
- Refresh the Pages settings page
- If still not there, check the Actions tab for errors

### Problem: "404 - There isn't a GitHub Pages site here"

**Solutions:**
1. **Wait** - First deployment can take up to 10 minutes
2. **Check branch** - Make sure you selected `gh-pages` (not `main`)
3. **Check repository** - Must be Public
4. **Clear cache** - Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
5. **Check Actions** - Make sure workflow completed successfully

### Problem: "Workflow failed with error"

**Solutions:**
1. Click on the failed workflow in the Actions tab
2. Read the error message
3. Common issues:
   - **Python version mismatch**: Update `python-version` in `.github/workflows/cicd.yml`
   - **Syntax error in mkdocs.yml**: Check for proper YAML formatting
   - **Missing dependencies**: Make sure `pyproject.toml` is correct

### Problem: "Site loads but has no styling"

**Solution:**
- This usually happens with project sites (not `username.github.io` repos)
- Add to `mkdocs.yml`:
  ```yaml
  site_url: https://yourusername.github.io/repository-name/
  ```
- Commit and push the change

### Problem: "Site shows old content after pushing updates"

**Solutions:**
1. Check Actions tab - make sure workflow completed
2. Wait a few minutes
3. Hard refresh your browser: Ctrl+Shift+R or Cmd+Shift+R
4. Clear browser cache
5. Try incognito/private window

## Understanding the GitHub Actions Workflow

The workflow file (`.github/workflows/cicd.yml`) does this automatically:

```yaml
1. When you push to main branch
   ↓
2. GitHub Actions starts
   ↓
3. Installs Python and Poetry
   ↓
4. Installs your blog dependencies
   ↓
5. Runs: mkdocs gh-deploy
   ↓
6. Builds your site
   ↓
7. Pushes to gh-pages branch
   ↓
8. GitHub Pages serves the site
```

You don't need to understand this - it just works! But it's good to know what happens behind the scenes.

## Next Steps

Once your blog is live:

1. **Share your URL:** `https://yourusername.github.io/`
2. **Add custom domain** (optional): See `USAGE_GUIDE.md`
3. **Set up Google Analytics** (optional): Edit `mkdocs.yml`
4. **Start writing!**

## Need More Help?

- **Detailed setup:** See `USAGE_GUIDE.md`
- **General questions:** See main `README.md`
- **GitHub Pages docs:** https://docs.github.com/en/pages
- **MkDocs Material:** https://squidfunk.github.io/mkdocs-material/

---

Congratulations! Your blog is live on the internet! 🎉
