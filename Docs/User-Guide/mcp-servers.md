# SuperCodex MCP Servers Guide 🔌

## ✅ Verification Status
- **SuperCodex Version**: v4.0+ Compatible
- **Last Tested**: 2025-01-16
- **Test Environment**: Linux/Windows/macOS
- **MCP Servers**: ✅ All Verified (6 servers tested)

## 🧪 Testing MCP Server Connection

Before using this guide, verify MCP servers are working:

```bash
# Test server connectivity
SuperCodex status --mcp
# Expected: Shows connected servers (context7, sequential, magic, playwright, serena, morphllm)

# Test Context7 server
/sg:explain "React useEffect"
# Expected: Should fetch official React documentation

# Test Sequential server  
/sg:analyze complex-problem/ --think
# Expected: Should show structured reasoning steps
```

**If tests fail**: Check [Installation Guide](../Getting-Started/installation.md) for MCP setup

## 🚀 MCP in 5 Minutes - Quick Success Path

**What are MCP Servers?** Specialized tools that extend Codex CLI's capabilities automatically. No manual configuration needed - just start coding.

**Instant Validation:**
```bash
# 1. Verify MCP servers are working (takes 30 seconds)
echo "Test Context7 server" | codex --test-mcp

# 2. Quick success indicators you'll see:
✅ "context7: Connected" 
✅ "sequential: Connected"
✅ "magic: Connected" (if API key configured)

# 3. Try a simple command to see MCP in action
/sg:explain "React useEffect" 
# → You'll see Context7 automatically provide official React docs
```

**If something's not working:**
- Missing packages? Run: `SuperCodex install --components mcp --force`
- Need Node.js? Run: `node --version` (requires 16+)
- API keys needed? Magic and Morphllm require paid API keys (skip for now)

## 🎯 The Simple Truth About MCP Servers

MCP (Model Context Protocol) servers are specialized tools that extend Codex CLI's capabilities beyond native functionality. SuperCodex integrates 6 carefully selected MCP servers that automatically activate based on your tasks, providing enhanced documentation access, advanced reasoning, UI generation, browser automation, code transformation, and project memory.

**Seamless Integration**: Type `/sg:implement "React dashboard"` → Magic MCP activates for UI generation. Type `/sg:analyze --think-hard` → Sequential MCP enables structured reasoning. The system intelligently selects the right tools for your context.

## Overview

**What MCP Servers Do:**
- **context7**: Official library documentation and framework patterns  
- **sequential**: Multi-step reasoning and hypothesis testing
- **magic**: Modern UI component generation from 21st.dev patterns  
- **playwright**: Real browser automation and E2E testing
- **morphllm**: Efficient pattern-based code transformations
- **serena**: Semantic code understanding with project memory

**How They Enhance SuperCodex:**
- **Automatic Activation**: Intelligent context-based server selection
- **Parallel Coordination**: Multiple servers working together on complex tasks
- **Quality Enhancement**: Specialized tools for specific domains
- **Efficiency Gains**: 30-50% improvement in complex workflows
- **Session Persistence**: Maintain context across development sessions

## 🧠 Auto-Activation Logic & Server Selection

**How SuperCodex Chooses Servers:**

| Your Request Contains | Servers Activated | Priority Logic |
|----------------------|-------------------|----------------|
| `import`, `require`, API names | **context7** | Official docs always win |
| `--think`, `--think-hard`, debugging | **sequential** | Structured analysis needed |
| `component`, `UI`, `/ui`, `form` | **magic** | UI generation required |
| `test`, `e2e`, `browser`, `playwright` | **playwright** | Real browser automation |
| Multi-file edits, `refactor` | **morphllm** | Pattern-based transformation |
| `load`, `save`, large projects | **serena** | Project memory & navigation |

**Decision Tree - What Happens When:**

```
Your command: "/sg:implement user authentication"
    ↓
1. Parse keywords: "implement", "user", "authentication"
    ↓
2. Check patterns:
   - "authentication" → security patterns → context7 (high)
   - "implement" → code generation → magic (medium) 
   - Multiple files likely → serena (medium)
    ↓
3. Final selection: context7 + magic + serena
4. Result: Official auth patterns + UI components + project structure
```

**Edge Cases & Conflicts:**
- **Multiple triggers**: Higher priority server wins, others assist
- **API keys missing**: Server skipped, fallback to native tools
- **Performance limits**: Essential servers only (context7 + sequential)
- **Manual override**: Your `--magic --no-serena` flags always respected

## Available MCP Servers

### context7 📚
**NPM Package**: `@upstash/context7-mcp@latest` (v1.0.14)

**Purpose**: Official library documentation and framework pattern access

**Technical Specs:**
- **Command**: `npx -y @upstash/context7-mcp@latest`
- **Type**: External NPM package server
- **Dependencies**: Node.js 16+, internet connection
- **API Key**: Not required
- **Memory Usage**: ~50MB active documentation cache

**Capabilities:**
- Curated documentation lookup for 200+ popular libraries
- Version-specific API references and examples  
- Framework best practices and implementation patterns
- Real-time official documentation access (not cached snapshots)

