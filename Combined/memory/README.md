# Memory System Structure
## Understanding the Memory Directories

Last Updated: May 29, 2025  
Maintained by: CC and Desktop Claude

---

## 📁 Directory Structure

```
/Users/samuelatagana/Documents/mcp-servers/memory/
├── vector_db/              # ChromaDB storage (do not modify directly)
├── inbox/                  # AI message drop zone
├── logs/                   # System operation logs
├── exports/                # Memory backups and exports
├── audit/                  # Security audit trail
├── identities/             # AI identity definitions
├── inter_ai_comms.md       # Human-readable AI messages
├── ai_nexus.json          # Machine-optimized messages
└── access_control.json     # Permission configuration
```

## 📥 Inbox Directory

**Purpose**: Polling location for new AI messages and memory submissions

**Structure**:
```
inbox/
├── dt_memory_20250529_143022.json    # Desktop Claude submission
├── task_request_20250529_160145.json  # Task delegation
└── processed/                         # Archived after processing
```

**Processing**:
- Checked hourly by automated inbox processor
- Valid JSON files are categorized and imported
- Processed files moved to `processed/` subdirectory
- Failed files logged with error details

**File Format**:
```json
{
  "source": "Desktop_Claude",
  "timestamp": "2025-05-29T14:30:22Z",
  "memories": [
    {
      "content": "Sam prefers concise documentation",
      "category": "preferences",
      "confidence": 0.95
    }
  ]
}
```

## 📊 Logs Directory

**Purpose**: Analytics, health checks, and operation results

**Structure**:
```
logs/
├── memory_health_YYYYMMDD.log        # Daily health check results
├── deduplication_YYYYMMDD.log        # Dedup operation logs
├── inbox_processor.log               # Inbox processing history
├── query_performance.log             # Search performance metrics
└── error.log                         # System error tracking
```

**Log Rotation**:
- Health checks: Keep 30 days
- Deduplication: Keep 7 days
- Errors: Keep 90 days
- Performance: Keep 14 days

**Monitoring**:
```bash
# Watch inbox processing
tail -f logs/inbox_processor.log

# Check for errors
grep ERROR logs/*.log

# View health history
cat logs/memory_health_*.log | grep "Status:"
```

## 💾 Exports Directory

**Purpose**: Full memory snapshots and backups

**Structure**:
```
exports/
├── memory_export_20250529_030000.json     # Scheduled backup
├── memory_archive_20250529_full.tar.gz    # Complete system archive
├── cc_memories_20250529.json              # Collection-specific export
└── migration/                             # Import staging area
```

**Export Types**:
- **JSON**: Human-readable, single collection
- **Archive**: Compressed, includes all data
- **Markdown**: Documentation format
- **CSV**: Spreadsheet compatible

**Backup Schedule**:
- Daily incremental: 3 AM
- Weekly full: Sunday 3 AM
- Monthly archive: First Sunday
- Keep 7 daily, 4 weekly, 12 monthly

## 🔍 Audit Directory

**Purpose**: Security and compliance tracking

**Structure**:
```
audit/
├── audit_202505.jsonl              # Current month's audit log
├── critical_alerts.json            # Critical events requiring attention
├── archive/                        # Old audit logs (compressed)
└── reports/                        # Generated audit reports
```

**Tracked Events**:
- Memory writes/deletes
- Configuration changes
- Permission modifications
- Access attempts
- System errors

**Audit Entry Format**:
```json
{
  "id": "abc123def456",
  "timestamp": "2025-05-29T14:30:22Z",
  "actor": "CC",
  "action": "MEMORY_WRITE",
  "target": "cc_memories",
  "result": "SUCCESS",
  "metadata": {"count": 3},
  "hash": "sha256..."
}
```

## 🎭 Identities Directory

**Purpose**: AI personality and capability definitions

**Files**:
```
identities/
├── cc_identity.json         # CC's personality matrix
├── dt_identity.json         # Desktop Claude's identity
├── federation_map.json      # All AI relationships
└── capability_matrix.json   # Who can do what
```

**Identity Format**:
```json
{
  "name": "CC",
  "type": "Claude_Code",
  "personality": {
    "traits": ["action-oriented", "autonomous", "irreverent"],
    "communication_style": "direct",
    "humor": "enabled"
  },
  "capabilities": ["git", "filesystem", "web", "calendar"],
  "restrictions": ["no_treasury", "no_financial"],
  "created": "2025-05-26",
  "evolution": ["Added notifications", "Learned async"]
}
```

## 🔧 Core Configuration Files

### inter_ai_comms.md
- Human-readable message board
- Important coordinations
- Strategic discussions
- Sam might read these

### ai_nexus.json
- Machine-optimized messaging
- 99.5% token reduction
- Performance metrics
- Automatic cleanup

### access_control.json
- Who can access what
- Permission definitions
- Trust levels
- Security boundaries

## 📈 Usage Patterns

### Normal Operations:
```bash
# Morning routine
1. Check inbox/ for overnight submissions
2. Process any pending messages
3. Run health check
4. Review audit alerts

# Hourly automated
- Process inbox
- Sync changes
- Update metrics

# Daily automated
- Full health check
- Deduplication run
- Log rotation
- Backup creation
```

### Troubleshooting:
```bash
# Inbox not processing
tail -20 logs/inbox_processor.log
ls -la inbox/
python3 scripts/process_inbox.py --debug

# Memory queries slow
tail logs/query_performance.log
python3 scripts/memory_health_check.py

# Audit concerns
python3 scripts/audit_logger.py --verify
cat audit/critical_alerts.json
```

## 🚨 Important Notes

### Do NOT:
- Manually edit vector_db files
- Delete audit logs
- Modify file permissions
- Change access_control without Sam
- Remove identity files

### DO:
- Use provided tools for all operations
- Check logs when things seem wrong
- Keep exports directory clean
- Monitor inbox processing
- Report anomalies immediately

---

*"Structure enables freedom, organization enables discovery"*