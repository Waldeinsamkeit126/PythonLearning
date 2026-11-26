# Python程序设计 第二次作业 第1题
# 文件名：homework2_1.py
# 题目：货物装载——暴力枚举求解多重背包（25分）
# A：单件体积6，单件价值13，可用数量2
# B：单件体积5，单件价值11，可用数量3
# C：单件体积3，单件价值7，可用数量4
# 只需补全best_loading，输入、测试和输出代码已经提供。


def best_loading(capacity):
    # capacity保证为0～20的整数，函数内部不需要input或print。
    # TODO: 初始化最高总价值及对应的三种货物数量
    Hval = 0
    Anum = Bnum = Cnum = 0
    # TODO: 使用三重for循环枚举数量，注意库存上限
    for i in range(3):
        for j in range(4):
            for k in range(5):
                volume = 6 * i + 5 * j + 3 * k
                val = 13 * i + 11 * j + 7 * k
    # TODO: 检查总体积，比较有效方案的总价值并保存最优数量
                if volume <= capacity and val >= Hval:
                    Hval = val
                    Anum = i
                    Bnum = j
                    Cnum = k
    # TODO: 依次返回A、B、C的数量，即return best_a, best_b, best_c
    return Anum, Bnum, Cnum
    pass


# 以下为提供的检查、输入与输出代码，请保留，不需要修改。
def check_result(capacity, result, expected_value=None):
    # 不限制并列最优方案的具体组合，只检查约束和最高价值。
    if not isinstance(result, tuple) or len(result) != 3:
        return False
    if not all(type(count) is int for count in result):
        return False
    count_a, count_b, count_c = result
    if not (0 <= count_a <= 2 and 0 <= count_b <= 3 and 0 <= count_c <= 4):
        return False
    volume = 6 * count_a + 5 * count_b + 3 * count_c
    value = 13 * count_a + 11 * count_b + 7 * count_c
    return volume <= capacity and (expected_value is None or value == expected_value)


test_cases = [(0, 0), (2, 0), (6, 14), (10, 22), (20, 45)]
passed_count = 0
for capacity, expected_value in test_cases:
    result = best_loading(capacity)
    passed = check_result(capacity, result, expected_value)
    print(f"测试：容量{capacity}立方米")
    print(f"测试结果：{'通过' if passed else '未通过'}")
    if passed:
        passed_count += 1
print(f"通过测试：{passed_count}/{len(test_cases)}")
print()

# 测试后输入一个容量，按统一格式显示装货方案。
print("请输入货厢容量（0～20的整数）：")
capacity = int(input())
if capacity < 0 or capacity > 20:
    print("容量无效")
else:
    result = best_loading(capacity)
    if not check_result(capacity, result):
        print("返回结果无效，请检查函数是否返回三个合法的整数数量")
    else:
        count_a, count_b, count_c = result
        volume = 6 * count_a + 5 * count_b + 3 * count_c
        value = 13 * count_a + 11 * count_b + 7 * count_c
        print(f"A货物：{count_a}件")
        print(f"B货物：{count_b}件")
        print(f"C货物：{count_c}件")
        print(f"总体积：{volume}立方米")
        print(f"剩余容量：{capacity - volume}立方米")
        print(f"总价值：{value}元")