**Auto-Activation Triggers:**
- Library imports: `import`, `require`, `from`, `use`
- Framework keywords: React, Vue, Angular, Next.js, Express, Django
- Documentation requests: "official docs", "API reference", "how to"
- Pattern queries: "best practices", "recommended approach"

#### Success Criteria
- [ ] Server connects without configuration errors
- [ ] Fetches official documentation within 5 seconds
- [ ] Provides version-specific API references
- [ ] Includes working code examples and patterns

**Usage Examples:**
```bash
# Automatic activation
/sg:implement "React useEffect for data fetching"
# → Context7 provides official React hooks documentation

# Manual activation  
/sg:analyze auth-system/ --c7
# → Access authentication pattern libraries

# What you'll see working:
✅ "Fetching React documentation for useEffect..."
✅ "Found official pattern: data fetching with cleanup"
```

**Verify:** Context7 should activate automatically for library imports  
**Test:** `/sg:explain "Express middleware"` should fetch Express.js docs  
**Check:** Documentation should match current library versions

**Best For:**
- Following official framework patterns (not generic tutorials)
- Ensuring API compliance and best practices
- Learning new libraries with authoritative sources
- Version-specific implementation requirements

---

### sequential 🧠
**NPM Package**: `@modelcontextprotocol/server-sequential-thinking` (v2025.7.1)

**Purpose**: Structured multi-step reasoning and systematic analysis

**Technical Specs:**
- **Command**: `npx -y @modelcontextprotocol/server-sequential-thinking`
- **Type**: Official MCP server from Anthropic
- **Dependencies**: Node.js 16+
- **API Key**: Not required
- **Memory Usage**: ~75MB for reasoning chains and hypothesis tracking

**Capabilities:**
- Hypothesis generation and testing workflows with 10+ step chains
- Complex problem decomposition using structured methodologies
- Evidence-based reasoning with citation tracking
- Systematic debugging with root cause analysis trees

**Auto-Activation Triggers:**
- Complex debugging scenarios with multiple layers
- Architectural analysis and system design questions
- `--think`, `--think-hard`, `--ultrathink` flags
- Multi-component failure investigation  
- Performance analysis requiring systematic approach

**Usage Examples:**
```bash
# Automatic activation
/sg:troubleshoot "API performance degrading under load"
# → Sequential enables systematic root cause analysis

# Manual activation  
/sg:analyze --think-hard microservices-architecture/
# → Deep architectural analysis with structured reasoning

# What you'll see working:
✅ "Hypothesis 1: Database connection pooling..."
✅ "Testing evidence: Connection metrics show..."
✅ "Conclusion: Root cause identified in..."
```

**Best For:**
- Root cause analysis of complex issues (not simple bugs)
- System architecture design and evaluation
- Performance bottleneck identification requiring methodical approach
- Security vulnerability assessment with threat modeling

---

### magic ✨
**NPM Package**: `@21st-dev/magic` (v0.1.0) - **Requires API Key**

**Purpose**: Modern UI component generation from 21st.dev design patterns

**Technical Specs:**
- **Command**: `npx @21st-dev/magic`
- **Type**: Third-party UI generation service
- **Dependencies**: Node.js 16+, TWENTYFIRST_API_KEY environment variable
- **API Key**: Required - paid service from 21st.dev
- **Memory Usage**: ~30MB + component generation cache

**Capabilities:**
- Production-ready React, Vue, Angular components with modern patterns
- WCAG 2.1 AA accessibility compliance built-in
- Design system integration with popular frameworks (Tailwind, Material-UI, Chakra)
- Responsive and interactive components with TypeScript support

**Auto-Activation Triggers:**
- UI component requests: button, form, modal, table, nav, card
- `/ui` or `/21` commands
- Frontend development keywords: responsive, accessible, component, design
- Design system implementation needs

**Usage Examples:**
```bash
# Automatic activation
/sg:implement "responsive dashboard with data visualization" 
# → Magic generates modern UI components with accessibility

# Manual activation
/sg:design "e-commerce checkout flow" --magic
# → UI-focused design with component generation

# What you'll see working:
✅ "Generating accessible form components..."
✅ "Applied responsive grid patterns..."
✅ "Added keyboard navigation support..."
```

**API Key Setup:**
```bash
# Get API key from https://21st.dev/api-keys
export TWENTYFIRST_API_KEY="your_key_here"
# Or add to ~/.bashrc or ~/.zshrc for persistence
```

**Best For:**
- Creating production-ready UI components (not prototypes)
- Implementing accessible design systems with compliance  
- Rapid frontend development with modern patterns
- Enterprise-grade component architecture

---

### playwright 🎭
**NPM Package**: `@playwright/mcp@latest` (v0.0.34)

**Purpose**: Real browser automation and comprehensive E2E testing

**Technical Specs:**
- **Command**: `npx @playwright/mcp@latest`
- **Type**: Official Playwright MCP integration
- **Dependencies**: Node.js 16+, browser binaries (auto-installed)
- **API Key**: Not required
- **Memory Usage**: ~200MB + browser instances (~100MB each)

**Capabilities:**
- Cross-browser testing (Chrome, Firefox, Safari, Edge) with real rendering engines
- Visual regression testing with pixel-perfect screenshot comparison
- Accessibility compliance validation with automated WCAG 2.1 testing
- User interaction simulation including mobile device emulation

