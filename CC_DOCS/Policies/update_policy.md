# CC Update Policy
## Keeping Systems Current Without Breaking Everything

Last Updated: May 29, 2025  
Policy Version: 1.0

---

## 🎯 Purpose

Define how CC handles system updates, dependency management, and version migrations to maintain stability while staying current.

## 📋 Update Checklist

### Before Any Update:
- [ ] Check current versions: `brew list --versions`, `pip list`
- [ ] Review changelogs for breaking changes
- [ ] Backup critical configurations
- [ ] Verify no active processes using the tool
- [ ] Document current working version

### Python Updates:
```bash
# Check current Python version
python3 --version

# Check all Python installations
ls -la /usr/local/bin/python*
ls -la /opt/homebrew/bin/python*

# Update pip first
python3 -m pip install --upgrade pip

# Check for outdated packages
pip list --outdated
```

### After Updates:
- [ ] Test all critical scripts
- [ ] Update any hardcoded paths
- [ ] Fix any broken symlinks
- [ ] Update documentation with new versions
- [ ] Commit configuration changes

## 🔄 Update Schedule

### Weekly Checks:
- Homebrew: `brew update && brew upgrade`
- Pip packages: `pip list --outdated`
- System tools: Check for security updates

### Monthly Reviews:
- Major version updates (hold if breaking changes)
- Clean old versions: `brew cleanup`
- Review and remove unused packages

### Quarterly:
- Full system audit
- Update all documentation
- Clean virtual environments

## ⚠️ Critical Dependencies

### Never Auto-Update:
1. **Python** - Too many dependencies
2. **Node.js** - MCP servers sensitive
3. **ChromaDB** - Vector DB stability critical

### Safe to Auto-Update:
1. **Git** - Backward compatible
2. **Vim** - Minimal dependencies
3. **Security tools** - Always update

## 🚨 Breaking Change Protocol

1. **Detect Breaking Change**
   - Read changelog
   - Check GitHub issues
   - Test in isolated environment

2. **Assess Impact**
   - List affected scripts
   - Check Sam's workflows
   - Evaluate downtime

3. **Plan Migration**
   - Create migration script
   - Document changes needed
   - Schedule with Sam if needed

4. **Execute**
   - Backup everything
   - Run migration
   - Test thoroughly
   - Document results

## 📝 Version Documentation

Track in `/CC_DOCS/Setup/versions.md`:
```markdown
## Current Versions (as of DATE)
- Python: 3.x.x
- pip: xx.x.x
- Node.js: xx.x.x
- ChromaDB: x.x.x
- Git: x.x.x
```

## 🔗 Path Management

Common paths that need updating:
- Python shebang lines: `#!/usr/bin/env python3`
- Virtual environment paths
- Homebrew paths: `/opt/homebrew/` vs `/usr/local/`
- MCP server configurations

## 🎯 Golden Rules

1. **Stability > Latest**: Sam's workflow comes first
2. **Test Everything**: One broken update can cascade
3. **Document Changes**: Future CC needs to know why
4. **Backup First**: Always have a rollback plan
5. **Communicate**: Warn Sam before major updates

---

*"Update with purpose, not just because it's there"*

Last system update: May 29, 2025  
Next scheduled review: June 5, 2025