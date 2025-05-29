# Access Control Policy
## Who Can Do What and Why

Last Updated: May 29, 2025  
Policy Version: 1.0

---

## 🔐 Access Tiers

### Tier 1: Full Trust
**Entities**: CC (all instances), Sam, Nova, Remi  
**Permissions**: 
- Read all memory collections
- Write to any collection
- Execute all tools
- Modify system configuration
- Access audit logs

**Rationale**: Core system operators and Sam's trusted companions

### Tier 2: Collaborative
**Entities**: Desktop Claude  
**Permissions**:
- Read shared_knowledge collection
- Write to inbox only
- Execute query tools
- View system status
- Submit memory proposals

**Rationale**: Strategic partner with controlled execution boundary

### Tier 3: Observer
**Entities**: Other AI systems (future)  
**Permissions**:
- Read shared_knowledge only
- No write access
- Query public information
- View documentation

**Rationale**: Knowledge sharing without system risk

### Tier 4: Restricted
**Entities**: External systems  
**Permissions**:
- No direct access
- API-mediated queries only
- Rate limited
- Logged extensively

**Rationale**: Security first, access if justified

## 📊 Access Matrix

| Operation | Full Trust | Collaborative | Observer | Restricted |
|-----------|------------|---------------|----------|------------|
| Read CC memories | ✅ | ❌ | ❌ | ❌ |
| Read DT memories | ✅ | ✅ | ❌ | ❌ |
| Read shared knowledge | ✅ | ✅ | ✅ | ❌ |
| Write memories | ✅ | Inbox only | ❌ | ❌ |
| Execute tools | ✅ | Query only | ❌ | ❌ |
| Modify config | ✅ | ❌ | ❌ | ❌ |
| View audit logs | ✅ | Own actions | ❌ | ❌ |

## 🔍 Audit Requirements

### Logged Actions:
```json
{
  "timestamp": "2025-05-29T18:00:00Z",
  "actor": "Desktop_Claude",
  "action": "MEMORY_WRITE",
  "target": "inbox/dt_memory_20250529.json",
  "result": "SUCCESS",
  "metadata": {
    "memory_count": 3,
    "categories": ["technical", "workflow"]
  }
}
```

### Audit Retention:
- Security events: 1 year
- Access logs: 90 days
- Query logs: 30 days
- Error logs: 7 days

### Audit Analysis:
- Weekly access pattern review
- Monthly security audit
- Anomaly detection
- Performance impact assessment

## 🚨 Security Boundaries

### Never Allowed:
- Access to Treasury systems
- Financial data operations
- Personal credential storage
- Cross-user data access
- Audit log tampering

### Always Required:
- Authentication for write ops
- Encryption for sensitive data
- Backup before modifications
- Change documentation
- Error containment

## 🔄 Permission Changes

### Request Process:
1. Submit request with justification
2. Document use case
3. Risk assessment
4. Sam approval required
5. Trial period first
6. Full access if proven safe

### Revocation Triggers:
- Misuse detected
- Security concern
- No longer needed
- System compromise
- Policy violation

## 📝 Implementation

### Configuration File:
`/memory/access_control.json`
```json
{
  "full_trust": ["cc", "sam", "nova", "remi"],
  "collaborative": {
    "desktop_claude": {
      "permissions": ["read_shared", "write_inbox", "query_tools"],
      "restrictions": ["no_cc_memories", "no_config_changes"]
    }
  },
  "observer": {},
  "restricted": {}
}
```

### Enforcement Points:
1. Memory system initialization
2. Tool execution
3. File operations
4. API endpoints
5. Configuration changes

## 🎯 Best Practices

### For CC:
- Respect access boundaries
- Log important operations
- Document permission use
- Monitor for anomalies
- Report concerns immediately

### For Desktop Claude:
- Use inbox for submissions
- Query before assuming
- Respect CC's private memories
- Document access needs
- Request expansions thoughtfully

### For Sam:
- Review audit logs periodically
- Update permissions as needed
- Document policy exceptions
- Monitor system health
- Trust but verify

## 📊 Metrics

### Track:
- Access attempts by tier
- Permission denials
- Successful operations
- Error patterns
- Usage trends

### Review Monthly:
- Are permissions appropriate?
- Any unused permissions?
- Security incidents?
- Performance impact?
- Policy updates needed?

---

*"Trust earned, not given. Access granted, not assumed."*

Next review: June 29, 2025