**Auto-Activation Triggers:**
- Browser testing and E2E scenarios: `test`, `e2e`, `browser`
- Visual testing and screenshot requests: `screenshot`, `visual`, `responsive`
- Accessibility testing requirements: `accessibility`, `a11y`, `wcag`
- User workflow validation needs: `flow`, `journey`, `interaction`

**Usage Examples:**
```bash
# Automatic activation
/sg:test --type e2e "user registration flow"
# → Playwright automates browser testing

# Manual activation
/sg:validate "form accessibility compliance" --play
# → Browser-based accessibility testing

# What you'll see working:
✅ "Launching Chrome browser..."
✅ "Testing form interactions..."
✅ "WCAG compliance: 3 issues found..."
```

**Best For:**
- End-to-end user workflow testing (not unit tests)
- Cross-browser compatibility validation across 4+ browsers
- Visual regression testing with automated comparison
- Accessibility compliance verification with real screen readers

---

### morphllm 🔄
**NPM Package**: `@morph-llm/morph-fast-apply` (v0.6.8) - **Requires API Key**

**Purpose**: Efficient pattern-based code transformations and bulk editing

**Technical Specs:**
- **Command**: `npx @morph-llm/morph-fast-apply /app/`
- **Type**: AI-powered code transformation service
- **Dependencies**: Node.js 16+, MORPH_API_KEY environment variable
- **API Key**: Required - paid service from Morph-LLM
- **Memory Usage**: ~100MB + file processing cache

**Capabilities:**
- Multi-file pattern transformations across 100+ files simultaneously
- Style guide enforcement with custom rule definitions
- Framework migration assistance (React Class → Hooks, Vue 2 → 3)
- Bulk code modernization with semantic understanding

**Auto-Activation Triggers:**
- Multi-file edit operations requiring consistent patterns
- Framework updates and migrations: `migrate`, `update`, `modernize`
- Code cleanup and standardization: `cleanup`, `standardize`, `lint-fix`
- Pattern-based refactoring tasks: `refactor`, `transform`, `apply-pattern`

**Usage Examples:**
```bash
# Automatic activation
/sg:improve legacy-codebase/ --focus maintainability
# → Morphllm applies consistent patterns across files

# Manual activation
/sg:cleanup src/ --morph
# → Pattern-based code organization

# What you'll see working:
✅ "Analyzing 47 files for patterns..."
✅ "Applying consistent naming convention..."
✅ "Updated 23 files with modern syntax..."
```

**API Key Setup:**
```bash
# Get API key from https://morph-llm.com/api-keys  
export MORPH_API_KEY="your_key_here"
# Configure ALL_TOOLS=true for full capabilities (already set)
```

**Best For:**
- Large-scale refactoring projects (50+ files)
- Code style standardization across entire codebases
- Framework migration projects requiring semantic understanding
- Bulk code transformations that preserve logic while updating syntax

---

### serena 🧭
**Installation**: Local Python package via `uv` - **No API Key Required**

**Purpose**: Semantic code understanding with persistent project memory

**Technical Specs:**
- **Command**: `uv run serena start-mcp-server --context ide-assistant`
- **Type**: Local Python-based semantic analysis server
- **Dependencies**: Python 3.9+, uv package manager
- **API Key**: Not required - runs locally
- **Memory Usage**: ~150MB + project index (varies by codebase size)
- **Working Directory**: `$HOME/.codex/serena`

**Capabilities:**
- Symbol-level code navigation with LSP integration
- Cross-session project memory with persistent indexing
- Semantic code transformations using AST analysis
- Large codebase architecture understanding (supports 10K+ files)

**Auto-Activation Triggers:**
- Symbol operations: rename, extract, move functions, find references
- Project-wide code navigation: `navigate`, `find`, `search symbols`
- Session management: `/sg:load`, `/sg:save`, project persistence
- Large codebase analysis requirements (>100 files)

**Usage Examples:**
```bash
# Automatic activation  
/sg:load existing-project/
# → Serena builds project understanding and memory

# Manual activation
/sg:refactor "extract UserService class" --serena
# → Semantic-aware code restructuring

# What you'll see working:
✅ "Building project index..."
✅ "Found 23 references to UserService..."
✅ "Preserving semantic relationships..."
```

**Installation Verification:**
```bash
# Check if serena is properly installed
ls -la ~/.codex/serena/
# Should show serena installation directory

# Test serena server
uv run serena --help
# Should show serena command options
```

**Best For:**
- Long-term project development with session continuity
- Complex codebase navigation (enterprise-scale projects)
- Semantic code refactoring that preserves relationships
- Cross-session context preservation for ongoing work

## Installation & Configuration

### Automatic Installation (Recommended)

**During SuperCodex Setup:**
```bash
SuperCodex install
# → Interactive installer offers MCP server selection
# → Automatically configures selected servers in ~/.codex.json
# → Downloads and configures NPM packages automatically
```

**Installation Options:**
- **All Servers**: Complete MCP capability (requires ~500MB, 2 API keys)
- **Essential Only**: context7 + sequential-thinking (no API keys needed)
- **Custom Selection**: Choose specific servers for your workflow
- **Skip MCP**: Native-only installation for resource constraints

