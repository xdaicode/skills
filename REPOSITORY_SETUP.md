# GitHub 仓库配置指南

## 📋 仓库设置清单

访问：https://github.com/xdaicode/skills/settings

### 1. 基本信息

**Repository name** (仓库名):
- 当前: `skills`
- 建议: 保持不变或改为 `claude-jsonl-converter`（更明确）

**Description** (描述):
```
Convert Claude AI JSONL session logs to readable Markdown documents. A CLI tool and Claude Skill for extracting, formatting, and sharing AI conversations.
```

**Website** (网站):
```
https://xdaicode.github.io/skills (如果有文档站点)
```

### 2. Topics 标签

添加这些标签到仓库（在 About 部分）：
```
claude
claude-ai
claude-code
jsonl
markdown
converter
python
cli-tool
ai-logs
session-export
python3
utf-8
cli
terminal
conversation
ai-assistant
log-parser
```

### 3. Features 配置

在仓库根目录创建 `.github/FUNDING.yml`：

```yaml
# These are supported funding model platforms

github: # Replace with up to 4 GitHub Sponsors-enabled usernames e.g., [user1, user2]
patreon: # Replace with a single Patreon username
open_collective: # Replace with a single Open Collective username
ko_fi: # Replace with a single Ko-fi username
tidelift: # Replace with a single Tidelift platform-name/package-name e.g., npm/babel
community_bridge: # Replace with a single Community Bridge project-name e.g., cloud-foundry
liberapay: # Replace with a single Liberapay username
issuehunt: # Replace with a single IssueHunt username
otechie: # Replace with a single Otechie username
custom: # Replace with up to 4 custom sponsorship URLs e.g., ['link1', 'link2', 'link3', 'link4']
```

或者创建 `.github/README.md` 用于 GitHub Pages（可选）：

```markdown
---
layout: home
title: Claude JSONL to Markdown Converter
---

# Claude JSONL to Markdown Converter

Convert Claude AI JSONL session logs to readable Markdown documents.

## Quick Start

```bash
pip install claude-jsonl-converter
jsonl2md your_session.jsonl
```

## Documentation

Visit [GitHub Repository](https://github.com/xdaicode/skills) for full documentation.
```

### 4. Branch Protection（可选但推荐）

设置：Settings → Branches

**Default branch**: `main`

**Branch protection rules**:
- [x] Require a pull request before merging
  - [x] Require approvals: 1
- [x] Require status checks to pass before merging
  - [x] Require branches to be up to date before merging

### 5. Webhooks（可选）

如果要集成 CI/CD：
- Settings → Webhooks
- Add webhook: https://actions.github.com

### 6. 协作者（如果需要）

Settings → Collaborators
- Add team members who can push to the repository

### 7. 自动化链接

**Issues**:
- 创建模板: `.github/ISSUE_TEMPLATE/bug_report.md`
- 创建模板: `.github/ISSUE_TEMPLATE/feature_request.md`

**Pull Requests**:
- 创建模板: `.github/PULL_REQUEST_TEMPLATE.md`

### 8. Badge 徽章（添加到 README.md）

已在 README.md 中包含：
- License: MIT
- Python 3.7+
- Claude Skill

可以添加的额外徽章：
```markdown
[![GitHub stars](https://img.shields.io/github/stars/xdaicode/skills?style=social)](https://github.com/xdaicode/skills/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/xdaicode/skills?style=social)](https://github.com/xdaicode/skills/network/members)
[![GitHub issues](https://img.shields.io/github/issues/xdaicode/skills)](https://github.com/xdaicode/skills/issues)
```

### 9. 社区健康文件

确保以下文件存在：
- ✅ LICENSE (MIT)
- ✅ README.md
- ✅ CONTRIBUTING.md
- ✅ CHANGELOG.md
- ✅ CODE_OF_CONDUCT.md (可选)
- ✅ SECURITY.md (可选)

---

## 🚀 快速操作步骤

### 立即执行（5分钟）:

1. **添加 Topics**:
   - 访问 https://github.com/xdaicode/skills
   - 点击 "About" 右侧的 ⚙️
   - 添加上述 Topics

2. **更新描述**:
   - 在 About 部分点击编辑
   - 粘贴上面的 Description

3. **创建 Release**:
   - 访问 https://github.com/xdaicode/skills/releases/new
   - 按照 RELEASE_NOTES.md 的说明创建

### 后续优化（可选）:

4. **设置 GitHub Pages** (如果需要文档站点)
5. **配置 Branch Protection**
6. **添加 Funding.yml** (如果接受赞助)

---

准备好创建 Release 了吗？打开这个链接开始：

👉 https://github.com/xdaicode/skills/releases/new
