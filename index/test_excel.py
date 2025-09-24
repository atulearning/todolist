#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""测试 Excel 自动换行功能"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'todolist'))

from index.mathimage import create_task_excel

# 测试数据
test_tasks = [
    {"description": "这是一个很长的任务描述，用来测试自动换行功能是否正常工作，如果文字太长应该会自动换行显示", "status": "未完成"},
    {"description": "短任务", "status": "已完成"},
    {"description": "另一个非常长的任务描述，包含很多文字内容，用来验证 Excel 单元格的自动换行和行高调整功能是否正常", "status": "未完成"},
    {"description": "普通长度的任务描述", "status": "已完成"},
]

def test_excel_generation():
    """测试 Excel 文件生成"""
    print("正在生成测试 Excel 文件...")
    
    # 生成到文件
    filename = create_task_excel(test_tasks, "test_task_list.xlsx", save_to_memory=False)
    print(f"Excel 文件已生成: {filename}")
    
    # 生成到内存
    excel_data = create_task_excel(test_tasks, save_to_memory=True)
    print(f"内存中的 Excel 数据大小: {len(excel_data)} 字节")
    
    # 保存内存数据到文件用于检查
    test_memory_file = "test_memory_excel.xlsx"
    with open(test_memory_file, 'wb') as f:
        f.write(excel_data)
    print(f"内存中的 Excel 数据已保存到: {test_memory_file}")
    
    print("\n测试完成！请检查生成的 Excel 文件：")
    print(f"1. {filename} - 直接保存到文件的版本")
    print(f"2. {test_memory_file} - 内存生成后保存的版本")
    print("\n请打开这两个文件检查以下内容：")
    print("- 任务描述列是否自动换行")
    print("- 行高是否适当增加")
    print("- 长文本是否完整显示")

if __name__ == "__main__":
    test_excel_generation()