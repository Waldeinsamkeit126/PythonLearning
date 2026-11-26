"""第 1 题。全连接层与教师提供的 Layer 基类。"""

from math import sqrt


class Layer:
    def __init__(self):
        self._input = None

    def _save_input(self, inputs):
        """保存本次前向输入的副本，供反向传播使用。"""
        self._input = inputs.copy()

    def _get_input(self):
        """读取最近一次前向输入。"""
        if self._input is None:
            raise ValueError("请先调用 forward，再调用 backward")
        return self._input

    def forward(self, inputs):
        raise NotImplementedError

    def backward(self, grad_output):
        raise NotImplementedError


def initialize_parameters(in_features, out_features, rng):
    """返回 (weights, bias)，每个输出神经元对应一行权重和一个偏置。"""
    bound = sqrt(6.0 / in_features)
    weights = []
    for _ in range(out_features):
        row = [rng.uniform(-bound, bound) for _ in range(in_features)]
        weights.append(row)
    return weights, [0.0] * out_features


class Linear(Layer):
    """第 1 题。实现带偏置的全连接层。"""

    def __init__(self, in_features, out_features, rng):
        # TODO：在创建每个 Linear 对象时完成以下三步。
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features
        # 1. 用 super().__init__() 初始化父类状态，再把输入和输出维度存为实例属性。
        self.weights, self.bias = initialize_parameters(in_features, out_features, rng)
        # 2. 在这里调用同文件中的普通函数，rng 直接使用构造函数收到的值：
        #    self.weights, self.bias = initialize_parameters(in_features, out_features, rng)
        #    例如，输入 2 项、输出 3 项时，weights 有 3 行，每行 2 项，
        #    bias 有 3 项。后续每次前向计算都使用对象已有的参数。
        self.grad_weights = [[0.0] * in_features for i in range(out_features)] 
        self.grad_bias = [0.0] * out_features
        return
        # 3. 创建同样形状的零列表 self.grad_weights 和 self.grad_bias。
        #    例如，循环 3 次，每次新建一行 [0.0, 0.0]，再加入梯度列表。
        raise NotImplementedError("第 1 题：Linear.__init__")

    def forward(self, inputs):
        self._save_input(inputs)
        # TODO：先调用 self._save_input(inputs)。
        outputs = []
        for j in range(self.out_features):
            total = self.bias[j]
            for i in range(self.in_features):
                total += self.weights[j][i] * inputs[i]
        # 按输出下标 j 遍历。从 self.bias[j] 开始，逐项加上
            outputs.append(total)
        return outputs
        # self.weights[j][i] * inputs[i]。算完一个输出就加入结果列表。
        raise NotImplementedError("第 1 题：Linear.forward")

    def backward(self, grad_output):
        inputs = self._get_input()
        # TODO：用 inputs = self._get_input() 取回上次前向的输入。
        grad_input = [0.0] * self.in_features
        # 新建长度为 in_features 的零列表，用来累加输入梯度。
        for j in range(self.out_features):
            self.grad_bias[j] = grad_output[j]
        # 遍历每个输出 j，用 grad_output[j] 覆盖偏置梯度。
            for i in range(self.in_features):
                self.grad_weights[j][i] = grad_output[j] * inputs[i]
                grad_input[i] += self.weights[j][i] * grad_output[j]
        # 再遍历每个输入 i，覆盖权重梯度[j][i]，并累加到输入梯度[i]。
        return grad_input
        # 各项公式和手算例子见题面。最后返回输入梯度列表。
        raise NotImplementedError("第 1 题：Linear.backward")


if __name__ == "__main__":
    from random import Random

    layer = Linear(2, 3, Random(42))
    assert isinstance(layer, Layer)
    assert layer.grad_weights == [[0, 0], [0, 0], [0, 0]]
    assert layer.grad_bias == [0, 0, 0]
    assert layer.grad_weights[0] is not layer.grad_weights[1]

    layer.weights = [[2, -1], [0, 3], [1, 1]]
    layer.bias = [1, -2, 0]
    inputs = [4, 5]
    assert layer.forward(inputs) == [4, 13, 9]
    inputs[0] = 99  # 检查反向传播使用的是前向时保存的副本
    assert layer.backward([2, -1, 3]) == [7, -2]
    assert layer.grad_bias == [2, -1, 3]
    assert layer.grad_weights == [[8, 10], [-4, -5], [12, 15]]

    assert layer.forward([-1, 2]) == [-3, 4, 1]
    assert layer.backward([0, 1, 0]) == [0, 3]
    assert layer.grad_bias == [0, 1, 0]
    assert layer.grad_weights == [[0, 0], [-1, 2], [0, 0]]
    print("第 1 题自测通过")
