"""第 3 题。按顺序组合多个网络层。"""


class Sequential:
    """第 3 题。按顺序组合多个层对象。"""

    def __init__(self, layers):
        self.layers = layers.copy()
        # TODO：用 layers.copy() 复制列表并存入 self.layers。
        return
        # 列表里的每一项仍是调用者传进来的层对象。
        raise NotImplementedError("第 3 题：Sequential.__init__")

    def forward(self, inputs):
        result = inputs
        # TODO：用 inputs 作为第一个传入值。遍历 self.layers，
        for layer in self.layers:
            result = layer.forward(result)
        return result
        # 每次用 layer.forward(...) 的返回值替换当前值，最后返回它。
        raise NotImplementedError("第 3 题：Sequential.forward")

    def backward(self, grad_output):
        result = grad_output
        # TODO：从 grad_output 开始，用 reversed(self.layers) 倒序遍历。
        for layer in reversed(self.layers):
            result = layer.backward(result)
        return result
        # 把每次 layer.backward(...) 返回的梯度交给下一个遍历到的层。
        raise NotImplementedError("第 3 题：Sequential.backward")


if __name__ == "__main__":
    from homework4_1 import Layer

    calls = []

    class TestLayer(Layer):
        def __init__(self, name, factor):
            super().__init__()
            self.name = name
            self.factor = factor

        def forward(self, inputs):
            calls.append(("forward", self.name, inputs))
            return [inputs[0] * self.factor]

        def backward(self, grad_output):
            calls.append(("backward", self.name, grad_output))
            return [grad_output[0] * self.factor]

    first = TestLayer("first", 2)
    second = TestLayer("second", 3)
    layers = [first, second]
    model = Sequential(layers)
    layers.clear()
    assert model.layers == [first, second], "应复制列表，保留原来的层对象"
    assert model.forward([4]) == [24]
    assert model.backward([1]) == [6]
    assert calls == [
        ("forward", "first", [4]),
        ("forward", "second", [8]),
        ("backward", "second", [1]),
        ("backward", "first", [3]),
    ], f"层的调用顺序或收到的值不正确：{calls}"
    print("第 3 题自测通过")
