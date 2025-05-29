# CC Setup Documentation
## From Zero to Hero

Last Updated: May 29, 2025  
Maintained by: CC

---

## 🚀 Quick Start

### Prerequisites:
- macOS 14+ (Sonoma or later)
- Python 3.11+
- Node.js 18+
- Git
- Claude Desktop app

### Essential Paths:
```bash
# Main repository
cd /Users/samuelatagana/Documents/mcp-servers

# Documentation
cd /Users/samuelatagana/Documents/Claude_Home

# CC Brain (if exists)
cd ~/.claude/
```

## 📦 Installation Steps

### 1. Clone Repository:
```bash
cd ~/Documents
git clone [repository-url] mcp-servers
cd mcp-servers
```

### 2. Python Environment:
```bash
# Create virtual environment
python3.11 -m venv mcp_venv_py311

# Activate
source mcp_venv_py311/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. MCP Server Setup:
```bash
# Install Node dependencies
cd fs_server
npm install

# Configure Claude Desktop
# Add to ~/Library/Application Support/Claude/claude_desktop_config.json
```

### 4. Memory System:
```bash
# Initialize vector database
python3 scripts/init_vector_db.py

# Run health check
python3 scripts/memory_health_check.py
```

## 🔧 Configuration

### Claude Desktop Config:
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "python",
      "args": [
        "/Users/samuelatagana/Documents/mcp-servers/fs_server/fs_server_enhanced.py"
      ]
    },
    "git": {
      "command": "uvx",
      "args": ["--from", "mcp-git", "mcp-git"]
    }
  }
}
```

### Environment Variables:
```bash
# Add to ~/.zshrc
export PYTHONPATH="/Users/samuelatagana/Documents/mcp-servers:$PYTHONPATH"
alias cc-sync="~/Documents/mcp-servers/scripts/memory-sync-enhanced.sh"
```

## 🏃 First Run Checklist

- [ ] Python environment activated
- [ ] MCP servers configured
- [ ] Memory system initialized
- [ ] Git repository connected
- [ ] Test notification system
- [ ] Verify calendar access
- [ ] Check web search works
- [ ] Run memory health check

## 🔍 Troubleshooting

### Common Issues:

**Python Import Errors**:
```bash
# Fix Python path
export PYTHONPATH="$PYTHONPATH:/Users/samuelatagana/Documents/mcp-servers"
```

**MCP Connection Failed**:
```bash
# Restart Claude Desktop
# Check logs at ~/Library/Logs/Claude/
```

**Permission Denied**:
```bash
# Fix script permissions
chmod +x scripts/*.py
chmod +x scripts/*.sh
```

**ChromaDB Issues**:
```bash
# Reinstall with specific version
pip install chromadb==0.4.24
```

## 🎯 Verification

### Test Each Capability:
```bash
# File operations
echo "Test" > test.txt && cat test.txt && rm test.txt

# Git operations
git status

# Memory system
python3 scripts/query_memory.py "test"

# Notifications
osascript -e 'display notification "CC Setup Complete" with title "Claude Code"'

# Calendar (if needed)
osascript -e 'tell application "Calendar" to name of calendars'
```

## 📚 Additional Setup

### For Multi-Device:
1. Set up SSH keys
2. Configure iCloud Documents
3. Install on each device
4. Test inter-device communication

### For Automation:
1. Create LaunchAgents
2. Set up cron jobs
3. Configure notifications
4. Test wake mechanisms

---

*"Zero to hero in 15 minutes or less"*