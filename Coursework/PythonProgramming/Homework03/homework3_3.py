# Python程序设计 第三次作业 第3题（50分）
# 只补全三个函数，保留路径、测试与输出代码，不修改原始数据。
# 不得添加模板之外的库；使用字符串方法解析CSV，按题目公式计算。


def read_experiments(path):
    result = {}
    # TODO: 使用with和open，以UTF-8读取文件，跳过表头和空行
    with open(path, "r", encoding='utf-8') as f:
        next(f)
    # TODO: 拆分字段、去除两侧空白，将准确率转换为float
        for line in f:
            line = line.strip()
            if line == "":
                continue
            dics = [item.strip() for item in line.split(",")]
            model = dics[1]
            accuracy = float(dics[3])
            if model not in result:
                result[model] = []
            result[model].append(accuracy)
    # TODO: 返回{模型名称: [准确率, ...]}
    return result
    pass


def calculate_statistics(results):
    models = {}
    # TODO: 计算每种模型的实验次数、平均值和标准差（分母为n）
    for model, values in results.items():
        count = len(values)
        mean = sum(values) / count
        std = (sum((x - mean) ** 2 for x in values) / count) ** 0.5
        models[model] = {
            "count": count,
            "mean": mean,
            "std": std
        }
    # TODO: 返回{模型名称: {"count": 次数, "mean": 平均值, "std": 标准差}}
    return models
    # TODO: 不修改输入字典，空输入返回{}
    pass


def write_report(path, statistics):
    # TODO: 使用with和open，以UTF-8覆盖写入报告
    with open(path, "w", encoding="utf-8") as f:
        f.write("model,count,mean,std\n")
        for model in sorted(statistics):
            count = statistics[model]["count"]
            mean = statistics[model]["mean"]
            std = statistics[model]["std"]
            f.write(f"{model},{count},{mean:.4f},{std:.4f}\n")
            
    # TODO: 写出表头，按模型名升序写出数据，mean和std保留四位小数
    # 本函数不需要返回值
    pass


# 以下为提供的路径、调用及检查代码，请保留，不需要修改。
from pathlib import Path
from tempfile import TemporaryDirectory

base_dir = Path(__file__).resolve().parent
expected_results = {
    "Model_A": [82.0, 84.0, 84.0, 86.0],
    "Model_B": [87.0, 88.0, 88.0, 89.0],
    "Model_C": [84.0, 90.0, 90.0, 96.0],
}
expected_stats = {
    "Model_A": {"count": 4, "mean": 84.0, "std": 2 ** 0.5},
    "Model_B": {"count": 4, "mean": 88.0, "std": 0.5 ** 0.5},
    "Model_C": {"count": 4, "mean": 90.0, "std": 18 ** 0.5},
}
expected_lines = ["model,count,mean,std", "Model_A,4,84.0000,1.4142",
                  "Model_B,4,88.0000,0.7071", "Model_C,4,90.0000,4.2426"]


def stats_equal(actual, expected):
    if not isinstance(actual, dict) or actual.keys() != expected.keys():
        return False
    for model, values in expected.items():
        row = actual[model]
        if not isinstance(row, dict) or row.keys() != values.keys():
            return False
        for key, value in values.items():
            if not isinstance(row[key], (int, float)) or abs(row[key] - value) > 1e-9:
                return False
    return True


passed_count = 0

def check(label, passed):
    global passed_count
    passed_count += int(passed)
    print(f"{label}：{'通过' if passed else '未通过'}")


check("读取分组", read_experiments(base_dir / "data" / "experiments.csv") == expected_results)
inputs = {key: values[:] for key, values in expected_results.items()}
actual = calculate_statistics(inputs)
check("统计计算", stats_equal(actual, expected_stats) and inputs == expected_results)

with TemporaryDirectory() as temp_dir:
    folder = Path(temp_dir)
    output = folder / "summary.csv"
    write_report(output, dict(reversed(list(expected_stats.items()))))
    check("报告写入", output.exists() and output.read_text(encoding="utf-8").splitlines() == expected_lines)

    source = folder / "experiments.csv"
    source.write_text("experiment_id,model,seed,accuracy\n", encoding="utf-8")
    check("空文件分组", read_experiments(source) == {})
    check("空统计", calculate_statistics({}) == {})
    empty_output = folder / "empty.csv"
    write_report(empty_output, {})
    check("空报告", empty_output.exists() and empty_output.read_text(encoding="utf-8").splitlines() == [expected_lines[0]])

    source.write_text("experiment_id,model,seed,accuracy\n\nE1, Model_X ,1, 80.0 \n  \nE2,Model_Y,2,90\nE3,Model_Y,3,90\n", encoding="utf-8")
    check("空白与分组", read_experiments(source) == {"Model_X": [80.0], "Model_Y": [90.0, 90.0]})
    check("不同次数与零波动", stats_equal(calculate_statistics({"Model_X": [80.0], "Model_Y": [90.0, 90.0]}), {
        "Model_X": {"count": 1, "mean": 80.0, "std": 0.0},
        "Model_Y": {"count": 2, "mean": 90.0, "std": 0.0}}))

print(f"通过测试：{passed_count}/8")
if passed_count == 8:
    results = read_experiments(base_dir / "data" / "experiments.csv")
    statistics = calculate_statistics(results)
    report = base_dir / "summary.csv"
    write_report(report, statistics)
    passed = report.exists() and report.read_text(encoding="utf-8").splitlines() == expected_lines
    print(f"完整流程：{'通过' if passed else '未通过'}")
    if passed:
        print("报告已生成：summary.csv")
