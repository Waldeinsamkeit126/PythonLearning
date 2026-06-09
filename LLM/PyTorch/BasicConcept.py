import torch
import torch.nn as nn
#1.
x=torch.tensor([
    [1,2,3],
    [4,5,6]
])

print (x) #tensor([[1, 2, 3],
       #[4, 5, 6]])
print(x.shape) #torch.Size([2, 3])
#2.
x = torch.randn(5,3)
print(x.shape) #torch.Size([5, 3])
#3.
A = torch.randn(2,4)
B = torch.randn(4,6)
C = A @ B
print(C.shape) #torch.Size([2, 6])
#4.
X = torch.randn(64,1,28,28) 
print(X[0].shape)
print(X[0,0].shape)
print(X[0,0,0].shape)
print(X[:10].shape)
print(X[:,0,:,:])
print(X[:,0].shape)
#5.
x = torch.tensor([
    [1,2,3],
    [4,5,6]
])
y = x.reshape(3,2)
print(y)#tensor([[1, 2],
       #[3, 4],
       #[5, 6]])
#6.
x = torch.randn(64,784)
linear = nn.Linear(784, 128)
y = linear(x)
print(y.shape)#torch.Size([64, 128])
#7.
linear = nn.Linear(784, 128)
print(linear.weight.shape)
print(linear.bias.shape)