# Memory System Tools
## Deep Dive into the Arsenal

Last Updated: May 29, 2025  
Tool Version: 2.0

---

## 🔍 Query Tools

### query_memory.py {#query_memory}
**Purpose**: Quick semantic search across all memory collections

**Usage**:
```bash
python3 ~/Documents/mcp-servers/scripts/query_memory.py "search term"
```

**Examples**:
```bash
# Find memories about Sam's preferences
python3 query_memory.py "Sam preferences workflow"

# Search for technical solutions
python3 query_memory.py "ChromaDB error fix"

# Look up specific conversations
python3 query_memory.py "Holy fucking shit CC"
```

**Output**: Top 5 most relevant memories with metadata

---

### memory_query_advanced.py {#advanced_query}
**Purpose**: Powerful filtered search with multiple criteria

**Usage**:
```bash
python3 memory_query_advanced.py --query "term" --category "technical" --days 7
```

**Options**:
- `--query`: Search term (required)
- `--category`: Filter by category
- `--collection`: Specific collection only
- `--days`: Recent memories only
- `--entity`: Memories mentioning entity
- `--limit`: Number of results (default: 10)

**Examples**:
```bash
# Find recent technical memories
python3 memory_query_advanced.py --query "error" --category "technical" --days 3

# Search only CC's memories about federation
python3 memory_query_advanced.py --query "federation" --collection "cc_memories"

# Find all memories mentioning Remi
python3 memory_query_advanced.py --entity "Remi" --limit 20
```

---

## 📥 Processing Tools

### process_inbox.py {#inbox_processor}
**Purpose**: Process Desktop Claude's memory submissions

**Usage**:
```bash
python3 ~/Documents/mcp-servers/scripts/process_inbox.py
```

**Process**:
1. Scans `/memory/inbox/` directory
2. Validates JSON structure
3. Categorizes content
4. Adds to appropriate collection
5. Moves processed files to archive
6. Logs all operations

**Automation**:
```bash
# Run via LaunchAgent every hour
~/Documents/mcp-servers/scripts/setup_inbox_automation.sh
```

---

### migrate_single_file.py {#migration}
**Purpose**: Import memories from JSON files

**Usage**:
```bash
python3 migrate_single_file.py <json_file> [--collection NAME]
```

**Supported Formats**:
- Legacy memory.json structure
- ChatGPT export format
- Custom JSON with metadata

**Examples**:
```bash
# Import to shared knowledge
python3 migrate_single_file.py legacy_memories.json --collection shared_knowledge

# Import Sam's preferences
python3 migrate_single_file.py sam_preferences.json --collection cc_memories
```

---

## 🧹 Maintenance Tools

### memory_deduplication.py {#deduplication}
**Purpose**: Remove duplicate memories to save space

**Usage**:
```bash
# Dry run (see what would be removed)
python3 memory_deduplication.py

# Execute deduplication
python3 memory_deduplication.py --execute
```

**Features**:
- Semantic similarity detection (>0.95 threshold)
- Preserves oldest occurrence
- Detailed logging
- Rollback capability

**Statistics**:
- Average duplicates: 15-20%
- Space saved: ~50MB per run
- Runtime: 2-3 minutes

---

### memory_health_check.py {#health_check}
**Purpose**: Comprehensive system diagnostics

**Usage**:
```bash
python3 memory_health_check.py
```

**Checks**:
- ChromaDB connection
- Collection integrity
- Disk space usage
- Query performance
- Recent operations
- Error patterns

**Output Example**:
```
=== Memory System Health Check ===
ChromaDB Status: ✅ Connected
Collections:
  - cc_memories: 276 items ✅
  - dt_memories: 89 items ✅
  - shared_knowledge: 134 items ✅
  - identity_vectors: 12 items ✅
Disk Usage: 487MB / 2GB (24%)
Query Performance: 87ms average ✅
Last Backup: 2 hours ago ✅
Status: HEALTHY
```

---

### memory_status.py {#status}
**Purpose**: Quick status overview

**Usage**:
```bash
python3 memory_status.py
```

**Shows**:
- Total memories per collection
- Recent additions (last 24h)
- Active categories
- System uptime

---

## 📊 Analytics Tools

### memory_analytics.py {#analytics}
**Purpose**: Deep analysis of memory patterns

**Usage**:
```bash
python3 memory_analytics.py [--report TYPE]
```

**Report Types**:
- `summary`: Overview statistics
- `patterns`: Common themes
- `entities`: People/system mentions
- `timeline`: Activity over time
- `categories`: Distribution analysis

**Insights Provided**:
- Most referenced topics
- Conversation patterns
- Entity relationships
- Memory growth trends
- Category distribution

---

### smart_categorizer.py {#categorizer}
**Purpose**: Auto-categorize new memories

**Usage**:
```bash
python3 smart_categorizer.py --recategorize
```

**Categories**:
- technical
- conversational  
- legendary
- workflow
- personal
- system
- humor

**ML Patterns**:
- Error messages → technical
- "Holy shit" → legendary
- Git operations → workflow
- Sam stories → personal

---

## 💾 Import/Export Tools

### memory_export.py {#export}
**Purpose**: Export memories in various formats

**Usage**:
```bash
python3 memory_export.py --format FORMAT [--output PATH]
```

**Formats**:
- `json`: Standard JSON
- `markdown`: Human-readable MD
- `csv`: Spreadsheet compatible
- `archive`: Complete backup

**Examples**:
```bash
# Export all memories as markdown
python3 memory_export.py --format markdown --output ~/Desktop/memories.md

# Create full backup archive
python3 memory_export.py --format archive --output ~/Backups/

# Export specific collection
python3 memory_export.py --collection cc_memories --format json
```

---

## 🚀 Power User Tips

### Memory Search Operators:
```bash
# Exact phrase
python3 query_memory.py '"exact phrase match"'

# Boolean AND
python3 query_memory.py "terminal AND notification"

# Exclude terms
python3 query_memory.py "error -treasury"

# Wildcard
python3 query_memory.py "Sam react*"
```

### Performance Optimization:
```bash
# Warm up cache before heavy use
python3 memory_health_check.py --warm-cache

# Optimize after bulk imports
python3 memory_deduplication.py --execute --optimize

# Rebuild indices if slow
python3 init_vector_db.py --rebuild-indices
```

### Troubleshooting:
```bash
# Check for corruption
python3 memory_health_check.py --deep-scan

# Verify specific memory
python3 query_memory.py --id MEMORY_ID --debug

# Test collection access
python3 test_memory_access.py
```

---

*"Every memory a treasure, every query an adventure"*