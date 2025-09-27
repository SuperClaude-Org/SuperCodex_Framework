# SuperCodex Installation Guide 📦

> **Command Context**: This guide uses **Terminal Commands** for installation and setup. These run in your terminal/command prompt, not inside Codex CLI.

## 🎯 It's Easier Than It Looks!

SuperCodex installs in under 2 minutes with an interactive installer. The process involves installing the Python package and running the component installer to configure your Codex CLI environment.

## Quick Start 🚀

**Method 1: pipx (Recommended for CLI tools)**
```bash
# Install with pipx for isolated environment
pipx install SuperCodex
SuperCodex install
```

**Method 1b: pip (Traditional Python)**
```bash
# Install with pip (may cause dependency conflicts)
pip install SuperCodex
SuperCodex install
```

**Method 2: NPM (Cross-platform)**
```bash
npm install -g supercodex
SuperCodex install
```

**Method 3: Development**
```bash
git clone https://github.com/SuperCodex-Org/SuperCodex_Framework.git
cd SuperCodex_Framework
pip install -e ".[dev]"
SuperCodex install --dry-run
```

### 📋 Command Quick Reference

| Command Type | Where to Run | Format | Example |
|-------------|--------------|--------|----------|
| **🖥️ Installation** | Terminal/CMD | `SuperCodex [command]` | `SuperCodex install` |
| **🔧 Configuration** | Terminal/CMD | `python3 -m SuperCodex` | `python3 -m SuperCodex --version` |
| **💬 Development** | Codex CLI | `/sg:[command]` | `/sg:analyze "idea"` |
| **⚡ Workflow** | Codex CLI | `/sg:[command] --flags` | `/sg:test --coverage` |

> **Important**: Installation commands run in your terminal. Once installed, you'll use `/sg:` commands inside Codex CLI for development tasks.

---

**What Gets Installed:**
- 18 slash commands (/sg:*) for workflow automation
- 13 specialized AI agents with domain expertise
- 5 behavioral modes for different contexts
- 6 MCP server configurations for enhanced capabilities
- Core instruction files in ~/.codex directory

**Dry-run Preview:**
```bash
SuperCodex install --dry-run  # Preview changes without installing
```

## Before You Start 🔍

### What You Need 💻

**Required:**
- Python 3.8+ with pip
- Codex CLI installed and working
- 50MB free space for components

**Optional but Recommended:**
- Node.js 16+ (for MCP servers like Context7, Magic)
- Git (for version control integration)
- 1GB RAM for optimal performance

### Quick Check 🔍

Run these commands to verify your system is ready:

```bash
# Verify Python (should be 3.8+)
python3 --version

# Verify Codex CLI availability
codex --version

# Optional: Check Node.js for MCP servers
node --version

# Check available disk space
df -h ~
```

