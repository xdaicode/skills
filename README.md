# Claude JSONL to Markdown Converter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Claude Skill](https://img.shields.io/badge/Claude-Skill-green.svg)](https://github.com/anthropics/skills)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> Convert Claude AI Agent JSONL session logs into readable Markdown documents

## ✨ Features

- 📖 **Extract Complete Conversations** - Parse and format all user and assistant messages
- 🎨 **Clean Markdown Output** - Well-structured, easy to read documents
- 🌍 **Full UTF-8 Support** - Handles Chinese characters, emojis, and special symbols
- 🔧 **Smart Content Filtering** - Skip tool call noise, keep valuable content
- 🚀 **Cross-Platform** - Works on Windows, macOS, and Linux
- ⚡ **Zero Dependencies** - Uses only Python standard library
- 🎯 **Multiple Use Modes** - CLI tool or Claude Skill

## 📦 Installation

### Option 1: As Claude Skill ⭐ (Recommended)

#### Manual Install

Clone to your Claude skills directory:
```bash
cd ~/.claude/skills
git clone https://github.com/xdaicode/skills.git jsonl-converter
```

Then restart Claude Code and use:
```
Please convert d:/AI/session.jsonl to a readable document
```

📖 **See**: [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md) for detailed installation guide

### Option 2: Direct Download

```bash
# Clone the repository
git clone https://github.com/xdaicode/skills.git
cd skills

# Run directly
python jsonl_converter.py session.jsonl
```

### Option 3: Install as Package

```bash
# From local directory
cd skills
pip install -e .

# Or install directly from GitHub
pip install git+https://github.com/xdaicode/skills.git
```

**Note**: After installation, you can use `python -m jsonl_converter` instead of the full path.

## 🚀 Usage

### Method 1: Direct Script (Recommended)

```bash
# Basic conversion
python jsonl_converter.py session.jsonl

# Specify output file
python jsonl_converter.py input.jsonl output.md
```

This creates `session_readable.md` in the same directory.

### Method 2: Using Python Module (After Installation)

```bash
# Convert using Python module
python -m jsonl_converter session.jsonl

# With custom output
python -m jsonl_converter input.jsonl output.md
```

### Method 3: In Claude Code

Simply tell Claude:
```
Please convert d:/AI/agent-session.jsonl to a readable document
```

Claude will automatically use the skill to perform the conversion.

## 📖 Example

### Input: `session.jsonl`

```json
{"type":"user","message":{"role":"user","content":"Hello, Claude!"},"timestamp":"2026-01-18T10:00:00Z"}
{"type":"assistant","message":{"role":"assistant","content":"Hello! How can I help you today?"},"timestamp":"2026-01-18T10:00:05Z"}
{"type":"user","message":{"role":"user","content":"Can you explain Yoshop configuration?"},"timestamp":"2026-01-18T10:00:10Z"}
{"type":"assistant","message":{"role":"assistant","content":"Of course! Yoshop requires..."},"timestamp":"2026-01-18T10:00:15Z"}
```

### Output: `session_readable.md`

```markdown
# AI Agent Session Log

**Session ID**: abc123
**Agent Slug**: my-agent
**Total Messages**: 4

---

## [1] USER
**Time**: 2026-01-18 10:00:00

**Content**:
Hello, Claude!

---

## [2] ASSISTANT
**Time**: 2026-01-18 10:00:05

**Content**:
Hello! How can I help you today?

---

## [3] USER
**Time**: 2026-01-18 10:00:10

**Content**:
Can you explain Yoshop configuration?

---

## [4] ASSISTANT
**Time**: 2026-01-18 10:00:15

**Content**:
Of course! Yoshop requires...

---
```

## 🎯 Use Cases

### 📚 Review AI Agent Behavior
Debug and validate agent actions by examining complete conversation history.

### 📝 Extract Knowledge
Save valuable AI-generated content (tutorials, guides, explanations) from sessions.

### 🔍 Search Conversations
Easily search through exported Markdown to find specific discussions.

### 📤 Share Sessions
Export readable logs for team collaboration or documentation.

### 🗄️ Archive Records
Keep conversation history in version control for future reference.

## 🛠️ How It Works

The converter:

1. **Reads** JSONL files line by line (memory efficient for large files)
2. **Parses** JSON objects with Claude Agent metadata
3. **Extracts** content from different message types:
   - `text` - User and assistant messages
   - `tool_use` - Tool invocations (simplified display)
   - `tool_result` - Tool outputs (truncated if too long)
4. **Formats** timestamps to human-readable format
5. **Filters** noise (skips standalone tool calls)
6. **Outputs** clean Markdown document

## 📋 Requirements

- Python 3.7 or higher
- No external dependencies

## 🧪 Testing

```bash
# Run tests (if available)
python -m pytest tests/

# Manual test
python jsonl_converter.py test_data/sample.jsonl
```

## 📂 Project Structure

```
claude-jsonl-converter/
├── jsonl_converter.py      # Main converter script
├── SKILL.md                 # Claude Skill definition
├── README.md                # This file
├── README_zh.md             # Chinese documentation
├── LICENSE                  # MIT License
├── setup.py                 # Package configuration
├── pyproject.toml          # Modern Python config
└── .gitignore              # Git ignore rules
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 🐛 Reporting Issues

Found a bug? Please open an issue with:

- Clear title and description
- Steps to reproduce
- Expected vs actual behavior
- Environment (OS, Python version)
- Sample JSONL file (if possible, sanitize sensitive data)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built for [Claude Code](https://claude.com/code)
- Inspired by [Anthropic Skills Repository](https://github.com/anthropics/skills)
- Created to help the Claude AI community

## 📮 Support

- 📖 [Documentation](https://github.com/xdaicode/skills/claude-jsonl-converter/wiki)
- 🐛 [Report Issues](https://github.com/xdaicode/skills/claude-jsonl-converter/issues)
- 💡 [Feature Requests](https://github.com/xdaicode/skills/claude-jsonl-converter/issues)

## 🔮 Roadmap

- [ ] Add JSON output format option
- [ ] Add HTML output format option
- [ ] Create web interface
- [ ] Add conversation statistics
- [ ] Support other AI log formats

## ⭐ Show Your Support

If this project helped you, please consider giving it a ⭐️!

---

Made with ❤️ for the Claude AI community