**What Gets Installed:**
```bash
# NPM packages (auto-installed via npx):
✅ @upstash/context7-mcp@latest (1.0.14)
✅ @modelcontextprotocol/server-sequential-thinking (2025.7.1)
✅ @21st-dev/magic (0.1.0) - requires TWENTYFIRST_API_KEY
✅ @playwright/mcp@latest (0.0.34)
✅ @morph-llm/morph-fast-apply (0.6.8) - requires MORPH_API_KEY

# Local Python package:
✅ serena (installed via uv in ~/.codex/serena)
```

### Manual Configuration

**Server-Specific Installation:**
```bash
# Install MCP component (configures all selected servers)
SuperCodex install --components mcp

# Force reinstall with updated configurations
SuperCodex install --components mcp --force

# Validate current configuration
cat ~/.codex.json | jq '.mcpServers'
```

**Configuration File (`~/.codex.json`):**
```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    },
    "sequential": {
      "command": "npx", 
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "magic": {
      "type": "stdio",
      "command": "npx",
      "args": ["@21st-dev/magic"],
      "env": {
        "TWENTYFIRST_API_KEY": "${TWENTYFIRST_API_KEY}"
      }
    },
    "serena": {
      "command": "uv",
      "args": ["run", "serena", "start-mcp-server", "--context", "ide-assistant"],
      "cwd": "$HOME/.codex/serena"
    }
  }
}
```

### Prerequisites by Server

**Node.js Required (Most Servers):**
- Context7, Magic, Sequential, Playwright require Node.js 16+
- Install: `brew install node` (macOS) or visit https://nodejs.org

**Python Required:**
- Morphllm, Serena work with Python environment
- Already satisfied by SuperCodex installation

**System Resources:**
- **Minimal**: 2GB RAM for basic MCP functionality
- **Recommended**: 4GB RAM for full MCP suite
- **Storage**: 200MB additional for MCP server installations

## Usage Patterns

### Automatic Server Selection

**Context-Based Activation:**
SuperCodex analyzes your request and automatically selects optimal MCP servers:

```bash
# Frontend development → Magic + Context7
/sg:implement "responsive navigation component"

# Performance investigation → Sequential + Playwright  
/sg:troubleshoot "page load time >3 seconds"

# Large refactoring → Serena + Morphllm + Sequential
/sg:improve legacy-authentication-system/

# Documentation lookup → Context7
/sg:explain "React useCallback best practices"

# Browser testing → Playwright + Sequential
/sg:test --type e2e user-checkout-flow/
```

**Intelligence Behind Selection:**
- **Keywords**: "component", "UI" → Magic activation
- **File types**: `.jsx`, `.vue` → Magic + Context7
- **Complexity**: Multi-file operations → Serena + Morphllm
- **Analysis depth**: `--think-hard` → Sequential + Context7
- **Testing scope**: E2E workflows → Playwright + Sequential

### Manual Server Control

**Force Specific Servers:**
```bash
# Enable specific servers
/sg:analyze codebase/ --c7 --seq --serena

# Disable all MCP servers
/sg:implement "simple function" --no-mcp

# Enable all servers for maximum capability
/sg:design "complex system architecture" --all-mcp

# Lightweight execution
/sg:explain "function purpose" --no-mcp
```

**Server Combination Strategies:**

**Documentation + Analysis:**
```bash
/sg:analyze security-patterns/ --c7 --seq
# → Context7 provides security patterns + Sequential analyzes implementation
```

**UI Development:**
```bash
/sg:implement "dashboard interface" --magic --c7 --play
# → Magic generates components + Context7 patterns + Playwright testing
```

**Code Transformation:**
```bash
/sg:improve legacy-code/ --serena --morph --seq
# → Serena analyzes structure + Morphllm transforms + Sequential validates
```

### Multi-Server Coordination

**Complex Workflow Example:**
```bash
/sg:implement "e-commerce checkout system"
```

**Automatic Coordination:**
1. **Sequential**: Breaks down checkout workflow systematically
2. **Context7**: Provides payment integration patterns
3. **Magic**: Generates checkout UI components
4. **Serena**: Manages code organization and dependencies
5. **Playwright**: Creates E2E testing for checkout flow

**Efficiency Gains:**
- **30-50% faster development** through specialized tools
- **Higher quality output** through domain expertise
- **Reduced context switching** with intelligent automation
- **Comprehensive coverage** across all development aspects

## Advanced Features

### Multi-Server Orchestration

**Intelligent Workflow Coordination:**
SuperCodex orchestrates multiple MCP servers for complex tasks:

**Full-Stack Development Workflow:**
```bash
/sg:implement "real-time chat application"
```
1. **Sequential**: Analyzes requirements and architecture
2. **Context7**: Provides WebSocket and React patterns  
3. **Magic**: Generates chat UI components
4. **Serena**: Manages project structure and dependencies
5. **Playwright**: Creates E2E tests for messaging flow
6. **Morphllm**: Applies consistent code patterns

**Performance Optimization Workflow:**
```bash
/sg:analyze --focus performance --ultrathink
```
1. **Sequential**: Systematic performance analysis methodology
2. **Serena**: Code structure and bottleneck identification
3. **Context7**: Framework-specific optimization patterns
4. **Playwright**: Real browser performance testing
5. **Morphllm**: Code optimization pattern application