If any checks fail, see [Prerequisites Setup](#prerequisites-setup-🛠️) below.

## Installation Options 🎛️

### 🎯 Interactive Installation (Default - Recommended)

### ⚡ Component-Specific Installation

### 🔍 Other Useful Options

**Node.js Installation:**
```bash
# Linux (Ubuntu/Debian)
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# macOS
brew install node

# Windows
winget install OpenJS.NodeJS
# Or download from https://nodejs.org/
```

### Getting SuperCodex 📥

**Choose Your Preferred Method:**

**Python Users (Recommended: pipx):**
```bash
# For CLI tools - isolated environment (recommended)
pipx install SuperCodex

# Traditional installation
pip install SuperCodex
```

**JavaScript/Node.js Users:**
```bash
npm install -g supercodex
```

**Development/Contributors:**
```bash
git clone https://github.com/SuperCodex-Org/SuperCodex_Framework.git
cd SuperCodex_Framework
pip install -e ".[dev]"
```

### Running the Installer 🎬

**Interactive Installation (Default):**
```bash
SuperCodex install
```
The installer will:
1. Detect your system configuration
2. Show available components with descriptions
3. Let you select which components to install
4. Configure MCP servers if desired
5. Create backups before making changes

### Installation Profiles 📦

**Choose your installation type:**

```bash
# 🚀 Express Installation (Recommended for most users)
SuperCodex install --yes                        # Interactive setup with auto-confirm

# 🎯 Minimal Installation (Fastest - Core features only)
SuperCodex install --profile minimal --yes      

# 💼 Standard Installation (Balanced - Core + Commands + Modes)
SuperCodex install --profile standard --yes     

# 🛠️ Full Installation (Complete - All features including MCP servers)
SuperCodex install --profile full --yes         
```

### Advanced Options ⚙️

**For specific needs:**

```bash
# Preview without installing
SuperCodex install --dry-run                    

# Custom component selection
SuperCodex install --components core mcp modes  

# Custom installation directory
SuperCodex install --install-dir /custom/path   

# Speed optimizations (skip checks)
SuperCodex install --skip-validation --no-backup --yes
```

### During Installation 📱

**Installation Steps:**

1. **System Check** - Validates Python, Codex CLI, permissions
2. **Component Discovery** - Scans available components and dependencies
3. **User Selection** - Interactive menu for component choices
4. **Backup Creation** - Saves existing ~/.codex configuration
5. **File Installation** - Copies framework files with merge logic
6. **MCP Configuration** - Sets up .codex.json for selected servers
7. **Verification** - Tests installation and provides next steps

**Progress Indicators:**
- ✅ Step completion checkmarks
- 🔄 Real-time progress bars for file operations
- ⚠️ Warnings for potential issues
- 📊 Summary statistics (files installed, space used)

## After Installation ✅

### Quick Test 🧪

**Verify Installation:**
```bash
# Check SuperCodex version
SuperCodex --version

# List installed components
SuperCodex install --list-components

# Test basic functionality
echo "Test analysis" | codex
# Then try: /sg:analyze README.md

# Verify MCP servers (if installed)
ls ~/.codex/.codex.json
```

**Expected Results:**
- ✅ Version number displays correctly
- ✅ Components list shows installed items
- ✅ Slash commands available in Codex CLI
- ✅ MCP servers connect successfully

### What Got Installed 📂

**Files in ~/.codex:**
```
~/.codex/
├── CODEX.md           # Main instruction file with @imports
├── FLAGS.md            # Behavioral flags system
├── RULES.md            # Development rules
├── PRINCIPLES.md       # Engineering principles
├── MCP_*.md            # MCP server instructions
├── MODE_*.md           # Behavioral modes
├── .codex.json        # MCP server configurations
└── [your files]        # Preserved customizations
```

**Component Breakdown:**
- **Core**: Essential framework files and behavioral instructions
- **Commands**: 18 slash commands for workflow automation
- **Modes**: 5 behavioral modes for different contexts
- **Agents**: 13 specialized AI personas
- **MCP**: Configuration for 6 MCP servers
- **MCP Docs**: Documentation for MCP server usage

### First Steps 🎯

**Try These Commands:**
```bash
# Interactive requirements discovery
/sg:analyze "mobile app idea"

# Analyze existing code
/sg:analyze src/

# Generate implementation workflow
/sg:workflow "user authentication system"

# Get command help
/sg:index
```

**Learning Path:**
1. Start with `/sg:analyze` for project discovery
2. Use `/sg:analyze` to understand existing code
3. Try `/sg:implement` for feature development
4. Explore `/sg:index` for command discovery

## Managing Your Installation 🛠️

### Updates 📅

**Update SuperCodex:**
```bash
# Update core package
pip install --upgrade SuperCodex
# or: npm update -g supercodex

# Update components
SuperCodex update

# Update specific components
SuperCodex install --components mcp modes --force
```

**Version Management:**
- Updates preserve user customizations
- New components available via `SuperCodex install --list-components`
- Selective updates possible for individual components

### Backups 💾

**Automatic Backups:**
- Created before every installation/update
- Stored in ~/.codex.backup.YYYYMMDD_HHMMSS
- Include all customizations and configurations

**Manual Backup Management:**
```bash
# Create backup
SuperCodex backup --create

# List available backups
SuperCodex backup --list

# Restore from backup
SuperCodex backup --restore ~/.codex.backup.20241201_143022

# Manual backup (alternative)
cp -r ~/.codex ~/.codex.backup.manual
```

### Uninstallation 🗑️

**Complete Removal (Two-Step Process):**

SuperCodex requires a **two-step uninstall process** for complete removal:

```bash
# Step 1: Remove SuperCodex components from ~/.codex
SuperCodex uninstall

# Step 2: Remove the Python/npm package itself  
pip uninstall SuperCodex
# or: npm uninstall -g supercodex
```

> **⚠️ Why Two Steps?**  
> - **Step 1** removes framework files from your ~/.codex directory while preserving your personal files
> - **Step 2** removes the SuperCodex command-line tool itself
> - This design prevents accidental deletion of user customizations

**Interactive Options:**
```bash
# Interactive component selection
SuperCodex uninstall                    # Choose what to remove

# Complete removal (all components)
SuperCodex uninstall --complete         # Remove all SuperCodex files

# Preserve specific data
SuperCodex uninstall --keep-backups     # Keep backup files
SuperCodex uninstall --keep-logs        # Keep log files
SuperCodex uninstall --keep-settings    # Keep user settings
```

**What Gets Preserved:**
- ✅ Your custom CODEX.md content
- ✅ Personal configuration files
- ✅ Project-specific customizations  
- ✅ Created backups (unless --complete used)
- ✅ Other tools' files in ~/.codex

## Prerequisites Setup 🛠️

**Missing Python?**
```bash
# Linux (Ubuntu/Debian)
sudo apt update && sudo apt install python3 python3-pip

# macOS  
brew install python3

# Windows
# Download from https://python.org/downloads/
# Or use winget
winget install python
```

**Missing Codex CLI?**
- Visit https://codex.ai/code for installation instructions
- SuperCodex enhances Codex CLI, so you need it first

**MCP Server Requirements:**
Some MCP servers require Node.js for optimal functionality:
- Context7: Library documentation lookup
- Magic: UI component generation (requires API key)
- Sequential: Advanced reasoning
- Playwright: Browser automation
- Morphllm: Code transformations (requires API key)
- Serena: Project memory (Python-based)

Install Node.js 16+ for full MCP capabilities.

## Troubleshooting 🔧

**Common Issues:**

**Permission Denied:**
```bash
# Linux/macOS: Use --user flag
pip install --user SuperCodex

# Or fix permissions
sudo chown -R $USER ~/.codex
```

**Python Version Issues:**
```bash
# Verify Python 3.8+
python3 --version

# Use specific Python version
python3.9 -m pip install SuperCodex
```

**Codex CLI Not Found:**
- Install Codex CLI from https://codex.ai/code
- Verify with: `codex --version`
- Check PATH configuration

**Get Help:**
- GitHub Issues: https://github.com/SuperCodex-Org/SuperCodex_Framework/issues
- Include: OS, Python version, error message, steps to reproduce

## Advanced Options ⚙️

**Custom Installation Directory:**
```bash
# Install to custom location
SuperCodex install --install-dir /path/to/custom/codex

# Set environment variable
export CODEX_CONFIG_DIR=/path/to/custom/codex
SuperCodex install
```

**Development Setup:**
```bash
# Clone repository
git clone https://github.com/SuperCodex-Org/SuperCodex_Framework.git
cd SuperCodex_Framework

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install in development mode
pip install -e ".[dev]"

# Run tests
SuperCodex install --dry-run
python scripts/validate_pypi_ready.py
```

## What's Next? 🚀

**Recommended Next Steps:**

1. **Learn Commands**: Start with [Commands Guide](../User-Guide/commands.md)
2. **Try Examples**: Explore [Examples Cookbook](../Reference/examples-cookbook.md)
3. **Configure MCP**: Set up [MCP Servers](../User-Guide/mcp-servers.md)
4. **Understand Modes**: Read [Behavioral Modes](../User-Guide/modes.md)
5. **Join Community**: Follow development on [GitHub](https://github.com/SuperCodex-Org/SuperCodex_Framework)

**Essential Guides:**
- 🚀 [Quick Start Guide](quick-start.md) - 5-minute setup
- 🔧 [Commands Reference](../User-Guide/commands.md) - All 18 commands
- 🧐 [Best Practices](../Reference/quick-start-practices.md) - Optimization tips
- 🎆 [Troubleshooting](../Reference/troubleshooting.md) - Problem solving

---

## Final Notes 📝

**Installation Summary:**
- **Time**: 2-5 minutes typical installation
- **Space**: 50MB for full installation
- **Requirements**: Python 3.8+, Codex CLI, 1GB RAM recommended
- **Platform**: Linux, macOS, Windows supported
- **Usage**: Immediate access to 21 commands and 6 behavioral modes

**What's Next**: Your Codex CLI now has enhanced capabilities. Try `/sg:analyze` for your first SuperCodex experience!

---

## Related Guides

**Documentation Roadmap:**

**Beginner** (🌱 Start Here)
- [Quick Start Guide](quick-start.md) - 5-minute setup
- [Commands Reference](../User-Guide/commands.md) - Basic usage

**Intermediate** (🌿 Growing)
- [Behavioral Modes](../User-Guide/modes.md) - Context optimization
- [MCP Servers](../User-Guide/mcp-servers.md) - Enhanced capabilities
- [Examples Cookbook](../Reference/examples-cookbook.md) - Practical patterns

**Advanced** (🌲 Expert)
- [Technical Architecture](../Developer-Guide/technical-architecture.md) - System design
- [Contributing Code](../Developer-Guide/contributing-code.md) - Development
- [Best Practices](../Reference/quick-start-practices.md) - Optimization strategies