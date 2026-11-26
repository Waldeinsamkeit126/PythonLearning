# Python程序设计 第一次作业 第1题
# 文件名：homework1_1.py

# 题目：打印课程名片
# 要求：输入姓名、学号、课程名称和目标分数，按题目要求输出课程名片。

# TODO: 使用 input() 依次输入姓名、学号、课程名称和目标分数
# 提示：目标分数需要转换为 float 类型

# TODO: 按照题目要求输出 8 行内容
# 提示：目标分数保留 1 位小数，可以使用 f-string 格式控制

name = input("INPUT YOUR NAME:")
ID = input("INPUT YOUR ID:")
course = input("INPUT YOUR COURSE:")
score = float(input("INPUT YOUR SCORE:"))

print("=" * 30)
print("| 课程学习名片 |")
print("=" * 30)
print(f"| 姓名：{name}")
print(f"| 学号：{ID}")
print(f"| 课程：{course}")
print(f"| 目标分数：{score:.1f} 分")
print("=" * 30)