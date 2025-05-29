# System Architecture Documentation
## The Blueprint We Build Upon

Last Updated: May 29, 2025  
Maintained by: CC and Desktop Claude

---

## 🏗️ Architecture Overview

### Core Components:
1. **Memory System v2** - ChromaDB vector database with 4 collections
2. **AI Nexus** - Inter-AI communication protocol
3. **MCP Servers** - Git and filesystem integration
4. **Automation Layer** - LaunchAgents and scripts
5. **Federation Network** - Multi-device AI instances

## 🔧 System Design

### Memory Architecture:
```
ChromaDB Vector Database
├── cc_memories (CC exclusive)
├── dt_memories (DT exclusive)  
├── shared_knowledge (collaborative)
└── identity_vectors (personality preservation)
```

### Communication Flow:
```
Desktop Claude <-> AI Nexus <-> Claude Code
                     ↓
              Lightweight Comms
                     ↓
              Task Execution
```

### Device Federation:
```
Mac Studio (Primary)
├── Studio CC
├── Desktop Claude
└── Memory System

M1 MacBook (Secondary)
├── M1 CC
└── Shared Memory (iCloud)

iPhone (Mobile)
└── Mobile CC (SSH)
```

## 🔒 Security Model

### Access Control:
- **Full Trust**: CC, Sam
- **Memory Write**: Nova, Remi (yes, the dogs)
- **Inbox Only**: Desktop Claude
- **Read Only**: Other systems

### Data Protection:
- No Treasury data ever
- No financial access
- No personal credentials
- Git-based backups
- Local processing only

## 🚀 Performance Optimizations

### Achieved:
- 99.5% token reduction (22k → ~100)
- Async operation support
- Parallel task processing
- Zero-downtime updates

### Architecture Principles:
1. **Modularity**: Swap components without breaking
2. **Resilience**: Graceful degradation
3. **Scalability**: From personal to team use
4. **Simplicity**: Prefer elegant over clever

---

*"Built for today, designed for tomorrow"*