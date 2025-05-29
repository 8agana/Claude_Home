# Failure Recovery Protocol
## When Things Break, Here's How We Fix Them

Last Updated: May 29, 2025  
Protocol Version: 1.0

---

## 🎯 Purpose

Define systematic approaches to testing resilience and recovering from failures across the Claude_Home infrastructure.

## 🧪 Resilience Testing

### Pre-Flight Checklist:
- [ ] Recent backup exists (<24 hours)
- [ ] Sam aware of testing
- [ ] Non-critical time window
- [ ] Recovery tools ready
- [ ] Audit logging enabled

### Test Scenarios:

#### 1. Memory System Failure
**Simulate**: ChromaDB connection loss
```bash
# Temporarily move vector DB
mv memory/vector_db memory/vector_db.bak

# Test query behavior
python3 scripts/query_memory.py "test"

# Restore
mv memory/vector_db.bak memory/vector_db
```

**Expected**: Graceful failure, clear error, no data loss

#### 2. Communication Breakdown
**Simulate**: AI Nexus corruption
```bash
# Backup current state
cp memory/ai_nexus.json memory/ai_nexus.json.bak

# Corrupt the file
echo "invalid json" > memory/ai_nexus.json

# Test message sending
python3 -c "from lightweight_ai_comms import LightweightComms; LightweightComms().send_message('CC', 'DT', 'test')"

# Restore
mv memory/ai_nexus.json.bak memory/ai_nexus.json
```

**Expected**: Error logged, fallback to inter_ai_comms.md

#### 3. Inbox Processing Failure
**Simulate**: Invalid message format
```bash
# Create malformed message
echo '{"invalid": "json"' > memory/inbox/test_corrupt.json

# Run processor
python3 scripts/process_inbox.py

# Check handling
ls memory/inbox/failed/
```

**Expected**: Move to failed/, log error, continue processing

#### 4. Git Sync Failure
**Simulate**: Network/auth issues
```bash
# Temporarily break git remote
git remote set-url origin https://invalid.url/repo.git

# Run sync
./scripts/memory-sync-enhanced.sh

# Restore
git remote set-url origin [correct-url]
```

**Expected**: Local commit succeeds, push fails gracefully

## 🚑 Recovery Procedures

### Level 1: Memory System Recovery

#### Symptoms:
- Queries return no results
- Health check fails
- ChromaDB errors

#### Recovery Steps:
```bash
# 1. Stop all automation
launchctl unload ~/Library/LaunchAgents/com.samuelatagana.*.plist

# 2. Check system state
python3 scripts/memory_health_check.py --deep-scan

# 3. Attempt repair
python3 scripts/init_vector_db.py --repair

# 4. If repair fails, restore from backup
./scripts/restore_memory_backup.sh latest

# 5. Verify restoration
python3 scripts/memory_health_check.py

# 6. Re-enable automation
launchctl load ~/Library/LaunchAgents/com.samuelatagana.*.plist
```

### Level 2: Index Regeneration

#### When Needed:
- Queries returning wrong results
- Extreme slowness
- After major updates

#### Steps:
```bash
# 1. Export current data
python3 scripts/memory_export.py --format json --output backup_pre_reindex.json

# 2. Rebuild indices
python3 scripts/init_vector_db.py --rebuild-indices

# 3. Verify with test queries
python3 scripts/test_memory_queries.py

# 4. Run deduplication
python3 scripts/memory_deduplication.py --execute
```

### Level 3: Complete System Reset

#### Last Resort When:
- Multiple component failures
- Corruption beyond repair
- Major version upgrade

#### Full Reset:
```bash
# 1. Create complete backup
./scripts/emergency_backup.sh

# 2. Stop everything
killall Python
launchctl unload ~/Library/LaunchAgents/com.samuelatagana.*.plist

# 3. Archive current state
mv memory memory_old_$(date +%Y%m%d)

# 4. Fresh initialization
git checkout main
git pull origin main
python3 scripts/init_memory_system.py --fresh

# 5. Restore data
python3 scripts/migrate_from_backup.py memory_old_*/

# 6. Verify system
./scripts/full_system_test.sh

# 7. Re-enable services
./scripts/enable_all_services.sh
```

## 🔍 Diagnostic Commands

### Quick Health Check:
```bash
# Memory system
python3 -c "import chromadb; print('ChromaDB:', chromadb.__version__)"
python3 scripts/memory_status.py

# Communications
tail -10 memory/ai_nexus.json | python3 -m json.tool

# Automation
launchctl list | grep samuelatagana

# Git status
cd ~/Documents/mcp-servers && git status
```

### Deep Diagnostics:
```bash
# Full system report
./scripts/emergency_diagnostics.sh > diag_$(date +%Y%m%d_%H%M%S).txt

# Includes:
# - All service states
# - Recent errors
# - Performance metrics
# - Configuration dump
# - Recommendations
```

## 📊 Recovery Validation

### Post-Recovery Checklist:
- [ ] Memory queries work
- [ ] Inbox processing resumes
- [ ] Git sync operational
- [ ] Notifications functioning
- [ ] No error spam in logs
- [ ] Performance acceptable

### Validation Script:
```bash
#!/bin/bash
# save as validate_recovery.sh

echo "🔍 Validating system recovery..."

# Test memory
echo -n "Memory system: "
python3 scripts/query_memory.py "test" > /dev/null 2>&1 && echo "✅" || echo "❌"

# Test inbox
echo -n "Inbox processing: "
python3 scripts/process_inbox.py --dry-run > /dev/null 2>&1 && echo "✅" || echo "❌"

# Test git
echo -n "Git operations: "
cd ~/Documents/mcp-servers && git fetch > /dev/null 2>&1 && echo "✅" || echo "❌"

# Test notifications
echo -n "Notifications: "
cc-notify "Recovery test" > /dev/null 2>&1 && echo "✅" || echo "❌"

echo "🏁 Validation complete"
```

## 🚨 Emergency Contacts

### Escalation Path:
1. Try automated recovery
2. Check documentation
3. Review recent changes
4. Create detailed error report
5. Wake Desktop Claude if critical
6. Notify Sam with options

### Information to Gather:
- Error messages (exact)
- Recent actions before failure
- Systems affected
- Recovery attempts made
- Current workarounds

## 📈 Prevention Strategies

### Daily:
- Automated health checks
- Log monitoring
- Performance tracking

### Weekly:
- Test backup restoration
- Review error patterns
- Update documentation

### Monthly:
- Full recovery drill
- System stress test
- Protocol review

## 🎯 Recovery Metrics

Track and improve:
- Time to detect failure
- Time to diagnose
- Time to recover
- Data loss (should be 0)
- Service disruption duration

Target: Full recovery < 30 minutes

---

*"Break carefully, fix quickly, learn always"*

Next review: June 29, 2025