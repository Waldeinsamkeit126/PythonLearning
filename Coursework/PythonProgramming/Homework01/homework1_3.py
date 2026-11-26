# Python程序设计 第一次作业 第3题
# 文件名：homework1_3.py

# 题目：手机套餐账单
# 要求：输入本月使用流量和通话时长，计算套餐外费用。

# TODO: 使用 input() 输入本月流量 data 和通话时长 minutes
# 提示：流量可以转换为 float，通话时长可以转换为 float 或 int

# TODO: 判断输入是否有效

# TODO: 计算流量超出费用

# TODO: 计算通话超出费用

# TODO: 计算套餐外总费用

# TODO: 按题目要求输出结果
# 提示：三项费用都需要保留 2 位小数

data = float(input())
Dmoney = 0
Mmoney = 0
minutes = float(input())
if data < 0 or minutes < 0:
    print("输入无效")
else:
    if data <= 10:
        feedata = 0.0
    else:
        feedata = (data - 10) * 5
    if minutes < 100:
        feemin = 0.0
    else:
        feemin = (minutes - 100) * 0.2
    feesum = feedata + feemin
print(f"流量超出费用：{feedata:.2f} 元")
print(f"通话超出费用：{feemin:.2f} 元")
print(f"套餐外总费用：{feesum:.2f} 元")