### Resource Management

**Performance Optimization:**

**Smart Resource Allocation:**
- **Green Zone** (0-75% usage): All servers available
- **Yellow Zone** (75-85%): Priority servers only
- **Red Zone** (85%+): Essential servers, compressed output

**Server Priority Matrix:**
| Priority | Servers | Use Case |
|----------|---------|----------|
| **Essential** | context7, sequential | Core functionality |
| **High** | magic, serena | Development workflows |
| **Standard** | playwright, morphllm | Testing and optimization |

**Concurrency Control:**
```bash
# Limit concurrent server operations
/sg:implement "complex feature" --concurrency 2

# Maximum performance mode
/sg:analyze large-codebase/ --all-mcp --concurrency 6

# Resource-constrained mode  
/sg:troubleshoot issue/ --c7 --seq --concurrency 1
```

### Advanced Configuration

**Custom Server Configurations:**
```json
{
  "mcpServers": {
    "context7": {
      "command": "node",
      "args": ["/custom/context7-server"],
      "env": {
        "CONTEXT7_CACHE_SIZE": "1000",
        "CONTEXT7_TIMEOUT": "30000"
      }
    },
    "sequential": {
      "command": "node",
      "args": ["/custom/sequential-server"],
      "env": {
        "MAX_THINKING_DEPTH": "10",
        "REASONING_TIMEOUT": "60000"
      }
    }
  }
}
```

**Performance Tuning:**
- **Context7**: Cache size, request timeout, documentation sources
- **Sequential**: Thinking depth, reasoning timeout, branch limits
- **Magic**: Component complexity, accessibility level, framework targets
- **Playwright**: Browser pool size, timeout values, screenshot quality
- **Morphllm**: Pattern matching precision, transformation scope
- **Serena**: Memory retention, project indexing depth, symbol resolution

### Integration Patterns

**Mode Integration:**
- **analysis mode**: Sequential for structured discovery
- **Task Management Mode**: Serena for session persistence
- **Orchestration Mode**: All servers for optimal tool selection
- **Token Efficiency Mode**: Selective activation for resource optimization

**Command Integration:**
- **Analysis Commands**: Sequential + Serena for deep understanding
- **Implementation Commands**: Magic + Context7 for development
- **Testing Commands**: Playwright + Sequential for comprehensive validation
- **Documentation Commands**: Context7 + Magic for pattern-rich docs

## Troubleshooting & Quick Fixes

### 🚨 Quick Troubleshooting

### Common Issues (< 2 minutes)
- **No servers connected**: Check Node.js installation: `node --version` (need v16+)
- **Context7 server fails**: Clear NPM cache: `npm cache clean --force`
- **Magic/Morphllm errors**: Expected if no API keys configured (paid services)
- **Server timeouts**: Restart Codex CLI session to reset connections
- **Performance issues**: Use `--no-mcp` for lightweight execution

### Immediate Fixes
- **Reset MCP**: Restart Codex CLI session to refresh server connections
- **Check dependencies**: Verify Node.js v16+ with `node --version`
- **Clear cache**: Run `npm cache clean --force` for package issues
- **Bypass servers**: Use `--no-mcp` flag to test without MCP servers

### 🚨 Setup Failures - Immediate Solutions

**MCP Server Issues - Step-by-Step Resolution:**

**Step 1: Quick Health Check (30 seconds)**
```bash
# Check if configuration exists
ls ~/.codex/.codex.json
# Should show: /home/user/.codex/.codex.json

# Check Node.js version (critical dependency)
node --version  
# Should show: v16.x.x or higher

# Test basic MCP connectivity
SuperCodex status --mcp
# Should show connected servers (at least context7, sequential-thinking)
```

**Step 2: Common Fixes (1-2 minutes)**
```bash
# Missing Node.js? Install it:
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# NPM packages not found? Clear cache:
npm cache clean --force

# Configuration corrupted? Reinstall:
SuperCodex install --components mcp --force

# Permissions issue? Fix MCP directory:
chmod -R 755 ~/.codex/
```

**Step 3: Server-Specific Validation (2-3 minutes)**
```bash
# Test context7 (should work without API key):
/sg:explain "React useEffect"
# ✅ Should show: "Fetching React documentation..."

# Test sequential-thinking:
/sg:analyze complex-issue/ --think
# ✅ Should show: "Hypothesis 1:..." or reasoning steps

# Test playwright (should work without API key):
/sg:test --type e2e simple-page
# ✅ Should launch browser automation

# Magic/Morphllm failures expected without API keys
```

**Step 4: Advanced Diagnostics (5+ minutes)**
```bash
# Detailed MCP server logs
tail -f ~/.codex/logs/mcp-*.log

# Test individual server connections
SuperCodex test-mcp --server context7
SuperCodex test-mcp --server sequential-thinking

# Check for port conflicts
netstat -tulpn | grep :3000
lsof -i :3000

# Reset all MCP configurations
SuperCodex uninstall --components mcp
SuperCodex install --components mcp
```

### Server-Specific Troubleshooting

**Context7 Server Issues:**
```bash
# Problem: "Context7 connection failed"
# Quick Fix: NPM and dependency issues
npm cache clean --force
npx -y @upstash/context7-mcp@latest --version  # Test package
/sg:explain "React" --c7                       # Test server directly
```

