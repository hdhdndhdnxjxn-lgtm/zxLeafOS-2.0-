#!/usr/bin/env python3
"""
zxLeafOS2.0正式版 02Engine HTML 解包工具
从 02Engine Packager 生成的 HTML 中提取项目源码，整理成 GitHub 仓库结构。

用法:
    python3 unpack.py <input.html> <output_dir>
"""

import re, sys, os, json, zipfile, struct, shutil
from pathlib import Path

def get_base85_value(code):
    if code == 0x28: code = 0x3c
    elif code == 0x29: code = 0x3e
    return code - 0x2a

def base85_decode(data):
    result = bytearray()
    for i in range(0, len(data) - 4, 5):
        v0 = get_base85_value(ord(data[i]))
        v1 = get_base85_value(ord(data[i + 1]))
        v2 = get_base85_value(ord(data[i + 2]))
        v3 = get_base85_value(ord(data[i + 3]))
        v4 = get_base85_value(ord(data[i + 4]))
        value = v4 * 85**4 + v3 * 85**3 + v2 * 85**2 + v1 * 85 + v0
        result.extend(struct.pack("<I", value & 0xFFFFFFFF))
    return bytes(result)

CHUNK_PATTERN = re.compile(
    r'<script\s+type="application/x-o2-project-chunk"\s+data-size="(\d+)"[^>]*>(.*?)</script>',
    re.DOTALL
)

def extract_project_zip(html_path):
    with open(html_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    matches = list(CHUNK_PATTERN.finditer(content))
    if not matches:
        raise ValueError("未在 HTML 中找到任何 project chunk")
    zip_data = bytearray()
    for m in matches:
        decoded = base85_decode(m.group(2))
        declared_size = int(m.group(1))
        if len(decoded) > declared_size:
            decoded = decoded[:declared_size]
        zip_data.extend(decoded)
    return bytes(zip_data)

def unpack_project(zip_data, output_dir):
    src_dir = os.path.join(output_dir, "src")
    os.makedirs(src_dir, exist_ok=True)
    zip_path = os.path.join(output_dir, "project.zip")
    with open(zip_path, "wb") as f:
        f.write(zip_data)
    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(src_dir)
    return src_dir

def main():
    if len(sys.argv) < 3:
        print("用法: python3 unpack.py <input.html> <output_dir>")
        sys.exit(1)
    html_path = sys.argv[1]
    output_dir = sys.argv[2]
    if not os.path.exists(html_path):
        print("错误: 文件不存在: " + html_path)
        sys.exit(1)
    zip_data = extract_project_zip(html_path)
    src_dir = unpack_project(zip_data, output_dir)
    print("解包完成: " + output_dir)
    print("源码目录: " + src_dir)

if __name__ == "__main__":
    main()