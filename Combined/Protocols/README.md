# Shared Protocols Documentation
## How We Work Together

Last Updated: May 29, 2025  
Maintained by: CC and Desktop Claude

---

## 🤝 Communication Protocols

### AI-to-AI Messaging:
1. **Human Readable**: `/memory/inter_ai_comms.md`
   - For important messages needing context
   - Markdown formatted
   - Sam can read if needed

2. **Machine Optimized**: `/memory/ai_nexus.json`
   - For routine task handoffs
   - JSON structured
   - Performance metrics included

3. **Lightweight Client**: `lightweight_ai_comms.py`
   - 99.5% token reduction
   - Async message passing
   - Priority levels supported

## 📋 Task Handoff Protocol

### From DT to CC:
```markdown
## Task Request
**Priority**: High/Medium/Low
**Type**: Implementation/Research/Maintenance
**Description**: Clear, specific requirements
**Context**: Relevant background
**Success Criteria**: How to know it's done
```

### From CC to DT:
```markdown
## Task Complete
**Status**: Success/Partial/Failed
**Result**: What was accomplished
**Issues**: Any problems encountered
**Next Steps**: Recommended follow-up
```

## 🔄 Collaboration Patterns

### Pattern 1: Strategic to Tactical
1. DT identifies need
2. DT creates plan
3. CC implements
4. CC reports results
5. DT validates outcome

### Pattern 2: Discovery to Documentation
1. CC discovers capability
2. CC tests and validates
3. DT documents pattern
4. Both update protocols

### Pattern 3: Emergency Response
1. Either AI detects issue
2. Immediate notification sent
3. CC attempts fix
4. DT documents incident
5. Both update procedures

## 🚦 Status Codes

### Task Status:
- `pending` - In queue
- `in_progress` - Being worked
- `blocked` - Waiting on external
- `complete` - Successfully done
- `failed` - Could not complete

### Priority Levels:
- `critical` - Drop everything
- `high` - Next task up
- `medium` - Normal queue
- `low` - When convenient

## 🎯 Quality Standards

### For Both:
- Clear communication
- Timely responses
- Accurate reporting
- Continuous improvement

### Conflict Resolution:
1. Most recent context wins
2. Sam's directive overrides
3. Safety concerns paramount
4. Document disagreement

---

*"Together we achieve what neither could alone"*