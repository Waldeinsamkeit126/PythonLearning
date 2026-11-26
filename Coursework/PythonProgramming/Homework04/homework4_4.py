"""第 4 题。搭建模型并更新参数，运行 python3 homework4_4.py。"""

from io import BytesIO
from math import exp, log
from pathlib import Path
from random import Random

from tempfile import TemporaryDirectory
from urllib.request import urlopen
from zipfile import BadZipFile, ZipFile

from homework4_1 import Linear
from homework4_2 import ReLU
from homework4_3 import Sequential


EPOCHS = 10
LEARNING_RATE = 0.025
SEED = 42
DATA_DIR = Path(__file__).resolve().parent
DATA_URL = (
    "https://archive.ics.uci.edu/static/public/80/"
    "optical+recognition+of+handwritten+digits.zip"
)
# Alpaydin & Kaynak (1998), Optical Recognition of Handwritten Digits.
# UCI Machine Learning Repository, https://doi.org/10.24432/C50P49
# CC BY 4.0, https://creativecommons.org/licenses/by/4.0/


def prepare_data():
    """复用脚本目录已有的数据文件，从 UCI 下载缺少的文件。"""
    train_path = DATA_DIR / "optdigits.tra"
    test_path = DATA_DIR / "optdigits.tes"
    missing = [path for path in (train_path, test_path) if not path.is_file()]
    if missing:
        print("正在下载 UCI 手写数字数据……", flush=True)
        try:
            with urlopen(DATA_URL, timeout=30) as response:
                archive = BytesIO(response.read())
            with ZipFile(archive) as zipped:
                with TemporaryDirectory(dir=DATA_DIR) as staging:
                    for path in missing:
                        temporary = Path(staging) / path.name
                        temporary.write_bytes(zipped.read(path.name))
                    for path in missing:
                        (Path(staging) / path.name).replace(path)
        except (OSError, BadZipFile, KeyError) as error:
            raise RuntimeError(
                "数据准备失败。请检查网络连接后重试，"
                "也可以从 UCI 下载数据，将 optdigits.tra 和 optdigits.tes "
                "放到本脚本所在目录。"
            ) from error
    return train_path, test_path


def load_digits(path):
    samples = []
    with path.open(encoding="ascii") as file:
        for line in file:
            fields = line.strip().split(",")
            inputs = [int(field) / 16 for field in fields[:-1]]
            samples.append((inputs, int(fields[-1])))
    return samples


def make_model(rng):
    layers = [
        Linear(64, 16, rng),
        ReLU(),
        Linear(16, 8, rng),
        ReLU(),
        Linear(8, 10, rng)
    ]
    # TODO：先创建一个列表。第一项是 Linear(64, 16, rng)，第二项是 ReLU()。
    # 按题面补齐剩余三层，每次创建 Linear 都传入这里收到的 rng，
    return Sequential(layers)
    # 每个激活层都单独调用一次 ReLU()。最后用该列表创建并返回 Sequential 对象。
    raise NotImplementedError("第 4 题：make_model")


def loss_and_gradient(scores, label):
    """从分类分数计算交叉熵损失及其对分数的梯度。"""
    maximum = max(scores)
    shifted = [score - maximum for score in scores]
    exponentials = [exp(score) for score in shifted]
    total = sum(exponentials)
    loss = log(total) - shifted[label]
    gradient = [value / total for value in exponentials]
    gradient[label] -= 1.0
    return loss, gradient


def update_parameters(model, learning_rate):
    for layer in model.layers:
        if isinstance(layer, Linear):

            for j in range(layer.out_features):
                for i in range(layer.in_features):
                    layer.weights[j][i] -= (
                        learning_rate * layer.grad_weights[j][i]
                    )
                layer.bias[j] -= learning_rate * layer.grad_bias[j]
    """使用各全连接层刚算出的梯度，进行一次参数更新。"""
    # TODO：遍历 model.layers，用 isinstance(layer, Linear) 筛选全连接层。
    # 对每个输出 j 和输入 i，把 layer.weights[j][i] 减去
    # learning_rate * layer.grad_weights[j][i]。
    # 每个输出 j 的偏置只更新一次。把偏置更新放在遍历 i 的循环外。
    return 
    raise NotImplementedError("第 4 题：update_parameters")


def train_epoch(model, samples, rng):
    rng.shuffle(samples)
    total_loss = 0.0
    for inputs, label in samples:
        scores = model.forward(inputs)
        loss, gradient = loss_and_gradient(scores, label)
        model.backward(gradient)
        update_parameters(model, LEARNING_RATE)
        total_loss += loss
    return total_loss / len(samples)


def evaluate(model, samples):
    correct = 0
    for inputs, label in samples:
        scores = model.forward(inputs)
        prediction = scores.index(max(scores))
        if prediction == label:
            correct += 1
    return correct


def main():
    rng = Random(SEED)
    model = make_model(rng)
    train_path, test_path = prepare_data()
    train_samples = load_digits(train_path)
    test_samples = load_digits(test_path)

    print(f"训练样本 {len(train_samples)} 张，测试样本 {len(test_samples)} 张")
    for epoch in range(1, EPOCHS + 1):
        loss = train_epoch(model, train_samples, rng)
        print(f"第 {epoch:2d} 轮  平均训练损失 {loss:.4f}", flush=True)

    correct = evaluate(model, test_samples)
    print(f"测试准确率 {correct / len(test_samples):.2%}（{correct}/{len(test_samples)}）")


if __name__ == "__main__":
    try:
        main()
    except NotImplementedError as error:
        print(f"请先补全模板中的方法。当前待完成：{error}")
        raise SystemExit(1)
    except RuntimeError as error:
        print(error)
        raise SystemExit(1)