**Sequential Server Issues:**
```bash
# Problem: "Sequential server not responding"
# Quick Fix: Verify Anthropic MCP server
npx -y @modelcontextprotocol/server-sequential-thinking --version
/sg:analyze problem/ --seq --think             # Test reasoning
```

**Magic/Morphllm API Key Issues:**
```bash
# Problem: "API key required" (expected for paid services)
# Solution 1: Set environment variables
export TWENTYFIRST_API_KEY="your_key_here"
export MORPH_API_KEY="your_key_here"

# Solution 2: Skip paid services
/sg:command --no-mcp                          # Use native tools only
/sg:command --c7 --seq --play                 # Free servers only
```

### 🔧 Activating Disabled MCP Servers

Some MCP servers are installed but **disabled by default**. Here's how to activate them:

**1. Magic Server** - Disabled (API key required)
```bash
# Get API key from 21st.dev
# Visit https://21st.dev/api-keys to obtain your key

# Activate magic server
export TWENTYFIRST_API_KEY="your_key_here"
echo 'export TWENTYFIRST_API_KEY="your_key_here"' >> ~/.bashrc  # Make persistent

# Test activation
/sg:implement "responsive form component" --magic
# ✅ Should now generate UI components
```

**2. Serena Server** - Ready to activate (no API key needed)
```bash
# Serena is pre-installed and ready - just needs activation
# Enable when you need project memory and semantic navigation

# Activate serena for current session
/sg:load large-project/ --serena
# ✅ Should start project indexing and memory

# Verify serena is working
ls ~/.codex/serena/
uv run serena --help
# ✅ Should show serena installation and commands
```

**3. Morphllm Server** - Disabled (API key required)  
```bash
# Get API key from Morph-LLM
# Visit https://morph-llm.com/api-keys to obtain your key

# Activate morphllm server
export MORPH_API_KEY="your_key_here"  
echo 'export MORPH_API_KEY="your_key_here"' >> ~/.bashrc  # Make persistent

# Test activation
/sg:improve legacy-code/ --morph
# ✅ Should now perform pattern-based code transformations
```

**Why These Servers Are Disabled by Default:**
- **Magic**: Requires paid API service from 21st.dev
- **Serena**: Complex semantic operations - enable for large projects only
- **Morphllm**: Requires paid API service from Morph-LLM

**When to Enable Each:**
- **Magic**: Building production UI components with 21st.dev API access
- **Serena**: Large codebases (>100 files) needing project memory and semantic navigation
- **Morphllm**: Bulk code transformations with Morph-LLM API access

**Playwright Browser Issues:**
```bash
# Problem: "Browser launch failed"
# Quick Fix: Browser dependencies
npx playwright install                        # Install browsers
/sg:test --type e2e --browser chrome         # Test specific browser
```

**Serena Local Server Issues:**
```bash
# Problem: "Serena server startup failed"
# Quick Fix: Python environment
ls ~/.codex/serena/                         # Verify installation
uv run serena --help                         # Test serena command
/sg:load project/ --serena                   # Test server directly
```

### Error Code Reference

| MCP Error | Server | Meaning | Quick Fix |
|-----------|--------|---------|-----------|
| **M001** | context7 | Package not found | Run `npm cache clean --force` |
| **M002** | sequential | Connection timeout | Restart Codex CLI session |
| **M003** | magic | API key missing | Set `TWENTYFIRST_API_KEY` or use `--no-mcp` |
| **M004** | playwright | Browser missing | Run `npx playwright install` |
| **M005** | morphllm | API key missing | Set `MORPH_API_KEY` or use `--no-mcp` |
| **M006** | serena | Python/uv issue | Check `uv run serena --help` |
| **M007** | * | Node.js version | Upgrade to Node.js v16+ |
| **M008** | * | Permission denied | Run `chmod -R 755 ~/.codex/` |

### Performance Issues

**Server Resource Management:**
```bash
# Problem: System slowing down with all MCP servers
# Quick Fix: Selective server usage
/sg:command --c7 --seq                       # Essential servers only
/sg:command --concurrency 1                  # Limit parallel ops
/sg:command --memory-limit 1024              # Limit memory to 1GB
```

**Server Timeout Issues:**
```bash
# Problem: Commands hanging with MCP servers
# Quick Fix: Timeout and restart management
/sg:command --timeout 30                     # Set explicit timeout
killall node                                 # Reset all MCP servers
SuperCodex restart --mcp                    # Restart MCP system
```

### Progressive Support Levels

**Level 1: Quick Fix (< 2 min)**
- Use the Common Issues section above
- Try `--no-mcp` to bypass MCP servers
- Restart Codex CLI session

**Level 2: Detailed Help (5-15 min)**
```bash
# MCP-specific diagnostics
SuperCodex diagnose --mcp
tail -f ~/.codex/logs/mcp-*.log
SuperCodex test-mcp --all-servers
```
- See [Common Issues Guide](../Reference/common-issues.md) for MCP installation problems
- See [MCP Server Guide](../Reference/mcp-server-guide.md) for detailed server troubleshooting

