# Python程序设计 第一次作业 第4题
# 文件名：homework1_4.py

# 题目：电影票价格判断
# 要求：输入年龄、是否学生、是否周末，计算电影票价格。

# TODO: 使用 input() 依次输入年龄、是否学生、是否周末
# 提示：年龄需要转换为 int 类型
# 提示：是否学生和是否周末输入 yes 或 no

# TODO: 判断年龄是否有效

# TODO: 根据年龄确定基础票价

# TODO: 根据是否学生判断是否减价

# TODO: 根据是否周末判断是否加价

# TODO: 按题目要求输出结果
# 提示：电影票价格需要保留 2 位小数

age = int(input())
is_stu = input()
is_wee = input()

if age < 0 or age > 120:
    print(f"年龄无效")
elif age < 6:
    fee = 0.0
elif age <= 17:
    fee = 25
elif age <= 59:
    fee = 40
elif age >= 60:
    fee = 20
if is_stu == "yes" and age >= 18 and age <= 25:
    fee = fee - 10
if is_wee == "yes" and fee != 0:
    fee += 5
print(f"电影票价格：{fee:.2f} 元")