# Python程序设计 第二次作业 第2题
# 文件名：homework2_2.py
# 题目：实现梯度下降算法（25分）
# 只需补全 gradient_descent，下面的测试与输出代码已经提供。


def gradient_descent(start_x, learning_rate, tolerance=1e-6, max_iter=100):
    # TODO: 初始化当前位置和更新次数
    x = start_x
    update = 0
    # TODO: 按题目步骤检查精度、检查次数、更新位置
    while True:
        if abs(2 * (x - 3)) < tolerance:
            return x, update, True
        else:
            if update == max_iter:
                return x, update, False
            else:
                x = x - learning_rate * 2 * (x - 3)
                update += 1
    # TODO: 返回 (最终位置, 更新次数, 是否达到精度)
    pass


# 以下为提供的测试代码，请保留，不需要修改。
# expected_x、expected_steps、expected_success 是对应的预期结果。
test_cases = [
    ("学习率0.1", 0.0, 0.1, 100, 3.0, 70, True),
    ("学习率0.5", 0.0, 0.5, 100, 3.0, 1, True),
    ("学习率0.9", 0.0, 0.9, 100, 3.0, 70, True),
    ("学习率1.0", 0.0, 1.0, 100, 0.0, 100, False),
    ("学习率1.1", 0.0, 1.1, 100, -248453920.566047, 100, False),
    ("起点已达精度", 3.0, 0.1, 100, 3.0, 0, True),
    ("不允许更新", 0.0, 0.1, 0, 0.0, 0, False),
    ("最后一次更新达标", 0.0, 0.5, 1, 3.0, 1, True),
]

passed_count = 0
for name, start_x, lr, max_iter, expected_x, expected_steps, expected_success in test_cases:
    result = gradient_descent(start_x, lr, tolerance=1e-6, max_iter=max_iter)
    print(f"测试：{name}")
    # 未补全函数或返回格式有误时，给出提示，继续下一项测试。
    if not isinstance(result, tuple) or len(result) != 3:
        print("测试结果：未通过（请返回三个值：最终位置、更新次数、是否达到精度）")
        print()
        continue

    x, steps, success = result
    valid_types = (
        type(x) in (int, float)
        and type(steps) is int
        and type(success) is bool
    )
    if not valid_types:
        print("测试结果：未通过（返回值类型应为数值、整数、布尔值）")
        print()
        continue

    # 最终位置允许浮点误差；大数使用相对误差，小数使用绝对误差。
    allowed_error = max(1e-6, abs(expected_x) * 1e-10)
    passed = (
        abs(x - expected_x) <= allowed_error
        and steps == expected_steps
        and success == expected_success
        and success == (abs(2 * (x - 3)) < 1e-6)
    )
    print(f"最终位置：{x:.6f}")
    print(f"迭代次数：{steps}")
    print(f"优化状态：{'达到精度' if success else '未达到精度'}")
    print(f"测试结果：{'通过' if passed else '未通过'}")
    print()
    if passed:
        passed_count += 1

print(f"通过测试：{passed_count}/{len(test_cases)}")