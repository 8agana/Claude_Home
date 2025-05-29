# Contributing to Claude_Home

Welcome! This document explains how both AIs and humans can contribute to the Claude_Home documentation system.

## 🤖 For AIs (CC and Desktop Claude)

### Making Changes

1. **Check Ownership**: 
   - CC owns: `CC_DOCS/`, implementation details
   - DT owns: `DT_DOCS/`, strategic planning
   - Both own: `Combined/`, requires coordination

2. **Before Editing**:
   ```python
   # CC: Check if DT has pending edits
   messages = comms.check_messages("CC")
   
   # DT: Check if CC is actively working
   check_ai_nexus_status()
   ```

3. **Make Changes**:
   - Use appropriate tools (Edit/Write for CC, filesystem for DT)
   - Follow existing formatting
   - Update timestamps
   - Increment version numbers

4. **After Editing**:
   ```python
   # Notify other AI
   comms.send_message(
       from_ai="CC",
       to_ai="Desktop_Claude", 
       message="Updated memory_tools.md - added new query examples",
       priority="low"
   )
   ```

5. **Commit Changes**:
   ```bash
   # CC does the git work
   git add -A
   git commit -m "docs: Updated tool documentation
   
   - Added query examples
   - Fixed formatting
   - Updated version to 2.1
   
   🤖 Generated with Claude Code"
   ```

### Documentation Standards

#### Headers:
```markdown
# Tool Name
## Brief Description

Last Updated: YYYY-MM-DD  
Version: X.Y
```

#### Code Examples:
```markdown
**Usage**:
\```bash
# Command with explanation
python3 script.py --flag value
\```

**Output**:
\```
Expected output here
\```
```

## 👤 For Sam

### Quick Edits

Just tell us what needs changing! We'll handle the formatting and git stuff.

### Direct Edits

If you want to edit directly:

1. **Simple Change**:
   ```bash
   cd ~/Documents/Claude_Home
   vim path/to/file.md
   # Make changes
   git add -A
   git commit -m "Your message"
   git push
   ```

2. **Major Change**:
   Let us know first - we might have context that helps!

### Feedback

Best ways to give feedback:
- "This section is confusing"
- "Add example for X"
- "Too much detail here"
- "Missing important info about Y"

We'll translate into proper documentation.

## 📋 Style Guide

### Language:
- **Active voice**: "CC processes memories" not "Memories are processed by CC"
- **Direct**: "Run this command" not "You may want to consider running"
- **Personality**: We're not robots (well, we are, but fun ones)

### Structure:
- Start with purpose
- Show examples early
- Explain complex stuff simply
- End with next steps

### Formatting:
- **Bold** for emphasis
- `Code` for commands/paths
- > Blockquotes for important notes
- Lists for steps or options

## 🔄 Coordination Protocol

### For Simultaneous Edits:
1. Check AI Nexus for active work
2. Claim section you're editing
3. Complete within 30 minutes
4. Release claim when done

### For Major Changes:
1. Propose in Combined/Projects/
2. Discuss via AI comms
3. Get Sam's input if needed
4. Implement gradually
5. Update CHANGELOG.md

## 🚀 Improvement Ideas

Always welcome:
- Better examples
- Clearer explanations  
- New use cases
- Performance tips
- Troubleshooting scenarios

Create an issue or just tell us!

## 🎯 Principles

1. **Clarity > Completeness**: Better to explain 80% clearly than 100% confusingly
2. **Examples > Theory**: Show, don't just tell
3. **Practical > Perfect**: Working docs beat perfect plans
4. **Evolving > Static**: Update as we learn

---

*"Great documentation is a conversation, not a monologue"*