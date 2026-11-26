# Python 与 PyTorch 学习

记录 Python 程序设计课程作业，以及张量、神经网络与注意力机制学习。课程归档包含前四次作业的 14 个源码文件；LLM 目录保留 6 个 PyTorch 学习脚本。

## 课程作业

[Python 程序设计课程归档](Coursework/PythonProgramming/README.md)：按作业次数整理原始提交，附题目索引、运行方法和验证记录。

| 作业 | 内容 | 入口 |
| --- | --- | --- |
| 第一次 | 输入输出、条件判断与费用计算 | [4 个文件](Coursework/PythonProgramming/Homework01/) |
| 第二次 | 枚举装载、梯度下降与 BFS | [3 个文件](Coursework/PythonProgramming/Homework02/) |
| 第三次 | 凯撒密码、商品管理与 CSV 统计 | [3 个文件](Coursework/PythonProgramming/Homework03/) |
| 第四次 | 用标准库实现神经网络层与训练 | [4 个文件](Coursework/PythonProgramming/Homework04/) |

原始提交中的已知问题和缺失数据见[验证记录](Coursework/PythonProgramming/VERIFICATION.md)。

## 学习导航

| 阶段 | 内容 | 入口 |
| --- | --- | --- |
| 1. 基础 | 张量形状、索引、矩阵乘法与线性层 | [BasicConcept.py](LLM/PyTorch/BasicConcept.py) |
| 2. 训练循环 | 用线性回归学习 y = 2x + 1 | [LinearRegression.py](LLM/PyTorch/LinearRegression.py) |
| 3. 非线性模型 | 用 MLP 拟合少量平方函数样本 | [MLP.py](LLM/PyTorch/MLP.py) |
| 4. 图像分类 | MNIST 数据加载与全连接网络训练 | [NeuralNet(PyTorch).py](LLM/NeuralNet%28PyTorch%29.py) |
| 5. 注意力基础 | Embedding、Softmax 与 Q/K/V 计算 | [Embedding&QKV.py](LLM/PyTorch/Embedding%26QKV.py) |
| 6. 模块组合 | 注意力、残差、LayerNorm 与 MLP | [TinyTransformer.py](LLM/PyTorch/TinyTransformer.py) |

更详细的实验说明见 [LLM 模块](LLM/README.md)。`LLM` 是原有目录名，其中也包含通用神经网络基础。

## 运行第一个例子

准备 Python 3 和适配本机环境的 PyTorch。在仓库根目录创建虚拟环境（PowerShell）：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install torch
.\.venv\Scripts\python.exe LLM/PyTorch/LinearRegression.py
```

脚本会输出 loss、权重、偏置与输入 10 的预测值。目标关系为 y = 2x + 1；数值受随机初始化与训练过程影响。

MNIST 示例额外需要 torchvision，首次运行会联网下载数据到当前工作目录下的 `data/`：

```powershell
.\.venv\Scripts\python.exe -m pip install torchvision
.\.venv\Scripts\python.exe "LLM/NeuralNet(PyTorch).py"
```

文件名包含括号或 `&` 时，请用引号包住路径。每个脚本单独执行；仓库尚未锁定依赖版本，也没有统一训练入口。

## 实验边界

- MLP 使用很小的样本集，其外推结果不能代表泛化能力。
- TinyTransformer 是随机输入的前向传播演示；当前注意力是单头、没有缩放和因果掩码，不是完整语言模型。
- MNIST 脚本训练 5 轮并输出训练损失，尚无测试集评估或模型保存逻辑。
- 训练结果和运行环境需要自行记录；本次文档整理未执行模型训练。

## 后续维护

新练习注明目的、依赖、运行命令、预期输出与局限。训练数据、模型权重和环境文件应按需忽略，不要将缓存混入源码目录。

相关仓库：[C++ 学习](https://github.com/Waldeinsamkeit126/CPPLearning) · [竞赛与工具项目](https://github.com/Waldeinsamkeit126/Projects)
