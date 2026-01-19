#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JSONL to Readable Document Converter
将 Claude JSONL 格式的对话记录转换为可读的 Markdown 文档

使用方法：
    python jsonl_converter.py <jsonl_file_path> [output_file_path]

示例：
    python jsonl_converter.py d:/AI/agent-aa4105a.jsonl
    python jsonl_converter.py d:/AI/agent-aa4105a.jsonl d:/AI/output.md
"""

import json
import sys
import io
from datetime import datetime
from pathlib import Path

# 设置标准输出为 UTF-8 编码（修复 Windows 控制台问题）
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def extract_content(msg):
    """从消息中提取可读内容"""
    if isinstance(msg, str):
        return msg
    elif isinstance(msg, dict):
        role = msg.get('role', '')
        content = msg.get('content', '')

        if isinstance(content, list):
            # 处理 content blocks
            texts = []
            for item in content:
                if isinstance(item, dict):
                    item_type = item.get('type', '')

                    if item_type == 'text':
                        texts.append(item.get('text', ''))

                    elif item_type == 'tool_use':
                        name = item.get('name', '')
                        inputs = item.get('input', {})
                        # 简化工具调用显示
                        if isinstance(inputs, dict):
                            file_path = inputs.get('file_path', '')
                            if file_path:
                                texts.append(f'[调用工具: {name} - {file_path}]')
                            else:
                                texts.append(f'[调用工具: {name}]')
                        else:
                            texts.append(f'[调用工具: {name}]')

                    elif item_type == 'tool_result':
                        result_content = item.get('content', '')
                        is_error = item.get('is_error', False)

                        # 截断过长的工具结果
                        if len(result_content) > 500:
                            result_content = result_content[:500] + '...[截断]'

                        if is_error:
                            texts.append(f'[错误: {result_content}]')
                        else:
                            # 只显示非空结果的前 200 字符
                            if result_content and result_content.strip():
                                preview = result_content[:200] + '...' if len(result_content) > 200 else result_content
                                texts.append(f'[结果: {preview}]')

                elif isinstance(item, str):
                    texts.append(item)

            return ' '.join(texts) if texts else '[空消息]'

        return str(content) if content else '[空内容]'

    return ''


def format_timestamp(ts):
    """格式化时间戳"""
    try:
        # 处理 ISO 8601 格式
        dt = datetime.fromisoformat(ts.replace('Z', '+00:00'))
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    except:
        return ts


def convert_jsonl_to_markdown(jsonl_file_path, output_file_path=None):
    """将 JSONL 文件转换为 Markdown 文档"""

    input_path = Path(jsonl_file_path)

    if not input_path.exists():
        print(f"错误: 文件不存在 - {jsonl_file_path}")
        return False

    # 默认输出文件名
    if output_file_path is None:
        output_file_path = input_path.parent / f"{input_path.stem}_readable.md"
    else:
        output_file_path = Path(output_file_path)

    try:
        # 读取 JSONL 文件
        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if not lines:
            print(f"警告: 文件为空 - {jsonl_file_path}")
            return False

        # 解析第一行获取会话信息
        first_line_data = json.loads(lines[0])
        session_id = first_line_data.get('agentId', 'unknown')
        agent_slug = first_line_data.get('slug', 'unknown')
        cwd = first_line_data.get('cwd', '')

        # 构建 Markdown 内容
        md_lines = []

        # 标题和元信息
        md_lines.append('# AI Agent Session Log\n')
        md_lines.append(f'**Session ID**: {session_id}\n')
        if agent_slug != 'unknown':
            md_lines.append(f'**Agent Slug**: {agent_slug}\n')
        if cwd:
            md_lines.append(f'**Working Directory**: {cwd}\n')
        md_lines.append(f'**Total Messages**: {len(lines)}\n')
        md_lines.append('---\n')

        # 处理每条消息
        for i, line in enumerate(lines):
            try:
                data = json.loads(line)
                ts = format_timestamp(data.get('timestamp', ''))
                msg_type = data.get('type', 'unknown').upper()
                message = data.get('message', {})

                # 跳过纯工具调用消息（减少噪音）
                if isinstance(message, dict):
                    content = message.get('content', [])
                    if isinstance(content, list) and len(content) == 1:
                        if content[0].get('type') == 'tool_use':
                            continue

                md_lines.append(f'## [{i+1}] {msg_type}')
                md_lines.append(f'**Time**: {ts}\n')

                # 提取并格式化内容
                content_text = extract_content(message)

                if content_text and content_text.strip():
                    # 清理并限制内容长度
                    content_text = content_text.strip()

                    # 对于非常长的消息（如最终总结），保留完整内容
                    # 对于中间过程消息，适当截断
                    if len(content_text) > 10000 and i < len(lines) - 1:
                        content_text = content_text[:10000] + '\n\n...[内容过长，已截断]...'

                    md_lines.append(f'**Content**:\n{content_text}\n')

                md_lines.append('---\n')

            except json.JSONDecodeError as e:
                md_lines.append(f'Error parsing line {i+1}: {e}\n')
                md_lines.append('---\n')
            except Exception as e:
                md_lines.append(f'Unexpected error at line {i+1}: {e}\n')
                md_lines.append('---\n')

        # 写入输出文件
        output = '\n'.join(md_lines)

        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(output)

        print(f'✓ 成功转换文件:')
        print(f'  输入: {jsonl_file_path}')
        print(f'  输出: {output_file_path}')
        print(f'  消息数: {len(lines)}')
        print(f'  文档大小: {len(output)} 字符')

        return True

    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print(__doc__)
        print("\n错误: 请提供 JSONL 文件路径")
        print("使用方法:")
        print("  python jsonl_converter.py <jsonl_file_path> [output_file_path]")
        sys.exit(1)

    jsonl_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    success = convert_jsonl_to_markdown(jsonl_file, output_file)
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
