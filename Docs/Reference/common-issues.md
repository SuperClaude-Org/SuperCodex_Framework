# Common Issues - Quick Reference

> **Quick Fix Guide**: The 10 most common SuperCodex issues with rapid solutions. Each issue is designed to be resolved in under 2 minutes.

**For Detailed Help**: If these quick fixes don't work, see the [Comprehensive Troubleshooting Guide](troubleshooting.md) for detailed solutions.

> **Command Context**: **🖥️ Terminal Commands** (for installation) vs **💬 Codex CLI Commands** (`/sg:` for development)

## Top 10 Quick Fixes

### 1. 🖥️ Permission Denied During Installation
**Error**: `ERROR: Permission denied: '/home/user/.codex/CODEX.md'`

**Quick Fix**:
```bash
sudo chown -R $USER ~/.codex && chmod 755 ~/.codex
```

**Alternative**: Use user installation: `pip install --user SuperCodex`

[Detailed Help →](troubleshooting.md#common-installation-problems)

---

### 2. 🖥️ Python Version Too Old  
**Error**: `ERROR: SuperCodex requires Python 3.8+`

**Quick Fix**:
```bash
python3 --version  # Check current version
# If < 3.8, install newer Python:
sudo apt install python3.9 python3.9-pip  # Linux
python3.9 -m pip install SuperCodex
```

[Detailed Help →](troubleshooting.md#python-version-compatibility)

---

### 3. 🖥️ Component Installation Failed
**Error**: `ERROR: Component 'mcp' installation failed`

**Quick Fix**:
```bash
python3 -m SuperCodex install --components core
python3 -m SuperCodex install --components mcp --force
```

[Detailed Help →](troubleshooting.md#component-installation-failures)

---

### 4. 💬 Commands Not Working in Codex CLI
**Error**: `/sg:help` command not recognized

**Quick Fix**:
1. Restart Codex CLI completely
2. Verify installation: `cat ~/.codex/CODEX.md | head -5`
3. If empty, reinstall: `python3 -m SuperCodex install --force`

[Detailed Help →](troubleshooting.md#command-execution-problems)

---

### 5. 🖥️ "SuperCodex" Command Not Found
**Error**: `command not found: SuperCodex`

**Quick Fix**:
```bash
# Try lowercase:
superclaude --version
# Or use module form:
python3 -m SuperCodex --version
```

[Detailed Help →](troubleshooting.md#command-not-found)

---

### 6. 🖥️ Windows Path Problems
**Error**: `Cannot find file 'C:\Users\name\.codex\CODEX.md'`

**Quick Fix**:
```cmd
set CLAUDE_CONFIG_DIR=C:\Users\%USERNAME%\.codex
python -m SuperCodex install --install-dir "%CLAUDE_CONFIG_DIR%"
```

[Detailed Help →](troubleshooting.md#windows-platform-issues)

---

### 7. 💬 Commands Hang or Timeout
**Error**: Commands start but never complete

**Quick Fix**:
1. Press Ctrl+C to cancel
2. Try smaller scope: `/sg:analyze src/` instead of entire project
3. Restart Codex CLI session

[Detailed Help →](troubleshooting.md#command-timeout-or-hanging)

---

### 8. 🖥️ Node.js Missing for MCP Servers
**Error**: `Node.js not found` during MCP installation

**Quick Fix**:
```bash
# Linux/macOS:
curl -fsSL https://nodejs.org/dist/v18.17.0/node-v18.17.0-linux-x64.tar.xz | tar -xJ
# Windows:
winget install OpenJS.NodeJS
```

[Detailed Help →](troubleshooting.md#mcp-server-connection-problems)

---

### 9. 💬 Memory/Resource Errors
**Error**: Insufficient memory or resources

**Quick Fix**:
```bash
# Clear temporary data:
rm -rf ~/.codex/tmp/ ~/.codex/cache/
# Work with smaller projects
# Close other applications
```

[Detailed Help →](troubleshooting.md#performance-problems-and-optimization)

---

### 10. 🖥️ Fresh Installation Needed
**Error**: Multiple issues, corrupted installation

**Quick Fix**:
```bash
rm -rf ~/.codex/
pip uninstall SuperCodex
pip install SuperCodex
python3 -m SuperCodex install --fresh
```

[Detailed Help →](troubleshooting.md#reset-and-recovery-procedures)

---

## Emergency Recovery

**Complete Reset** (when everything is broken):
```bash
rm -rf ~/.codex/ && pip uninstall SuperCodex && pip install SuperCodex && python3 -m SuperCodex install --fresh
```

**Test Installation**:
```bash
python3 -m SuperCodex --version && echo "✅ Installation OK"
```

**Test Codex CLI Integration**:
Type `/sg:help` in Codex CLI - should show available commands.

---

## Need More Help?

- **🔍 Detailed Solutions**: [Comprehensive Troubleshooting Guide](troubleshooting.md)
- **📖 Setup Help**: [Installation Guide](../Getting-Started/installation.md)  
- **🆘 Report Issues**: [GitHub Issues](https://github.com/SuperCodex-Org/SuperCodex_Framework/issues)
- **📧 Emergency Contact**: anton.knoery@gmail.com