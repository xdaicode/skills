---
name: jsonl-converter
description: Convert Claude AI JSONL session logs to readable Markdown documents. Use when you need to extract, read, or share Claude conversation history from .jsonl files.
---

# JSONL 对话记录转换器

将 Claude 的 JSONL 格式对话记录转换为可读性 Markdown 文档。

## 使用场景

当你有一个 Claude AI Agent 的会话日志文件（.jsonl 格式），需要将其转换为易于阅读和分享的 Markdown 文档时使用此技能。

## 输入要求

- 一个 `.jsonl` 格式的 Claude 对话记录文件
- 文件包含 JSON 格式的对话消息，每行一个 JSON 对象

## 功能特性

1. **提取完整对话内容**：解析所有用户和助手的消息
2. **格式化输出**：将紧凑的 JSON 转换为易读的 Markdown 格式
3. **保留关键信息**：
   - 时间戳
   - 消息类型（用户/助手）
   - 完整的文本内容
   - 工具调用信息（简化显示）
4. **智能截断**：对超长消息进行适当截断，保持文档可读性
5. **UTF-8 编码支持**：正确处理中文和特殊字符

## 输出

生成一个 `.md` 文档，包含：
- 会话元信息（Session ID、Agent 信息、消息总数）
- 按时间顺序排列的所有对话
- 清晰的标题和分隔线
- 可点击的文件链接（在支持的编辑器中）

## 使用方法

提供 JSONL 文件路径，例如：
```
请将 d:/AI/agent-xxx.jsonl 转换为可读文档
```

## 技术实现

使用 Python 解析 JSONL 文件：
- 逐行读取 JSON 对象
- 提取 timestamp、type、message 字段
- 处理嵌套的 content 结构（text、tool_use、tool_result）
- 格式化为 Markdown 并输出到新文件

## 示例

输入：
```
d:/AI/agent-aa4105a.jsonl
```

输出：
```
d:/AI/agent-aa4105a_readable.md
```

生成的文档结构：
```markdown
# AI Agent Session Log

**Session ID**: aa4105a
**Agent Slug**: optimized-gathering-rocket
**Total Messages**: 106

---

## [1] USER
**Time**: 2026-01-18 10:06:28

**Content**:
请详细探索 Yoshop 项目的运行环境要求...

---

## [2] ASSISTANT
**Time**: 2026-01-18 10:06:30

**Content**:
我将详细探索 Yoshop 项目的运行环境要求...
```
