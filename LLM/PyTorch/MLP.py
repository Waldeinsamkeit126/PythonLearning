import torch
import torch.nn as nn

X = torch.tensor([
    [-2.0],
    [-1.0],
    [0.0],
    [1.0],
    [2.0]
])

y = torch.tensor([
    [4.0],
    [1.0],
    [0.0],
    [1.0],
    [4.0]
])

model = nn.Sequential(
    nn.Linear(1,16),
    nn.ReLU(),
    nn.Linear(16,1)
)
loss_func=nn.MSELoss()

optimizer=torch.optim.SGD(
    model.parameters(),
    lr=0.01)

for epoch in range(5000):
    pred=model(X)
    loss=loss_func(pred,y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if epoch%500==0:
        print(epoch, loss.item())
print()

test = torch.tensor([[3.0]])

print(model(test))