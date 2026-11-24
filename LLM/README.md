# 神经网络与注意力机制练习

[返回仓库首页](../README.md)

本模块记录边学习 PyTorch 边编写的练习，包括 TinyMNIST、TinyMLP 和 TinyTransformer。

## 按学习目标分类

- **张量与网络基础**：[BasicConcept.py](PyTorch/BasicConcept.py)、[LinearRegression.py](PyTorch/LinearRegression.py)、[MLP.py](PyTorch/MLP.py)。
- **完整数据训练练习**：[MNIST 全连接网络](NeuralNet%28PyTorch%29.py)。
- **注意力与 Transformer 组件**：[Embedding 与 QKV](PyTorch/Embedding%26QKV.py)、[TinyTransformer](PyTorch/TinyTransformer.py)。

前三个基础练习和两个注意力练习只使用脚本内置数据或随机张量；MNIST 练习通过 torchvision 下载数据。

从仓库根目录运行注意力练习（已安装 torch）：

```powershell
python "LLM/PyTorch/Embedding&QKV.py"
python LLM/PyTorch/TinyTransformer.py
```

TinyTransformer 的输入与输出形状均为 `[2, 3, 4]`，用于观察注意力、残差连接和 MLP 对张量维度的影响。它没有训练循环、分词器或文本生成接口。
