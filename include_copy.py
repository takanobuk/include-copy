#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# include_copy.py
# HTMLファイル内の特定のコメントを処理し、ファイルをコピー
# <-- @include-file="ファイルパス" --> コメントを指定されたファイルの内容で置換
# <-- @date --> コメントを現在の日付（YYYYMMDDHHMM形式）で置換 
#
# 使い方: python include_copy.py <入力フォルダ> <出力フォルダ>
#
# Copyright(c) 2025 takanobuk
#

import os
import shutil
import re
from datetime import datetime

def process_html(src_path, dst_path, base_dir):
    include_pattern = re.compile(r'<!--\s*@include-file="([^"]+)"\s*-->')
    date_pattern = re.compile(r'<!--\s*@date\s*-->')

    print(f'Processing HTML: {src_path} -> {dst_path}')

    with open(src_path, encoding='utf-8') as f:
        content = f.read()

    def replace_include(match):
        include_file = match.group(1)
        include_file_path = os.path.join(base_dir, include_file)
        if os.path.exists(include_file_path):
            with open(include_file_path, encoding='utf-8') as incf:
                return incf.read()
        else:
            return f'<!-- ファイルが見つかりません: {include_file} {include_file_path} -->'

    def replace_date(match):
        current_date = datetime.now().strftime('%Y%m%d%H%M')
        return current_date

    # @include-fileの置換を実行
    new_content = include_pattern.sub(replace_include, content)
    
    # @dateの置換を実行
    new_content = date_pattern.sub(replace_date, new_content)

    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

def copy_files(src_dir, dst_dir):
    for root, dirs, files in os.walk(src_dir):
        rel_dir = os.path.relpath(root, src_dir)
        for file in files:
            src_path = os.path.join(root, file)
            dst_path = os.path.join(dst_dir, rel_dir, file)
            if file.endswith('.html'):
                #process_html(src_path, dst_path, root)
                process_html(src_path, dst_path, src_dir)
            else:
                os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                print(f'Copying file:    {src_path} -> {dst_path}')
                shutil.copy2(src_path, dst_path)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('使い方: python include_copy.py <入力フォルダ> <出力フォルダ>')
        exit(1)
    src_dir = sys.argv[1]
    dst_dir = sys.argv[2]
    copy_files(src_dir, dst_dir)