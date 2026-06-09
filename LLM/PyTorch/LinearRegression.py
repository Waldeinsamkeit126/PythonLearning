import torch
import torch.nn as nn

X = torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0]
])

y = torch.tensor([
    [3.0],
    [5.0],
    [7.0],
    [9.0]
])

model=nn.Linear(1,1)

loss_func=nn.MSELoss()

optimizer=torch.optim.SGD(
    model.parameters(),
    lr=0.01)

for epoch in range(1000):
    pred=model(X)
    loss=loss_func(pred,y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if epoch%100==0:
        print(
            f"epoch={epoch},"
            f"loss={loss.item():.4f}")
        print("weight =", model.weight.item())
        print("bias   =", model.bias.item())
print()

test = torch.tensor([[10.0]])

print(model(test))