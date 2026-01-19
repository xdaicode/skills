"""
Setup configuration for Claude JSONL Converter
"""
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="claude-jsonl-converter",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Convert Claude AI JSONL session logs to readable Markdown",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/claude-jsonl-converter",
    py_modules=["jsonl_converter"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Natural Language :: Chinese",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "jsonl2md=jsonl_converter:main",
            "claude-jsonl=jsonl_converter:main",
        ],
    },
    keywords="claude jsonl markdown converter ai logs session",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/claude-jsonl-converter/issues",
        "Source": "https://github.com/yourusername/claude-jsonl-converter",
        "Documentation": "https://github.com/yourusername/claude-jsonl-converter/blob/main/README.md",
    },
)
