# Claude Code 插件安装指南

## ⚠️ 重要说明

当前仓库结构**不支持**直接通过 `/plugin marketplace add` 命令安装。

这是因为缺少必需的 `marketplace.json` 文件和插件市场结构。

---

## ✅ 推荐的安装方式

### 方式 1: 手动安装到 Claude Skills（最简单）

#### 步骤 1: 创建 Skills 目录

**Windows PowerShell**:
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills"
```

**macOS/Linux**:
```bash
mkdir -p ~/.claude/skills
```

#### 步骤 2: 下载技能文件

**选项 A: 克隆整个仓库**
```bash
cd ~/.claude/skills
git clone https://github.com/xdaicode/skills.git jsonl-converter
```

**选项 B: 只下载必要文件**

创建目录：
```bash
mkdir ~/.claude/skills/jsonl-converter
```

下载这两个文件到 `~/.claude/skills/jsonl-converter/`：
- `SKILL.md`
- `jsonl_converter.py`

直接从 GitHub 下载：
- https://github.com/xdaicode/skills/blob/main/SKILL.md
- https://github.com/xdaicode/skills/blob/main/jsonl_converter.py

#### 步骤 3: 验证安装

检查文件是否存在：
```bash
# Windows PowerShell
Get-ChildItem "$env:USERPROFILE\.claude\skills\jsonl-converter"

# macOS/Linux
ls ~/.claude/skills/jsonl-converter
```

应该看到：
- `SKILL.md`
- `jsonl_converter.py`

#### 步骤 4: 重启 Claude Code

关闭并重新打开 Claude Code。

#### 步骤 5: 使用技能

在 Claude Code 中直接说：
```
请将 d:/AI/session.jsonl 转换为可读文档
```

---

### 方式 2: 作为 Python 工具使用（推荐给非 Claude Code 用户）

如果你不使用 Claude Code，可以直接作为 Python 工具使用：

```bash
# 克隆仓库
git clone https://github.com/xdaicode/skills.git
cd skills

# 直接运行
python jsonl_converter.py your_file.jsonl

# 或安装为 Python 包
pip install -e .
python -m jsonl_converter your_file.jsonl
```

---

## 🔧 手动安装详解

### Windows 用户

1. **打开文件资源管理器**
   - 按 `Win + R`
   - 输入 `%USERPROFILE%\.claude\skills`
   - 如果目录不存在，创建它

2. **下载文件**
   - 访问 https://github.com/xdaicode/skills
   - 点击 `SKILL.md` → "Raw" → 另存为
   - 点击 `jsonl_converter.py` → "Raw" → 另存为
   - 保存到 `%USERPROFILE%\.claude\skills\` 目录

3. **重启 Claude Code**

### macOS/Linux 用户

```bash
# 1. 创建目录
mkdir -p ~/.claude/skills

# 2. 克隆仓库
cd ~/.claude/skills
git clone https://github.com/xdaicode/skills.git jsonl-converter

# 3. 重启 Claude Code
```

---

## ❌ 为什么 `/plugin marketplace add` 不工作？

### 原因

Claude Code 的插件市场需要特殊的仓库结构：

```
xdaicode/skills (仓库根目录)
├── skills/              # 必需
│   ├── jsonl-converter/
│   │   ├── SKILL.md
│   │   └── jsonl_converter.py
├── marketplace.json     # 必需 - 插件市场描述文件
└── MANIFEST.md          # 必需 - 技能清单
```

**当前仓库缺少**：
- ❌ `marketplace.json`
- ❌ `MANIFEST.md`
- ❌ `skills/` 子目录结构

### 解决方案

有两个选择：

**选项 A: 重组仓库为插件市场格式**
- 创建正确的目录结构
- 添加 `marketplace.json` 和 `MANIFEST.md`
- 重新组织文件

**选项 B: 保持当前结构，使用手动安装**
- 用户直接克隆到 `~/.claude/skills/`
- 简单直接，无需额外配置

---

## 🎯 当前推荐的安装方法

### 对于 Claude Code 用户

**手动安装（推荐）**：
```bash
cd ~/.claude/skills
git clone https://github.com/xdaicode/skills.git jsonl-converter
```

然后重启 Claude Code 即可使用。

### 对于命令行用户

**直接使用**：
```bash
git clone https://github.com/xdaicode/skills.git
cd skills
python jsonl_converter.py your_file.jsonl
```

---

## 📝 验证清单

安装完成后，检查以下内容：

- [ ] `~/.claude/skills/jsonl-converter/SKILL.md` 存在
- [ ] `~/.claude/skills/jsonl-converter/jsonl_converter.py` 存在
- [ ] 重启了 Claude Code
- [ ] 在 Claude Code 中测试：`请转换一个文件`
- [ ] 转换成功生成 `.md` 文件

---

## 🆘 故障排除

### 问题 1: Claude 找不到技能

**检查**：
```bash
ls ~/.claude/skills/jsonl-converter/
```

**应该看到**：
```
SKILL.md
jsonl_converter.py
```

### 问题 2: 技能加载失败

**解决**：
1. 确认 `SKILL.md` 格式正确
2. 检查文件编码是 UTF-8
3. 重启 Claude Code

### 问题 3: Python 脚本无法运行

**测试**：
```bash
python ~/.claude/skills/jsonl-converter/jsonl_converter.py test.jsonl
```

---

## 📖 参考资源

- [Claude Skills 官方仓库](https://github.com/anthropics/skills)
- [Claude Code 文档](https://code.claude.com/docs)
- [技能创建最佳实践](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

---

## 🎉 快速开始（最简单）

```bash
# 一行命令安装（推荐）
cd ~/.claude/skills && git clone https://github.com/xdaicode/skills.git jsonl-converter

# 重启 Claude Code

# 在 Claude Code 中使用
# 请将 d:/AI/your_file.jsonl 转换为可读文档
```

---

**注意**：如果想要支持 `/plugin marketplace add` 安装，需要重组仓库结构。是否需要我帮你创建符合插件市场规范的版本？
