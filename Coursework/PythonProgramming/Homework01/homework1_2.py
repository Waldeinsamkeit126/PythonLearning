# Python程序设计 第一次作业 第2题
# 文件名：homework1_2.py

# 题目：快递费用计算
# 要求：输入包裹重量，按收费规则计算并输出快递费。

# TODO: 使用 input() 输入包裹重量 weight
# 提示：重量需要转换为 float 类型

# TODO: 判断重量是否有效

# TODO: 根据不同重量区间计算快递费

# TODO: 按题目要求输出结果
# 提示：有效重量的快递费需要保留 2 位小数

weight=int(input())
if weight>0 and weight<=1:
    print(f"快递费：8 元")
elif weight <= 3:
    print(f"快递费：12 元")
elif weight <= 10:
    print(f"快递费：{12 + (weight - 3) * 2}元")
elif weight >10 :    
    print(f"快递费：{26 + (weight - 10) * 3}元")
else:
    print(f"重量无效")