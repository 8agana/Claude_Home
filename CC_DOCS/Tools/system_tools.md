# System Management Tools
## The Infrastructure Arsenal

Last Updated: May 29, 2025  
Tool Version: 2.0

---

## 🔄 Git & Sync Tools

### memory-sync-enhanced.sh {#git_sync}
**Purpose**: Enhanced git operations with token tracking

**Location**: `/Users/samuelatagana/Documents/mcp-servers/scripts/memory-sync-enhanced.sh`

**Features**:
- Token usage tracking
- Automatic add/commit/push
- Detailed change summaries
- Error handling
- Time tracking

**Usage**:
```bash
# Run directly
~/Documents/mcp-servers/scripts/memory-sync-enhanced.sh

# Or use alias
cc-sync
```

**Output Example**:
```
📊 Token Check:
Total tokens used: 1,247,832
Percentage of 5M: 24.96%

🚀 Starting memory sync...
✅ Added files: 3 new memories
📝 Committed: Memory sync - 3 new entries
🔄 Pushed to origin/main
⏱️  Sync completed in 4.2 seconds
```

---

## 🤖 Automation Tools

### setup_inbox_automation.sh {#inbox_automation}
**Purpose**: Configure LaunchAgent for inbox processing

**Usage**:
```bash
# Install automation
~/Documents/mcp-servers/scripts/setup_inbox_automation.sh

# Check status
launchctl list | grep inbox

# View logs
tail -f ~/Documents/mcp-servers/memory/logs/inbox_processor.log
```

**LaunchAgent Details**:
- Runs every hour
- Processes DT submissions
- Logs all operations
- Handles errors gracefully

---

### backup_memory_system.sh {#backup}
**Purpose**: Comprehensive memory system backup

**Features**:
- Full ChromaDB backup
- Configuration files
- Scripts directory
- Compressed archive
- Rotation policy (keep 7)

**Usage**:
```bash
# Run backup
~/Documents/mcp-servers/scripts/backup_memory_system.sh

# Restore from backup
~/Documents/mcp-servers/scripts/restore_memory_backup.sh backup_20250529.tar.gz
```

**Backup Locations**:
```
~/Documents/mcp-servers/backups/
├── memory_backup_20250529_030000.tar.gz
├── memory_backup_20250528_030000.tar.gz
└── ...
```

---

## 🔔 Notification & Wake Tools

### wake_desktop_claude.sh {#wake_dt}
**Purpose**: Wake Desktop Claude for urgent matters

**Usage**:
```bash
# Wake with default message
~/Documents/mcp-servers/scripts/wake_desktop_claude.sh

# Wake with custom message
~/Documents/mcp-servers/scripts/wake_desktop_claude.sh "Photos processed!"
```

**How it Works**:
1. Activates Claude app
2. Types message
3. Sends Enter key
4. DT sees notification

**When to Use**:
- Urgent tasks completed
- Errors needing attention
- Important discoveries
- Sam requests

---

### cc-notify.sh {#notifications}
**Purpose**: Send system notifications with sound

**Location**: `/usr/local/bin/cc-notify`

**Usage**:
```bash
# Default notification
cc-notify "Task complete"

# With title
cc-notify "Task complete" "CC Status"

# With sound
cc-notify "Task complete" "CC Status" "Glass"
```

**Available Sounds**:
- Basso (error/warning)
- Glass (completion)
- Pop (info)
- Bark (Remi alerts!)

**Examples**:
```bash
# Photo processing done
cc-notify "17 photos processed" "Lightroom" "Glass"

# Error notification
cc-notify "Memory system error" "CRITICAL" "Basso"

# Remi alert
cc-notify "Remi detected near cables" "Pet Alert" "Bark"
```

---

## 📊 Monitoring Tools

### system_health_monitor.py
**Purpose**: Monitor system resources and performance

**Usage**:
```bash
python3 ~/Documents/mcp-servers/scripts/system_health_monitor.py
```

**Monitors**:
- CPU usage
- Memory consumption
- Disk space
- Process count
- Network activity

**Alerts When**:
- CPU > 80% for 5 min
- Memory > 90%
- Disk < 10GB free
- Zombie processes
- Network errors

---

### token_tracker.py
**Purpose**: Track token usage across sessions

**Usage**:
```bash
# Check current usage
python3 token_tracker.py --status

# Reset counter
python3 token_tracker.py --reset

# Set warning threshold
python3 token_tracker.py --warn-at 4000000
```

**Features**:
- Real-time tracking
- Session history
- Usage predictions
- Warning notifications

---

## 🛠️ Utility Scripts

### cleanup_old_logs.sh
**Purpose**: Maintain log file sizes

**Usage**:
```bash
# Clean logs older than 7 days
./cleanup_old_logs.sh

# Custom retention
./cleanup_old_logs.sh --days 30
```

**Cleans**:
- System logs
- Error logs
- Debug output
- Temporary files

---

### fix_permissions.sh
**Purpose**: Fix common permission issues

**Usage**:
```bash
# Fix all script permissions
./fix_permissions.sh

# Fix specific directory
./fix_permissions.sh /path/to/directory
```

**Fixes**:
- Script execute bits
- Directory access
- File ownership
- LaunchAgent permissions

---

## 🚀 Power Tools

### multi_device_sync.sh
**Purpose**: Sync across all CC instances

**Usage**:
```bash
# Sync to all devices
./multi_device_sync.sh

# Specific device
./multi_device_sync.sh --device m1-macbook
```

**Syncs**:
- Memory databases
- Configuration
- Scripts
- Documentation

---

### emergency_diagnostics.sh
**Purpose**: Comprehensive system analysis

**Usage**:
```bash
# Run full diagnostics
./emergency_diagnostics.sh > diagnostics_$(date +%Y%m%d).txt
```

**Generates**:
- System state snapshot
- Recent errors
- Performance metrics
- Configuration dump
- Recommendation report

---

## 📝 Usage Patterns

### Daily Routine:
```bash
# Morning health check
python3 memory_health_check.py
./system_health_monitor.py

# Hourly sync
cc-sync

# Evening backup
./backup_memory_system.sh
```

### Problem Solving:
```bash
# Something's wrong
./emergency_diagnostics.sh

# Fix permissions
./fix_permissions.sh

# Check logs
tail -f ~/Documents/mcp-servers/memory/logs/*.log

# Notify Sam
cc-notify "System issue detected - check diagnostics" "CC Alert" "Basso"
```

### Maintenance:
```bash
# Weekly cleanup
./cleanup_old_logs.sh
python3 memory_deduplication.py --execute

# Monthly review
python3 memory_analytics.py --report monthly
./system_performance_report.sh
```

---

*"With great tools comes great capability"*