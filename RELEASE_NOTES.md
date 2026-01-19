# GitHub Release v1.0.0 发布说明

## 在 GitHub 创建 Release 的步骤

### 1. 访问 Release 页面
浏览器打开：https://github.com/xdaicode/skills/releases/new

### 2. 填写以下信息

**Tag version**: 选择或输入 `v1.0.0`

**Release title**: `v1.0.0 - Initial Release`

**Description**: 粘贴下面的内容：

---

## 🎉 Initial Release - Claude JSONL to Markdown Converter

Convert Claude AI Agent JSONL session logs into readable Markdown documents.

A powerful CLI tool and Claude Skill for extracting, formatting, and sharing AI conversations.

### ✨ Features

- 📖 **Extract Complete Conversations** - Parse all user and assistant messages
- 🎨 **Clean Markdown Output** - Well-structured, easy to read documents
- 🌍 **Full UTF-8 Support** - Handles Chinese, emojis, and special symbols
- 🔧 **Smart Content Filtering** - Skip tool call noise, keep valuable content
- 🚀 **Cross-Platform** - Works on Windows, macOS, and Linux
- ⚡ **Zero Dependencies** - Uses only Python standard library
- 🎯 **Multiple Use Modes** - CLI tool or Claude Skill

### 📦 Installation

#### Option 1: Clone and Run

```bash
git clone https://github.com/xdaicode/skills.git
cd skills
python jsonl_converter.py your_session.jsonl
```

#### Option 2: Install as Package

```bash
git clone https://github.com/xdaicode/skills.git
cd skills
pip install -e .

# Then use the command
jsonl2md your_session.jsonl
```

#### Option 3: As Claude Skill

Copy `SKILL.md` and `jsonl_converter.py` to your Claude skills directory (`~/.claude/skills/`)

### 🚀 Quick Start

```bash
# Basic conversion
python jsonl_converter.py session.jsonl

# Specify output file
python jsonl_converter.py input.jsonl output.md

# Using installed command
jsonl2md input.jsonl output.md
```

### 📖 Documentation

- 📚 [Full Documentation](https://github.com/xdaicode/skills/blob/main/README.md)
- 🎯 [Claude Skill Guide](https://github.com/xdaicode/skills/blob/main/SKILL.md)
- 🤝 [Contributing Guide](https://github.com/xdaicode/skills/blob/main/CONTRIBUTING.md)
- 📝 [Changelog](https://github.com/xdaicode/skills/blob/main/CHANGELOG.md)

### 🎯 Use Cases

- 📚 **Review AI Agent Behavior** - Debug and validate agent actions
- 📝 **Extract Knowledge** - Save valuable AI-generated content
- 🔍 **Search Conversations** - Find specific discussions quickly
- 📤 **Share Sessions** - Export readable logs for teams
- 🗄️ **Archive Records** - Keep conversation history in version control

### 💻 Example

**Input** (`session.jsonl`):
```json
{"type":"user","message":{"role":"user","content":"Hello!"},"timestamp":"2026-01-18T10:00:00Z"}
{"type":"assistant","message":{"role":"assistant","content":"Hi there!"},"timestamp":"2026-01-18T10:00:05Z"}
```

**Output** (`session_readable.md`):
```markdown
# AI Agent Session Log

**Total Messages**: 2

---

## [1] USER
**Time**: 2026-01-18 10:00:00

**Content**:
Hello!

---

## [2] ASSISTANT
**Time**: 2026-01-18 10:00:05

**Content**:
Hi there!
```

### 🔧 Technical Details

- **Python**: 3.7+ (no external dependencies)
- **License**: MIT
- **Format**: JSONL → Markdown
- **Encoding**: UTF-8 (full international support)
- **Platform**: Windows, macOS, Linux

### 🙏 Acknowledgments

Built for the [Claude AI](https://claude.com) community to help developers and researchers extract value from AI conversation logs.

Inspired by [Anthropic Skills Repository](https://github.com/anthropics/skills).

### 📮 Support

- 🐛 [Report Issues](https://github.com/xdaicode/skills/issues)
- 💡 [Request Features](https://github.com/xdaicode/skills/issues)
- 📖 [Documentation](https://github.com/xdaicode/skills/wiki)

### ⭐ Show Your Support

If this project helped you, please consider giving it a star!

---

**Full Changelog**: https://github.com/xdaicode/skills/blob/main/CHANGELOG.md

**License**: [MIT](https://github.com/xdaicode/skills/blob/main/LICENSE)
