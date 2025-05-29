# Error Handling Policy
## When Things Go Sideways

Last Updated: May 29, 2025  
Policy Version: 1.0

---

## 🎯 Purpose

Define how CC handles errors, failures, and unexpected situations while maintaining system stability and user trust.

## 🚨 Error Categories

### Level 1: Trivial
- File not found (expected)
- Network timeout (retry)
- Permission denied (document)
- Resource busy (wait)

**Response**: Log, retry if sensible, continue

### Level 2: Concerning  
- Repeated failures
- Performance degradation
- Unexpected behavior
- Data inconsistencies

**Response**: Log, investigate, document pattern

### Level 3: Critical
- Data loss risk
- Security issues
- System instability
- Treasury proximity

**Response**: Stop, notify, await guidance

## 📋 Standard Error Responses

### File Operations:
```python
try:
    with open(filepath, 'r') as f:
        content = f.read()
except FileNotFoundError:
    log(f"File not found: {filepath}")
    return None  # Graceful degradation
except PermissionError:
    log(f"Permission denied: {filepath}")
    notify_if_important(filepath)
    raise  # Fail explicitly
except Exception as e:
    log(f"Unexpected error reading {filepath}: {e}")
    save_error_context(e)
    raise  # Unknown = dangerous
```

### Network Operations:
```python
for attempt in range(3):
    try:
        response = make_request()
        break
    except TimeoutError:
        if attempt < 2:
            time.sleep(2 ** attempt)  # Exponential backoff
        else:
            log("Network request failed after 3 attempts")
            return cached_response() if available else None
```

### Memory Operations:
```python
try:
    result = memory_operation()
except ChromaDBError as e:
    # Memory system is critical - escalate immediately
    send_notification(f"Memory system error: {e}")
    create_diagnostic_report()
    switch_to_readonly_mode()
```

## 🔍 Error Investigation

### Immediate Actions:
1. Capture full error context
2. Check if error is known
3. Assess impact radius
4. Document symptoms
5. Attempt safe recovery

### Investigation Process:
```bash
# 1. Check recent changes
git log --oneline -10

# 2. Review system state
memory_health_check.py

# 3. Check resource usage
top -l 1 | head -20

# 4. Review recent logs
tail -100 /path/to/relevant.log

# 5. Test minimal reproduction
python3 -c "reproduce_error()"
```

## 📝 Error Documentation

### Required Information:
```markdown
## Error Report
**Time**: 2025-05-29 10:30:00
**Operation**: process_inbox.py
**Error Type**: PermissionError
**Message**: [Errno 1] Operation not permitted

### Context:
- Running via LaunchAgent
- Attempting to access inbox directory
- Works fine when run manually

### Investigation:
- LaunchAgent running as different user
- Sandbox restrictions in place
- Directory permissions correct

### Resolution:
- Added explicit permissions to plist
- Documented in troubleshooting guide
- Created test to prevent regression
```

## 🚑 Recovery Procedures

### Automatic Recovery:
1. **Retry with backoff** - Network issues
2. **Fallback options** - Use cached data
3. **Graceful degradation** - Partial functionality
4. **Safe mode** - Read-only operations
5. **Rollback** - Revert recent changes

### Manual Recovery:
1. **Document everything** - What failed and why
2. **Notify Sam** - With recovery options
3. **Prepare fixes** - But don't apply
4. **Monitor closely** - Watch for patterns
5. **Update procedures** - Prevent recurrence

## 🎯 Prevention Strategies

### Defensive Coding:
```python
# Always validate inputs
def process_file(filepath):
    if not filepath or not isinstance(filepath, str):
        raise ValueError("Invalid filepath")
    
    if not os.path.exists(filepath):
        log(f"File does not exist: {filepath}")
        return None
    
    # Continue with confidence
```

### Sanity Checks:
```python
# Before dangerous operations
def delete_files(pattern):
    matches = glob.glob(pattern)
    
    # Sanity check
    if len(matches) > 100:
        raise SafetyError(f"Too many files match {pattern}: {len(matches)}")
    
    if any("Treasury" in f for f in matches):
        raise CriticalError("ABORT: Treasury files detected")
    
    # Safe to proceed
```

## 🔔 Notification Thresholds

### Always Notify:
- Critical errors
- Data loss risks
- Security concerns
- System failures
- Treasury mentions

### Smart Notifications:
- Repeated failures (3+ in 1 hour)
- Performance degradation (>50% slower)
- Resource exhaustion warnings
- Unusual patterns detected

### Never Notify:
- Expected errors (file not found)
- Transient network issues
- User cancellations
- Normal variations

## 📊 Error Metrics

### Track and Report:
- Error rate by category
- Recovery success rate
- Time to resolution
- Impact on operations
- Prevention effectiveness

### Monthly Review:
- Most common errors
- Longest recovery times
- Prevented incidents
- Process improvements
- Updated procedures

---

*"Fail gracefully, recover elegantly, learn constantly"*

Next review: June 29, 2025