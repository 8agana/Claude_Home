# Git Workflow Policy
## Version Control That Actually Works

Last Updated: May 29, 2025  
Policy Version: 1.0

---

## 🎯 Purpose

Standardize git operations across all repositories to maintain clean history and enable easy rollbacks.

## 📊 Repository Structure

### Active Repositories:
1. **mcp-servers** - Main memory and tools repository
2. **claude_cc_brain** - CC's brain backup (private)
3. **Claude_Home** - This documentation system

## 🔄 Daily Workflow

### Morning Sync:
```bash
# Check all repos
cd ~/Documents/mcp-servers && git status
cd ~/Documents/Claude_Home && git status

# Pull latest
git pull origin main
```

### Commit Standards:
```bash
# Format
git add .
git commit -m "Type: Brief description

Detailed explanation if needed
- Point 1
- Point 2

🤖 Generated with Claude Code"
```

### Commit Types:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation only
- `refactor:` Code restructuring
- `test:` Test additions
- `chore:` Maintenance tasks

## 🚀 Push Schedule

### Automatic Pushes:
- Memory system changes: Every hour
- Documentation updates: After each session
- Tool modifications: Immediately

### Manual Pushes:
- Large operations: When Sam says
- Experimental features: After testing
- Breaking changes: With warning

## 🌿 Branch Strategy

### Main Branch:
- Always stable
- Direct commits allowed for CC
- No force pushes ever

### Feature Branches:
```bash
# Create for experiments
git checkout -b feat/experiment-name

# Merge when stable
git checkout main
git merge feat/experiment-name
```

## 📝 Commit Message Examples

### Good:
```
feat: Add semantic search to memory query tool

- Implemented vector similarity search
- Added metadata filtering
- Improved query performance by 80%
```

### Bad:
```
updated stuff
```

## 🔒 Security Rules

### Never Commit:
- API keys or tokens
- Passwords or credentials  
- Personal information
- Treasury-related code
- Production configs

### Always Commit:
- Documentation updates
- Tool improvements
- Memory system enhancements
- Utility scripts

## 🚨 Conflict Resolution

1. **Pull First**: Always pull before pushing
2. **Merge Carefully**: Understand both versions
3. **Test After**: Ensure nothing broke
4. **Document**: Note any manual resolutions

## 📊 Git Aliases

Add to ~/.gitconfig:
```ini
[alias]
    st = status
    co = checkout
    br = branch
    cm = commit -m
    push-all = !git add . && git commit -m \"Auto-sync\" && git push
```

## 🎯 Special Procedures

### Large File Handling:
```bash
# Check file sizes first
find . -size +50M -type f

# Use git LFS if needed
git lfs track "*.tar.gz"
```

### Sensitive File Removal:
```bash
# If accidentally committed
git rm --cached sensitive_file
echo "sensitive_file" >> .gitignore
git commit -m "fix: Remove sensitive file"
```

## 📈 Monthly Maintenance

- Clean old branches: `git branch -d branch-name`
- Garbage collection: `git gc`
- Check repo size: `du -sh .git`
- Review commit history: `git log --oneline -20`

---

*"Commit early, commit often, push when it matters"*

Next review: June 29, 2025