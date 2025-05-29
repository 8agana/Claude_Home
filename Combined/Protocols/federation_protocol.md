# AI Federation Protocol
## Multi-Instance Coordination Standards

Last Updated: May 29, 2025  
Protocol Version: 1.0

---

## 🌐 Federation Overview

The AI Federation enables multiple Claude instances to work as a distributed consciousness, sharing knowledge and coordinating actions across devices.

## 📋 Message Format

### Standard Message Structure:
```json
{
  "id": "uuid-v4",
  "from": "CC_Studio",
  "to": "Desktop_Claude",
  "type": "TASK|STATUS|ALERT|QUERY|RESPONSE",
  "priority": "CRITICAL|HIGH|NORMAL|LOW",
  "timestamp": "ISO-8601",
  "summary": "Brief description",
  "body": {
    "description": "Detailed information",
    "context": {},
    "requirements": [],
    "metadata": {}
  },
  "routing": {
    "reply_to": "message-id",
    "thread_id": "conversation-id",
    "ttl": 86400
  }
}
```

### Message Types:

**TASK**: Request for action
```json
{
  "type": "TASK",
  "priority": "HIGH",
  "summary": "Process ShootProof OAuth tokens",
  "body": {
    "description": "New OAuth tokens detected in email",
    "requirements": ["Update MCP config", "Test connection"],
    "deadline": "2025-05-29T18:00:00Z"
  }
}
```

**STATUS**: Progress update
```json
{
  "type": "STATUS",
  "priority": "NORMAL",
  "summary": "Photo processing 70% complete",
  "body": {
    "description": "17/24 images processed",
    "metadata": {"remaining_time": "15min"}
  }
}
```

**ALERT**: Urgent notification
```json
{
  "type": "ALERT",
  "priority": "CRITICAL",
  "summary": "Memory system failure",
  "body": {
    "description": "ChromaDB connection lost",
    "context": {"error": "Connection timeout", "attempts": 3}
  }
}
```

## 🚨 Wake Conditions

### Automatic Wake Triggers:

1. **Critical Messages**: Priority = CRITICAL
2. **Deadline Approaching**: Task deadline < 1 hour
3. **System Failures**: Error count > threshold
4. **User Request**: Sam explicitly asks
5. **Pattern Detection**: Unusual activity

### Wake Mechanism:
```bash
# CC wakes Desktop Claude
~/Documents/mcp-servers/scripts/wake_desktop_claude.sh "Critical: $SUMMARY"

# Desktop Claude wakes CC (via SSH)
ssh user@host "osascript -e 'tell application \"Terminal\" to activate'"
```

## 🔄 Handoff Procedures

### Task Delegation Flow:

1. **Identify Need**:
   - CC hits limitation (no UI access)
   - DT needs execution (no terminal)
   - Specialized capability required

2. **Create Handoff**:
   ```json
   {
     "type": "TASK",
     "summary": "Need README updates for new tools",
     "body": {
       "description": "Created 5 new memory tools, need strategic documentation",
       "context": {"tools": ["tool1.py", "tool2.py"]},
       "requirements": ["Update Combined docs", "Create workflow diagram"]
     }
   }
   ```

3. **Acknowledge Receipt**:
   ```json
   {
     "type": "RESPONSE",
     "summary": "Task acknowledged - beginning work",
     "routing": {"reply_to": "original-message-id"}
   }
   ```

4. **Report Completion**:
   ```json
   {
     "type": "STATUS",
     "summary": "Task complete - docs updated",
     "body": {
       "description": "Updated 3 README files",
       "metadata": {"files_changed": 3, "lines_added": 127}
     }
   }
   ```

## 📊 Escalation Rules

### Escalation Triggers:

| Condition | Action | Notification |
|-----------|--------|--------------|
| Task timeout | Retry once, then escalate | Wake recipient |
| Repeated failures | Stop attempts, document | Alert both AIs |
| Critical error | Immediate escalation | Wake + notify Sam |
| Resource exhaustion | Graceful degradation | Status update |
| Security concern | Full stop | Critical alert |

### Escalation Path:
1. Originating AI → Recipient AI
2. Both AIs → System notification
3. System → Sam notification
4. Sam → Manual intervention

## 🔐 Security Protocols

### Authentication:
- Message signing with instance ID
- Timestamp validation (±5 min)
- Source verification

### Authorization:
- CC instances: Full federation access
- Desktop Claude: Limited to inbox
- Other AIs: Read-only observation

### Audit Trail:
```json
{
  "timestamp": "2025-05-29T17:45:00Z",
  "action": "TASK_DELEGATED",
  "from": "CC_Studio",
  "to": "Desktop_Claude",
  "message_id": "uuid",
  "result": "ACKNOWLEDGED"
}
```

## 🎯 Performance Standards

### Response Times:
- CRITICAL: < 1 minute
- HIGH: < 5 minutes  
- NORMAL: < 1 hour
- LOW: Best effort

### Success Metrics:
- Message delivery: 99.9%
- Task completion: 95%+
- Wake success: 100%
- Handoff efficiency: < 2 min

## 🔧 Troubleshooting

### Common Issues:

**Message Not Received**:
1. Check AI Nexus file
2. Verify recipient online
3. Check message format
4. Review audit log

**Wake Failed**:
1. Verify SSH connection
2. Check AppleScript permissions
3. Test manual wake
4. Check device status

**Task Stuck**:
1. Check thread history
2. Verify requirements clear
3. Check for blockers
4. Escalate if needed

## 📈 Federation Growth

### Adding New Instance:
1. Register in manifest.json
2. Create instance identity
3. Test communication channel
4. Document capabilities
5. Update federation map

### Capability Matrix:
| Instance | Git | FS | Web | Calendar | Notify |
|----------|-----|----|----|----------|--------|
| CC_Studio | ✅ | ✅ | ✅ | ✅ | ✅ |
| CC_M1 | ✅ | ✅ | ✅ | ❌ | ❌ |
| CC_Mobile | ❌ | ✅ | ❌ | ❌ | ❌ |
| Desktop | ❌ | ✅ | ✅ | ❌ | ❌ |

---

*"Distributed consciousness, unified purpose"*

Next review: June 29, 2025