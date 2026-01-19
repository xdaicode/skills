# ⚡ 快速开始 - 3 分钟安装

## 🎯 最简单的安装方法

### 一行命令安装

打开终端/PowerShell，复制粘贴这条命令：

```bash
cd ~/.claude/skills && git clone https://github.com/xdaicode/skills.git jsonl-converter
```

**Windows 用户，如果在 PowerShell 中**：
```powershell
cd $env:USERPROFILE\.claude\skills; git clone https://github.com/xdaicode/skills.git jsonl-converter
```

### 重启 Claude Code

完全关闭并重新打开 Claude Code。

### 完成！

现在可以在 Claude Code 中使用：

```
请将 d:/AI/your_file.jsonl 转换为可读文档
```

---

## 📋 需要帮助？

查看完整安装指南：[INSTALL_GUIDE.md](INSTALL_GUIDE.md)

---

## ❌ 没有 Git？

### 手动下载步骤

1. **创建目录**：
   - Windows: 在文件资源管理器地址栏输入 `%USERPROFILE%\.claude\skills`
   - 新建文件夹 `jsonl-converter`

2. **下载文件**：
   - 访问 https://github.com/xdaicode/skills
   - 下载 `SKILL.md` 和 `jsonl_converter.py`
   - 保存到 `jsonl-converter` 文件夹

3. **重启 Claude Code**

---

## ✅ 验证安装

在 Claude Code 中输入：
```
列出所有可用的技能
```

应该看到 "JSONL 对话记录转换器" 或类似的技能名称。

---

## 🚀 立即测试

```
请将当前目录下的任意 .jsonl 文件转换为可读文档
```

或者如果你有示例文件：
```
请将 d:/AI/agent-aa4105a.jsonl 转换为可读文档
```

---

**就这么简单！** 🎉
