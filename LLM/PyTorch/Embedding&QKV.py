import torch
import torch.nn as nn

#1.
embedding = nn.Embedding(10000,768)

x = torch.tensor([5])

print(embedding(x).shape)

embedding = nn.Embedding(
    num_embeddings=5000,
    embedding_dim=128
)

x = torch.tensor([
    [5, 7, 9],
    [2, 8, 1]
])
#2.
scores = torch.tensor([2.0,1.0,0.1])

weights = torch.softmax(scores, dim=0)

print(weights)

#3.
x=torch.randn(2,3,4) #batch=2, token=3, embedding_dim=4
print("x:",x.shape)

q_proj = nn.Linear(4, 4)
k_proj = nn.Linear(4, 4)
v_proj = nn.Linear(4, 4)

Q = q_proj(x)
K = k_proj(x)
V = v_proj(x)

print("Q:", Q.shape)
print("K:", K.shape)
print("V:", V.shape)

scores = Q @ K.transpose(-2, -1)

print("scores:", scores.shape)

weights = torch.softmax(
    scores,
    dim=-1
)

print("weights:", weights.shape)
print(weights[0])

output = weights @ V

print("output:", output.shape)