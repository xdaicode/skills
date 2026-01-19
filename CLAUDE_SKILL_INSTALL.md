# Claude Skill 安装指南

## 🎯 快速安装（3 种方式）

### 方式 1: 使用 Claude Code 插件市场（最简单）

在 Claude Code 中运行：

```bash
/plugin marketplace add xdaicode/skills
```

或者直接安装：

```bash
/plugin install jsonl-converter@xdaicode/skills
```

安装后，直接告诉 Claude：
```
请将 d:/AI/session.jsonl 转换为可读文档
```

### 方式 2: 手动安装到 Claude Skills 目录

#### 1. 找到 Claude Skills 目录

**Windows**:
```
C:\Users\你的用户名\.claude\skills\
```

**macOS/Linux**:
```
~/.claude/skills/
```

如果目录不存在，创建它：
```bash
# Windows PowerShell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills"

# macOS/Linux
mkdir -p ~/.claude/skills
```

#### 2. 复制技能文件

将以下文件复制到 `skills` 目录：

**需要的文件**：
- `SKILL.md` （技能定义文件）
- `jsonl_converter.py` （Python 脚本）

**复制命令**：
```bash
# Windows PowerShell
Copy-Item "SKILL.md" "$env:USERPROFILE\.claude\skills\jsonl-converter\"
Copy-Item "jsonl_converter.py" "$env:USERPROFILE\.claude\skills\jsonl-converter\"

# macOS/Linux
mkdir -p ~/.claude/skills/jsonl-converter
cp SKILL.md ~/.claude/skills/jsonl-converter/
cp jsonl_converter.py ~/.claude/skills/jsonl-converter/
```

#### 3. 重启 Claude Code

关闭并重新打开 Claude Code，技能会自动加载。

#### 4. 使用技能

在 Claude Code 中直接说：
```
请将 d:/AI/session.jsonl 转换为可读文档
```

### 方式 3: 从 GitHub 直接安装（推荐）

```bash
# 克隆仓库到 skills 目录
cd ~/.claude/skills  # 或 Windows: cd $env:USERPROFILE\.claude\skills
git clone https://github.com/xdaicode/skills.git jsonl-converter

# 重启 Claude Code
```

---

## ✅ 验证安装

在 Claude Code 中运行：

```
列出所有可用的技能
```

或

```
/skill list
```

你应该看到 `jsonl-converter` 或 `JSONL 对话记录转换器` 出现在列表中。

---

## 🚀 使用示例

安装完成后，在 Claude Code 中：

### 基本转换
```
请将 d:/AI/agent-session.jsonl 转换为可读文档
```

### 指定输出文件
```
将 d:/AI/input.jsonl 转换为 Markdown 并保存到 d:/AI/output.md
```

### 批量转换
```
将 d:/AI/sessions/ 目录下所有 .jsonl 文件转换为可读文档
```

---

## 🔧 技能文件结构

```
~/.claude/skills/jsonl-converter/
├── SKILL.md                 # 技能定义（Claude 读取这个文件）
├── jsonl_converter.py      # Python 脚本
├── README.md               # 完整文档
└── LICENSE                 # MIT 许可证
```

---

## 📝 SKILL.md 文件格式

Claude 会读取 `SKILL.md` 的开头部分：

```markdown
# 技能名称

简短描述，告诉 Claude 这个技能做什么。

## 使用场景

什么时候使用这个技能。

## 功能特性

- 特性 1
- 特性 2

## 使用方法

如何调用这个技能。
```

---

## 🐛 故障排除

### 问题 1: Claude 找不到技能

**解决方案**：
1. 确认文件在正确的目录：`~/.claude/skills/`
2. 检查文件名是 `SKILL.md`（全大写）
3. 重启 Claude Code
4. 检查文件格式（UTF-8 编码）

### 问题 2: 技能加载失败

**解决方案**：
1. 检查 `SKILL.md` 格式是否正确
2. 确认 YAML frontmatter 格式：
```markdown
---
name: skill-name
description: Skill description
---
```

3. 查看 Claude Code 日志：
```bash
# 查看 Claude Code 日志
cat ~/.claude/logs/latest.log
```

### 问题 3: Python 脚本无法执行

**解决方案**：
1. 确认 Python 3.7+ 已安装：
```bash
python --version
```

2. 测试脚本：
```bash
python ~/.claude/skills/jsonl-converter/jsonl_converter.py test.jsonl
```

3. 检查文件权限：
```bash
chmod +x ~/.claude/skills/jsonl-converter/jsonl_converter.py
```

---

## 📚 更多资源

- [Claude Skills 官方文档](https://github.com/anthropics/skills)
- [Claude Code 完整指南](https://code.claude.com/docs)
- [技能创建最佳实践](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

---

## 🎓 从技能仓库安装（高级用户）

如果你维护自己的技能仓库：

### 1. 创建技能仓库结构

```
your-skills/
├── skills/
│   ├── jsonl-converter/
│   │   ├── SKILL.md
│   │   └── jsonl_converter.py
│   └── other-skill/
│       └── SKILL.md
├── MANIFEST.md
└── README.md
```

### 2. 在 Claude Code 中注册

```bash
/plugin marketplace add yourusername/your-skills
```

### 3. 安装技能

```bash
/plugin install jsonl-converter@your-skills
```

---

## ⚡ 快速命令参考

```bash
# 查看所有技能
/skill list

# 安装技能
/plugin install jsonl-converter@xdaicode/skills

# 卸载技能
/plugin uninstall jsonl-converter

# 更新技能
/plugin update jsonl-converter

# 查看技能市场
/plugin marketplace browse
```

---

## 🤝 贡献

如果你改进了这个技能，欢迎提交 PR！

---

**安装遇到问题？** 请在 GitHub 提 Issue：https://github.com/xdaicode/skills/issues
