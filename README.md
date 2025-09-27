> 🚧 Work in progress: preparing SuperCodex v4.0.0
# SuperCodex v4.0.0 🚀
<a href="https://github.com/SuperClaude-Org/SuperClaude_Framework" target="_blank">
  <img src="https://img.shields.io/badge/Try-SuperClaude_Framework-brightgreen" alt="Try SuperClaude Framework"/>
</a>
<a href="https://github.com/SuperClaude-Org/SuperQwen_Framework" target="_blank">
  <img src="https://img.shields.io/badge/Try-SuperQwen_Framework-orange" alt="Try SuperQwen Framework"/>
</a>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://img.shields.io/pypi/v/SuperCodex.svg)](https://pypi.org/project/SuperCodex/)
[![Version](https://img.shields.io/badge/version-4.0.0-blue.svg)](https://github.com/SuperClaude-Org/SuperCodex_Framework)
[![GitHub issues](https://img.shields.io/github/issues/SuperClaude-Org/SuperCodex_Framework)](https://github.com/SuperClaude-Org/SuperCodex_Framework/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/SuperClaude-Org/SuperCodex_Framework/blob/master/CONTRIBUTING.md)
[![Contributors](https://img.shields.io/github/contributors/SuperClaude-Org/SuperCodex_Framework)](https://github.com/SuperClaude-Org/SuperCodex_Framework/graphs/contributors)


SuperCodex is a meta-programming configuration framework that enhances Codex CLI with structured development capabilities. It provides 18 Markdown-based slash prompts, 13 specialized AI agents with Persona Mode, behavioral instructions, and workflow automation for systematic software development.

## Quick Start

### Installation Methods

**Recommended: pipx (Isolated CLI Tool)**
```bash
# Install with pipx for clean, isolated environment
pipx install SuperCodex

# Setup SuperCodex for Codex CLI (Choose one)
SuperCodex install --yes                    # Express setup (recommended)
SuperCodex install --profile minimal --yes  # Fastest (core only)
SuperCodex install --profile full --yes     # All features
```

**Alternative: pip (Traditional Installation)**
```bash
# Install with pip (may cause dependency conflicts)
pip install SuperCodex

# Or in a virtual environment (recommended if using pip)
python -m venv supercodex-env
source supercodex-env/bin/activate  # Linux/Mac
# or: supercodex-env\Scripts\activate  # Windows
pip install SuperCodex
```

### Usage with Codex CLI
```bash
# Example commands after installation:
/sg:analyze src/
/sg:implement user authentication
```

**Why pipx?** SuperCodex is a standalone CLI tool. Using pipx:
- Prevents dependency conflicts with your projects
- Provides clean uninstallation
- Automatically manages virtual environments
- Keeps your system Python clean

**Note for pipx users:** If you encounter Node.js/npm detection issues during MCP setup, ensure these tools are available in your system PATH.

## What is SuperCodex? 💎

SuperCodex transforms Codex CLI into a structured development platform by providing:

- **18 Slash Prompts**: Markdown prompts for systematic workflow automation (/sg:analyze, /sg:implement, etc.)
- **Persona Mode**: 13 specialized AI agents that embody specific roles (system-architect, security-engineer, etc.)
- **Behavioral Instructions**: Core principles and rules for consistent development practices
- **Workflow Automation**: Systematic approaches to analysis, implementation, and optimization

Unlike traditional tools, SuperCodex uses **Persona Mode** where Codex CLI embodies agent roles rather than spawning separate sub-agents.

[![GitHub Sponsors](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#white)](https://github.com/sponsors/SuperClaude-Org)

## Documentation

### Getting Started
- [Quick Start Guide](Docs/Getting-Started/quick-start.md)
- [Installation Guide](Docs/Getting-Started/installation.md)

### User Guides
- [Prompts Reference](Docs/User-Guide/commands.md) - 18 Markdown-based slash prompts
- [Agents Guide](Docs/User-Guide/agents.md) - 13 specialized AI personas
- [Behavioral Modes](Docs/User-Guide/modes.md) - Context-aware operation modes
- [Flags Guide](Docs/User-Guide/flags.md) - Command flags and options
- [MCP Servers](Docs/User-Guide/mcp-servers.md) - MCP server integration guide
- [Session Management](Docs/User-Guide/session-management.md) - Session lifecycle management

### Developer Resources
- [Technical Architecture](Docs/Developer-Guide/technical-architecture.md)
- [Contributing Code](Docs/Developer-Guide/contributing-code.md)
- [Testing & Debugging](Docs/Developer-Guide/testing-debugging.md)

### Reference
- [Quick Start Practices](Docs/Reference/quick-start-practices.md)
- [Examples Cookbook](Docs/Reference/examples-cookbook.md)
- [Troubleshooting](Docs/Reference/troubleshooting.md)

## Contributing

**Current Priorities:**
- 📝 Documentation improvements and usage examples
- 🎯 Prompt workflow patterns and best practices
- 🤖 New AI agent personas for specialized domains
- 🧪 Testing and validation for Codex CLI integration
- 🌐 Translation and internationalization

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Contributors:** [View all contributors](https://github.com/SuperClaude-Org/SuperCodex_Framework/graphs/contributors)