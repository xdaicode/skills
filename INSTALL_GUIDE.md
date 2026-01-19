# Claude Code 手动安装步骤（图文指南）

## 🎯 安装目标

将 JSONL 转换器安装到 Claude Code，让你可以直接说：
```
请将 d:/AI/session.jsonl 转换为可读文档
```

---

## 📋 安装步骤

### 步骤 1: 打开 Claude Skills 目录

#### Windows 用户

1. **打开文件资源管理器**
2. **在地址栏输入**：
   ```
   %USERPROFILE%\.claude\skills
   ```
3. **按回车**

如果提示目录不存在，需要先创建：
- 在文件资源管理器中右键 → "新建" → "文件夹"
- 命名为：`.claude`
- 进入 `.claude`，新建文件夹 `skills`

#### 或使用命令行创建

**PowerShell**:
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills"
```

**CMD**:
```cmd
mkdir "%USERPROFILE%\.claude\skills"
```

#### macOS/Linux 用户

打开终端，运行：
```bash
mkdir -p ~/.claude/skills
cd ~/.claude/skills
```

---

### 步骤 2: 下载技能文件

#### 方法 A: 使用 Git（推荐，最简单）

1. **打开终端/命令行**
2. **进入 skills 目录**：
   ```bash
   cd ~/.claude/skills
   ```
   或 Windows PowerShell:
   ```powershell
   cd $env:USERPROFILE\.claude\skills
   ```

3. **克隆仓库**：
   ```bash
   git clone https://github.com/xdaicode/skills.git jsonl-converter
   ```

4. **等待下载完成**

完成后，你应该看到：
```
~/.claude/skills/jsonl-converter/
├── SKILL.md
├── jsonl_converter.py
├── README.md
└── ...其他文件
```

#### 方法 B: 手动下载（如果没有 Git）

1. **访问 GitHub**：
   https://github.com/xdaicode/skills

2. **下载这两个文件**：
   - 点击 `SKILL.md` → 右上角 "Raw" → 右键 "另存为"
   - 点击 `jsonl_converter.py` → 右上角 "Raw" → 右键 "另存为"

3. **保存到**：
   - Windows: `C:\Users\你的用户名\.claude\skills\jsonl-converter\`
   - macOS/Linux: `~/.claude/skills/jsonl-converter/`

   （需要先创建 `jsonl-converter` 子目录）

---

### 步骤 3: 验证文件

#### 检查文件是否存在

**Windows PowerShell**:
```powershell
Get-ChildItem "$env:USERPROFILE\.claude\skills\jsonl-converter"
```

**macOS/Linux 终端**:
```bash
ls ~/.claude/skills/jsonl-converter
```

**应该看到**：
```
SKILL.md
jsonl_converter.py
README.md
LICENSE
...
```

**最少需要**：
- ✅ `SKILL.md`
- ✅ `jsonl_converter.py`

---

### 步骤 4: 重启 Claude Code

1. **完全关闭 Claude Code**（不是最小化）
2. **重新打开 Claude Code**

这样 Claude Code 才能加载新安装的技能。

---

### 步骤 5: 测试技能

在 Claude Code 的聊天框中输入：

```
请将 d:/AI/agent-aa4105a.jsonl 转换为可读文档
```

或者如果有其他 JSONL 文件：

```
请将 [你的文件路径].jsonl 转换为可读文档
```

**预期结果**：
- Claude 会自动识别并使用这个技能
- 生成一个 `*_readable.md` 文件
- 告诉你转换成功

---

## ❌ 常见问题

### 问题 1: Claude 说 "Unknown skill"

**原因**：文件没有放在正确的目录

**解决**：
1. 确认路径是 `~/.claude/skills/jsonl-converter/`
2. 检查 `SKILL.md` 和 `jsonl_converter.py` 都在这个目录里
3. 重启 Claude Code

### 问题 2: 技能加载但运行失败

**原因**：Python 路径问题

**解决**：
1. 确认 Python 已安装：`python --version`
2. 测试脚本：
   ```bash
   python ~/.claude/skills/jsonl-converter/jsonl_converter.py test.jsonl
   ```

### 问题 3: 找不到 .claude 目录

**解决**：手动创建
```bash
# Windows PowerShell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills"

# macOS/Linux
mkdir -p ~/.claude/skills
```

---

## 🔍 验证清单

安装完成后，逐项检查：

- [ ] `.claude/skills/jsonl-converter/` 目录存在
- [ ] `SKILL.md` 文件存在
- [ ] `jsonl_converter.py` 文件存在
- [ ] 已重启 Claude Code
- [ ] 在 Claude Code 中测试命令成功

---

## 📸 视觉指南（目录结构）

**你应该有如下结构**：

```
C:\Users\你的用户名\
└── .claude/
    └── skills/
        └── jsonl-converter/
            ├── SKILL.md              ⭐ 必需
            ├── jsonl_converter.py    ⭐ 必需
            ├── README.md
            ├── LICENSE
            └── ...其他文件
```

或者 macOS/Linux：

```
~/
└── .claude/
    └── skills/
        └── jsonl-converter/
            ├── SKILL.md
            ├── jsonl_converter.py
            └── ...
```

---

## 🚀 一键安装命令（推荐）

如果你有 Git，只需要运行这一条命令：

```bash
cd ~/.claude/skills && git clone https://github.com/xdaicode/skills.git jsonl-converter
```

然后重启 Claude Code 即可！

---

## 🎓 使用示例

安装成功后，在 Claude Code 中你可以：

### 基本转换
```
请将 d:/AI/session.jsonl 转换为可读文档
```

### 指定输出文件
```
将 d:/AI/input.jsonl 转换并保存到 d:/AI/output.md
```

### 批量处理
```
将 d:/AI/sessions/ 目录下所有 .jsonl 文件转换为可读文档
```

---

## 📞 需要帮助？

如果遇到问题：
1. 检查上面的"常见问题"部分
2. 在 GitHub 提 Issue：https://github.com/xdaicode/skills/issues
3. 提供你的操作系统和错误信息

---

## ✅ 快速回顾

**最少步骤**：

1. 打开终端/PowerShell
2. 运行：`cd ~/.claude/skills && git clone https://github.com/xdaicode/skills.git jsonl-converter`
3. 重启 Claude Code
4. 在 Claude Code 中说：`请将文件.jsonl 转换为可读文档`

**完成！** 🎉