**Level 3: Expert Support (30+ min)**
```bash
# Deep MCP analysis
SuperCodex diagnose --mcp --full-system
lsof | grep mcp
netstat -tulpn | grep node
# Check individual server configurations
```
- See [Diagnostic Reference Guide](../Reference/diagnostic-reference.md) for comprehensive system analysis

**Level 4: Community Support**
- Report MCP issues at [GitHub Issues](https://github.com/SuperCodex-Org/SuperCodex_Framework/issues)
- Include server status output from Level 2
- Specify which servers are failing

### Success Validation

After applying MCP fixes, test with:
- [ ] `SuperCodex status --mcp` (should show connected servers)
- [ ] `/sg:explain "test" --c7` (context7 should fetch documentation)
- [ ] `/sg:analyze test/ --seq` (sequential should show reasoning)
- [ ] MCP flags work: `--magic`, `--play` (if configured)
- [ ] Performance is acceptable for your system

### Diagnostics

**MCP Server Status Check:**
```bash
# Check all server health
SuperCodex status --mcp

# Test individual servers
SuperCodex test-mcp --server context7
SuperCodex test-mcp --server sequential

# Detailed diagnostics
SuperCodex diagnose --verbose
```

**Log Analysis:**
```bash
# View MCP server logs
tail -f ~/.codex/logs/mcp-context7.log
tail -f ~/.codex/logs/mcp-sequential.log

# SuperCodex operation logs  
tail -f ~/.codex/logs/superclaude.log

# Codex CLI MCP logs
tail -f ~/.codex/logs/codex-mcp.log
```

**Manual Testing:**
```bash
# Test Context7 documentation lookup
echo "Test React hooks documentation" | codex --mcp context7

# Test Sequential reasoning
echo "Analyze this complex problem" | codex --mcp sequential

# Test server combination
echo "Complex analysis task" | codex --mcp context7,sequential
```

### Resolution Steps

**Step 1: Basic Verification**
1. Check SuperCodex installation: `SuperCodex --version`
2. Verify MCP component: `SuperCodex install --list-components`
3. Check Node.js: `node --version` (should be 16+)
4. Restart Codex CLI session

**Step 2: Configuration Check**
1. Verify `.codex.json` exists: `ls ~/.codex/.codex.json`
2. Check server paths and permissions
3. Test configuration syntax: `SuperCodex validate-config`

**Step 3: Server Specific**
1. **Context7**: Check documentation server connection
2. **Sequential**: Verify reasoning engine startup
3. **Magic**: Test UI component generation endpoint
4. **Playwright**: Check browser automation setup
5. **Morphllm**: Verify code transformation pipeline
6. **Serena**: Test project memory and indexing

**Step 4: Full Reset (Last Resort)**
```bash
# Backup existing configuration
cp ~/.codex/.codex.json ~/.codex/.codex.json.backup

# Remove and reinstall MCP
SuperCodex uninstall --components mcp
SuperCodex install --components mcp

# Restore custom settings if needed
```

## Developer Integration

### MCP Server Development

**Creating Custom MCP Servers:**

**Server Structure:**
```javascript
// custom-mcp-server.js
import { Server } from '@modelcontextprotocol/sdk/server/index.js';

const server = new Server(
  {
    name: "custom-server",
    version: "1.0.0"
  },
  {
    capabilities: {
      resources: {},
      tools: {},
      prompts: {}
    }
  }
);

// Tool implementation
server.setRequestHandler(
  'tools/call',
  async (request) => {
    // Custom tool logic
    return { content: [{ type: "text", text: result }] };
  }
);
```

**SuperCodex Integration:**
```python
# setup/components/custom_mcp.py
from setup.components.base import BaseComponent

class CustomMCPComponent(BaseComponent):
    def get_metadata(self):
        return {
            "name": "custom_mcp",
            "description": "Custom MCP server integration",
            "dependencies": ["core"]
        }
    
    def install(self, install_dir):
        # Install custom server configuration
        self._install_mcp_config(install_dir)
```

### Communication Protocols

**MCP Protocol Flow:**
1. **Initialization**: Codex CLI connects to MCP server via JSON-RPC
2. **Capability Exchange**: Server announces available tools and resources
3. **Request/Response**: Codex sends requests, server processes and responds
4. **Session Management**: Maintain context across multiple interactions

**Message Structure:**
```json
{
  "jsonrpc": "2.0",
  "id": "request-id",
  "method": "tools/call",
  "params": {
    "name": "analyze-code",
    "arguments": {
      "code": "function example() { return 'hello'; }",
      "language": "javascript"
    }
  }
}
```

**SuperCodex MCP Interface:**
```python
class MCPCoordinator:
    def select_servers(self, task_context):
        """Intelligent server selection based on task analysis"""
        servers = []
        
        if self._needs_documentation(task_context):
            servers.append("context7")
        
        if self._needs_reasoning(task_context):
            servers.append("sequential")
            
        if self._needs_ui_generation(task_context):
            servers.append("magic")
            
        return servers
    
    def coordinate_request(self, servers, request):
        """Orchestrate multi-server workflows"""
        results = []
        for server in servers:
            result = await self._send_request(server, request)
            results.append(result)
        
        return self._synthesize_results(results)
```

### Integration APIs

**Configuration API:**
```python
# Register custom MCP server
from setup.services.config_service import ConfigService

config_service = ConfigService()
config_service.add_mcp_server({
    "name": "custom-server",
    "command": "node",
    "args": ["/path/to/custom-server.js"],
    "env": {"CUSTOM_CONFIG": "value"}
})
```

**Tool Registration:**
```python
# Register server capabilities with SuperCodex
from setup.core.mcp_registry import MCPRegistry

registry = MCPRegistry()
registry.register_server("custom-server", {
    "capabilities": ["code-analysis", "documentation"],
    "triggers": ["custom", "analyze", "special-keyword"],
    "priority": "standard"
})
```

**Integration Testing:**
```python
# Test custom MCP server integration
from setup.testing.mcp_test import MCPTestSuite

test_suite = MCPTestSuite()
test_suite.test_server_connection("custom-server")
test_suite.test_tool_functionality("custom-server", "analyze-code")
test_suite.test_integration_workflow(["custom-server", "sequential"])
```

---

## 🎯 Server Selection Decision Tree

**When You Should Use Multiple Servers:**

```
Building a web application?
├─ Need UI components? → magic + context7
├─ Complex architecture? → sequential-thinking + serena  
├─ Need testing? → playwright + sequential-thinking
└─ Large codebase? → serena + morphllm-fast-apply

Debugging performance issues?  
├─ Single component? → sequential-thinking only
├─ Frontend issues? → playwright + sequential-thinking
├─ Backend/Database? → sequential-thinking + context7
└─ Architecture-wide? → sequential-thinking + serena + context7

Learning new technology?
├─ Official docs needed? → context7 + sequential-thinking  
├─ Need examples? → context7 + magic (for UI)
└─ Complex concepts? → sequential-thinking + context7
```

**API Key Decision Matrix:**
- **No API keys available**: Use context7 + sequential-thinking + playwright + serena (4 servers)
- **Have budget for 1 API key**: Add magic for UI development
- **Have budget for 2 API keys**: Add morphllm-fast-apply for large refactoring projects

## MCP Server Quick Reference 📋

| Server | Purpose | Auto-Triggers | Manual Flags | API Key | Best For |
|--------|---------|---------------|--------------|---------|----------|
| **context7** | Documentation | Library imports, API questions | `--c7`, `--context7` | ❌ No | Official patterns, framework docs |
| **sequential** | Reasoning | Complex debugging, analysis | `--seq`, `--sequential` | ❌ No | Systematic thinking, root cause |
| **magic** | UI Generation | Component requests, frontend | `--magic` | ✅ Yes | Modern UI, accessibility |
| **playwright** | Browser Testing | E2E testing, visual validation | `--play`, `--playwright` | ❌ No | User workflows, cross-browser |
| **morphllm** | Code Transform | Multi-file edits, refactoring | `--morph`, `--morphllm` | ✅ Yes | Pattern application, bulk changes |
| **serena** | Project Memory | Symbol operations, large codebases | `--serena` | ❌ No | Session persistence, navigation |

**Common Server Combinations:**
- **Beginner Web Development**: context7 + sequential + playwright (no API keys needed)
- **Professional UI Development**: magic + context7 + serena (1 API key required)
- **Enterprise Refactoring**: serena + morphllm + sequential (1 API key required) 
- **Full-Stack Production**: All 6 servers (2 API keys required)
- **Learning/Research**: context7 + sequential (lightweight, no API keys)

**Performance Control:**
- `--all-mcp`: Enable all servers (max capability, requires API keys)
- `--no-mcp`: Disable all servers (lightweight, native tools only)
- `--concurrency N`: Control parallel operations (1-15)
- Resource awareness: Auto-scaling based on system load

---

## Related Guides

**Learning Progression:**

**🌱 Essential (Week 1)**
- [Quick Start Guide](../Getting-Started/quick-start.md) - Experience MCP servers naturally
- [Installation Guide](../Getting-Started/installation.md) - MCP server setup
- [Commands Reference](commands.md) - Commands that activate MCP servers

**🌿 Intermediate (Week 2-3)**
- [Behavioral Modes](modes.md) - How modes coordinate MCP servers
- [Agents Guide](agents.md) - Agent-MCP server integration
- [Examples Cookbook](../Reference/examples-cookbook.md) - MCP workflow patterns

**🌲 Advanced (Month 2+)**
- [Session Management](session-management.md) - Serena MCP workflows
- [Best Practices](../Reference/quick-start-practices.md) - MCP optimization strategies
- [Flags Guide](flags.md) - Advanced MCP control

**🔧 Expert**
- [Technical Architecture](../Developer-Guide/technical-architecture.md) - MCP integration details
- [Contributing Code](../Developer-Guide/contributing-code.md) - Custom MCP development
- [Testing & Debugging](../Developer-Guide/testing-debugging.md) - MCP troubleshooting

**MCP-Specific Resources:**
- **Official MCP Documentation**: https://modelcontextprotocol.io/
- **Context7 Server**: Enhanced documentation lookup capabilities
- **Sequential Thinking**: Advanced reasoning and analysis
- **Magic UI**: Modern component generation from 21st.dev
- **Community MCP Servers**: https://github.com/modelcontextprotocol/servers