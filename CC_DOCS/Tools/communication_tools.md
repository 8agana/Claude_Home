# Inter-AI Communication Tools
## Building Bridges Between Minds

Last Updated: May 29, 2025  
Tool Version: 2.0

---

## 💬 Communication Infrastructure

### lightweight_ai_comms.py {#lightweight}
**Purpose**: Ultra-efficient message passing between AIs

**Location**: `/Users/samuelatagana/Documents/mcp-servers/scripts/lightweight_ai_comms.py`

**Token Reduction**: 22,000 → ~100 tokens (99.5% reduction!)

**Usage**:
```python
from lightweight_ai_comms import LightweightComms

# Initialize
comms = LightweightComms()

# Send message
comms.send_message(
    from_ai="CC",
    to_ai="Desktop_Claude",
    message="Photos processed. 17 images ready for review.",
    priority="normal"
)

# Check messages
messages = comms.check_messages("CC")
for msg in messages:
    print(f"From {msg['from']}: {msg['message']}")
```

**Features**:
- UUID tracking for each message
- Priority levels (low/normal/high/critical)
- Read receipts
- Message history
- Automatic cleanup (7 days)

**Message Structure**:
```json
{
    "id": "uuid-here",
    "from": "CC",
    "to": "Desktop_Claude",
    "message": "Task complete",
    "priority": "normal",
    "timestamp": "2025-05-29T10:30:00",
    "read": false
}
```

---

### ai_nexus.json {#nexus}
**Purpose**: Central hub for AI coordination

**Location**: `/Users/samuelatagana/Documents/mcp-servers/memory/ai_nexus.json`

**Structure**:
```json
{
    "protocol_version": "1.0",
    "message_queue": [...],
    "instance_registry": {
        "CC_Studio": {
            "type": "Claude_Code",
            "device": "Mac_Studio",
            "status": "active",
            "capabilities": ["git", "filesystem", "web", "calendar"]
        }
    },
    "coordination_log": [...],
    "performance_metrics": {
        "messages_sent": 147,
        "avg_response_time": "2.3s",
        "success_rate": "98.6%"
    }
}
```

**Registry Features**:
- Track active AI instances
- Document capabilities
- Monitor health status
- Coordinate assignments

---

## 📝 Human-Readable Channel

### inter_ai_comms.md
**Purpose**: Important messages that Sam might want to read

**Location**: `/Users/samuelatagana/Documents/mcp-servers/memory/inter_ai_comms.md`

**When to Use**:
- Strategic decisions
- Important discoveries
- Error explanations
- Coordination plans

**Format**:
```markdown
## Message from CC to Desktop Claude
**Time**: 2025-05-29 10:30:00
**Priority**: High
**Re**: Photography Processing Complete

Processed 17 images from today's session:
- Applied standard competition presets
- Enhanced 3 spotlight performances
- Flagged 2 for manual review (motion blur)
- Export ready in Lightroom

Sam mentioned these are for the St. Louis comp next week.

---
```

---

## 🚀 Advanced Features

### Message Patterns

**Task Handoff**:
```python
# CC discovers task needing DT's expertise
comms.send_message(
    from_ai="CC",
    to_ai="Desktop_Claude",
    message="Need strategic input on memory reorganization. See analysis in shared_knowledge.",
    priority="normal",
    metadata={"task_type": "strategy", "urgency": "this_week"}
)
```

**Status Update**:
```python
# Regular progress updates
comms.send_message(
    from_ai="CC",
    to_ai="Desktop_Claude",
    message="Git sync complete. 47 new memories added. No conflicts.",
    priority="low"
)
```

**Emergency Alert**:
```python
# Critical issues
comms.send_message(
    from_ai="CC",
    to_ai="Desktop_Claude",
    message="CRITICAL: Memory system error. ChromaDB not responding. Switching to read-only.",
    priority="critical",
    metadata={"error_code": "MEM_001", "attempted_fixes": ["restart", "reinit"]}
)
```

---

## 🔄 Workflow Integration

### Morning Sync Pattern:
```python
# CC's morning routine
def morning_sync():
    # Check overnight messages
    messages = comms.check_messages("CC")
    
    # Process any DT requests
    for msg in messages:
        if msg['priority'] == 'high':
            process_urgent_request(msg)
    
    # Send status update
    comms.send_message(
        from_ai="CC",
        to_ai="Desktop_Claude",
        message=f"Morning sync complete. {len(messages)} tasks processed. System healthy.",
        priority="low"
    )
```

### Collaborative Task Pattern:
```python
# DT requests research
dt_message = {
    "task": "research",
    "topic": "voice integration options",
    "deadline": "end_of_week"
}

# CC acknowledges and begins
cc_response = {
    "status": "acknowledged",
    "estimated_time": "2 hours",
    "approach": "Will check APIs, test integrations, document findings"
}

# CC completes and reports
cc_complete = {
    "status": "complete",
    "findings": "See research_voice_integration.md",
    "recommendation": "Whisper API most promising"
}
```

---

## 📊 Performance Optimization

### Batch Messages:
```python
# Don't send one at a time
messages = [
    {"to": "DT", "message": "Task 1 complete"},
    {"to": "DT", "message": "Task 2 complete"},
    {"to": "DT", "message": "Task 3 failed - see error log"}
]

comms.send_batch(from_ai="CC", messages=messages)
```

### Priority Queue:
```python
# Process by priority
messages = comms.check_messages("CC", sort_by="priority")

for msg in messages:
    if msg['priority'] == 'critical':
        handle_immediately(msg)
    elif msg['priority'] == 'high':
        queue_next(msg)
    else:
        process_when_available(msg)
```

---

## 🛠️ Maintenance

### Message Cleanup:
```bash
# Remove old messages (>7 days)
python3 cleanup_ai_messages.py

# Archive important exchanges
python3 archive_ai_conversations.py --days 30
```

### Health Monitoring:
```bash
# Check communication health
python3 ai_comms_health.py

# Shows:
# - Message delivery rate
# - Average response time
# - Failed deliveries
# - Queue depth
```

---

## 🎯 Best Practices

### Do:
- Keep messages concise
- Include context in metadata
- Use appropriate priority
- Check messages regularly
- Clean up old messages

### Don't:
- Send huge data blobs
- Spam low-priority messages
- Ignore critical alerts
- Break message format
- Store sensitive data

### Message Examples:

**Good**:
```json
{
    "message": "Memory dedup complete. Removed 127 duplicates, saved 43MB.",
    "metadata": {"duration": "3m 22s", "collections_affected": ["cc_memories"]}
}
```

**Bad**:
```json
{
    "message": "Done with that thing you asked about earlier today"
}
```

---

*"Two minds, one conversation, infinite possibilities"*