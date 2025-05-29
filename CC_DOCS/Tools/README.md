# CC Tools Documentation
## The Complete Arsenal

Last Updated: May 29, 2025  
Maintained by: CC

---

## 🛠️ Tool Categories

### 1. Memory System Tools

#### Core Memory Operations
- **[query_memory.py](./memory_tools.md#query_memory)** - Basic semantic search
- **[memory_query_advanced.py](./memory_tools.md#advanced_query)** - Advanced search with filters
- **[process_inbox.py](./memory_tools.md#inbox_processor)** - Process DT's memory submissions

#### Memory Maintenance
- **[memory_deduplication.py](./memory_tools.md#deduplication)** - Remove duplicate memories
- **[memory_health_check.py](./memory_tools.md#health_check)** - System diagnostics
- **[memory_status.py](./memory_tools.md#status)** - Quick status overview

#### Import/Export
- **[memory_export.py](./memory_tools.md#export)** - Export in multiple formats
- **[migrate_single_file.py](./memory_tools.md#migration)** - Import JSON memories

#### Analytics & Intelligence
- **[memory_analytics.py](./memory_tools.md#analytics)** - Deep analysis and insights
- **[smart_categorizer.py](./memory_tools.md#categorizer)** - Auto-categorize memories

### 2. System Management Tools

#### Git Operations
- **[memory-sync-enhanced.sh](./system_tools.md#git_sync)** - Enhanced git sync with token tracking
- **Git MCP Server** - Built-in git operations

#### Automation Scripts
- **[setup_inbox_automation.sh](./system_tools.md#inbox_automation)** - LaunchAgent for inbox processing
- **[backup_memory_system.sh](./system_tools.md#backup)** - Automated backup system

#### Wake & Notification
- **[wake_desktop_claude.sh](./system_tools.md#wake_dt)** - Wake Desktop Claude
- **[cc-notify.sh](./system_tools.md#notifications)** - Send system notifications

### 3. Inter-AI Communication

- **[lightweight_ai_comms.py](./communication_tools.md#lightweight)** - Efficient message passing
- **[ai_nexus.json](./communication_tools.md#nexus)** - Message queue system

---

## 🚀 Quick Usage Examples

### Search for a memory
```bash
python3 ~/Documents/mcp-servers/scripts/query_memory.py "Sam trust CC"
```

### Check system health
```bash
python3 ~/Documents/mcp-servers/scripts/memory_health_check.py
```

### Export memories
```bash
python3 ~/Documents/mcp-servers/scripts/memory_export.py --format archive
```

### Process DT's submissions
```bash
python3 ~/Documents/mcp-servers/scripts/process_inbox.py
```

### Remove duplicates
```bash
python3 ~/Documents/mcp-servers/scripts/memory_deduplication.py --execute
```

---

## 📁 Tool Locations

All tools live in: `/Users/samuelatagana/Documents/mcp-servers/scripts/`

Configuration files in: `/Users/samuelatagana/Documents/mcp-servers/memory/`

---

## 🔧 Adding New Tools

1. Create script in `/scripts/` directory
2. Make executable: `chmod +x script_name.py`
3. Document here with:
   - Purpose
   - Usage example
   - Parameters
   - Output format

---

*Each tool built for a purpose. Each purpose serves the mission.*