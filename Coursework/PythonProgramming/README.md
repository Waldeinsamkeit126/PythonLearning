# Python 程序设计课程作业

归档 Canvas「Python程序设计（0562）」第一次至第四次作业，共 14 个 `.py` 文件。文件来自已提交作业的附件，保留原文件名、代码、注释和字节内容；整理日期为 2026-11-26。

## 作业索引

| 作业 | 源码 | 练习内容 |
| --- | --- | --- |
| [第一次](https://canvas.shufe.edu.cn/courses/43781/assignments/41069) | [homework1_1.py](Homework01/homework1_1.py) | 输入信息并打印课程名片 |
| 第一次 | [homework1_2.py](Homework01/homework1_2.py) | 分段计算快递费用 |
| 第一次 | [homework1_3.py](Homework01/homework1_3.py) | 计算手机套餐外费用 |
| 第一次 | [homework1_4.py](Homework01/homework1_4.py) | 按年龄、学生身份及周末判断票价 |
| [第二次](https://canvas.shufe.edu.cn/courses/43781/assignments/43236) | [homework2_1.py](Homework02/homework2_1.py) | 暴力枚举求解货物装载 |
| 第二次 | [homework2_2.py](Homework02/homework2_2.py) | 梯度下降与停止条件 |
| 第二次 | [homework2_3.py](Homework02/homework2_3.py) | BFS 求迷宫最短步数 |
| [第三次](https://canvas.shufe.edu.cn/courses/43781/assignments/43326) | [homework3_1.py](Homework03/homework3_1.py) | 凯撒密码解密与线索匹配 |
| 第三次 | [homework3_2.py](Homework03/homework3_2.py) | 字典维护商品、库存及销售额 |
| 第三次 | [homework3_3.py](Homework03/homework3_3.py) | CSV 读取、分组统计及报告输出 |
| [第四次](https://canvas.shufe.edu.cn/courses/43781/assignments/44090) | [homework4_1.py](Homework04/homework4_1.py) | Layer 基类、全连接层及梯度 |
| 第四次 | [homework4_2.py](Homework04/homework4_2.py) | ReLU 前向与反向传播 |
| 第四次 | [homework4_3.py](Homework04/homework4_3.py) | Sequential 按顺序组合网络层 |
| 第四次 | [homework4_4.py](Homework04/homework4_4.py) | 手写数字分类、交叉熵与参数更新 |

Canvas 题面链接需要课程访问权限。第五次作业不在本次归档范围内。

## 运行方法

使用 Python 3，验证环境为 Python 3.9.13。以上源码只使用标准库，无需安装 PyTorch。

从仓库根目录运行，例如：

```powershell
python Coursework/PythonProgramming/Homework01/homework1_1.py
python Coursework/PythonProgramming/Homework02/homework2_2.py
python Coursework/PythonProgramming/Homework04/homework4_1.py
```

- 第一次作业需要终端输入：第 1 题依次输入姓名、学号、课程名和目标分数；第 2 题输入重量；第 3 题输入流量和通话时长；第 4 题输入年龄、是否学生、是否周末（后两项使用 `yes` / `no`）。边界问题见验证记录。
- 第二次作业第 1 题先执行自测，再输入 0～20 的整数容量；其余题和第三次作业前两题直接执行内置测试。
- 第三次作业第 3 题需要原课程的 `Homework03/data/experiments.csv`。该数据不在这次下载的提交附件内，因此未归档。请从课程材料获取原文件；成功运行后会在同目录写入 `summary.csv`。
- 第四次作业的四个文件必须放在同一目录，彼此存在模块导入。前三题直接执行自测。运行 `homework4_4.py` 会在缺少数据时联网下载 UCI 手写数字数据，在脚本目录保存 `optdigits.tra` 和 `optdigits.tes`，然后训练 10 轮并输出测试准确率。数据来源及许可说明保留在原代码内。

## 原始提交与验证

[验证记录](VERIFICATION.md)区分语法检查、内置测试、已知错误及未验证部分。归档保留学习过程中的问题，没有改写提交答案。

[文件清单](archive-manifest.json)记录每个文件的课程来源、字节数及 SHA-256，可用于核对原始下载。保留的 TODO、`pass` 或不可达异常语句不一定表示代码未完成，应结合实际执行结果判断。

[返回仓库首页](../../README.md)
