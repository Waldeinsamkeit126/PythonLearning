"""第 2 题。ReLU 激活层。"""

from homework4_1 import Layer


class ReLU(Layer):
    """第 2 题。继承 Layer 的初始化方法。"""

    def forward(self, inputs):
        self._save_input(inputs)
        outputs = []
        # TODO：先调用 self._save_input(inputs)，再逐项构造新列表。
        for x in inputs:
            if x > 0:
                outputs.append(x)
            else:
                outputs.append(0)
        # 大于零的值原样加入结果，其余位置加入零。
        return outputs
        raise NotImplementedError("第 2 题：ReLU.forward")

    def backward(self, grad_output):
        inputs = self._get_input()
        # TODO：用 inputs = self._get_input() 取回前向输入。
        grad_input = []
        # 遍历下标 i。如果 inputs[i] > 0，就把 grad_output[i]
        for i in range(len(inputs)):
            if inputs[i] > 0:
                grad_input.append(grad_output[i])
            else:
                grad_input.append(0)
        # 加入结果列表，否则加入零。判断条件取自前向输入。
        return grad_input
        raise NotImplementedError("第 2 题：ReLU.backward")


if __name__ == "__main__":
    layer = ReLU()
    assert isinstance(layer, Layer)
    inputs = [-2, 0, 3]
    assert layer.forward(inputs) == [0, 0, 3]
    inputs[2] = -3
    assert ReLU().forward([1, -2, 0]) == [1, 0, 0]
    assert layer.backward([5, 6, 7]) == [0, 0, 7]
    print("第 2 题自测通过")
