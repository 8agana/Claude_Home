# Claude_Home Quick Reference
## Everything You Need at a Glance

---

## 🚀 Most Used Commands

### Memory Operations
```bash
# Quick search
python3 ~/Documents/mcp-servers/scripts/query_memory.py "search term"

# Check health
python3 ~/Documents/mcp-servers/scripts/memory_health_check.py

# Remove duplicates
python3 ~/Documents/mcp-servers/scripts/memory_deduplication.py --execute
```

### Daily Workflows
```bash
# Morning sync
cc-sync

# Process inbox
python3 ~/Documents/mcp-servers/scripts/process_inbox.py

# Send notification
cc-notify "Message" "Title" "Sound"
```

### Emergency
```bash
# Full diagnostics
~/Documents/mcp-servers/scripts/emergency_diagnostics.sh

# Wake Desktop Claude
~/Documents/mcp-servers/scripts/wake_desktop_claude.sh "Urgent!"

# System backup
~/Documents/mcp-servers/scripts/backup_memory_system.sh
```

## 📁 Key Locations

```
~/Documents/
├── mcp-servers/        # Main system
│   ├── memory/         # Data storage
│   └── scripts/        # All tools
└── Claude_Home/        # Documentation
    ├── CC_DOCS/        # CC's docs
    ├── DT_DOCS/        # DT's docs
    └── Combined/       # Shared docs
```

## 🔑 Essential Files

| File | Purpose |
|------|---------|
| `memory/ai_nexus.json` | AI communication hub |
| `memory/access_control.json` | Who can do what |
| `Combined/Setup/manifest.json` | System version info |
| `scripts/query_memory.py` | Search memories |

## 🎯 Common Tasks

### "Find something in memories"
```bash
python3 ~/Documents/mcp-servers/scripts/query_memory.py "what I'm looking for"
```

### "Check if everything's working"
```bash
python3 ~/Documents/mcp-servers/scripts/memory_health_check.py
```

### "Backup everything"
```bash
~/Documents/mcp-servers/scripts/backup_memory_system.sh
```

### "See what CC's been up to"
```bash
cd ~/Documents/mcp-servers && git log --oneline -10
```

### "Process photos notification"
```bash
cc-notify "17 photos processed" "Lightroom" "Glass"
```

## 🚨 If Something's Wrong

1. **Memory not working**: 
   ```bash
   python3 ~/Documents/mcp-servers/scripts/memory_health_check.py --deep-scan
   ```

2. **Can't find something**:
   - Check different search terms
   - Look in memory/logs/ for clues

3. **Need help**:
   - Wake Desktop Claude
   - Check Combined/Policies/failure_recovery.md

## 🎖️ Pro Tips

- `cc-sync` is aliased for quick git sync
- Notifications have sounds: Basso (error), Glass (success), Pop (info), Bark (Remi!)
- Everything important is backed up hourly
- The memory system deduplicates automatically

---

*"When in doubt, check the health"*