import torch
import torch.nn as nn

class TinyAttention(nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.q_proj = nn.Linear(hidden_size, hidden_size)
        self.k_proj = nn.Linear(hidden_size, hidden_size)
        self.v_proj = nn.Linear(hidden_size, hidden_size)

    def forward(self, x):
        Q = self.q_proj(x)
        K = self.k_proj(x)
        V = self.v_proj(x)
        scores = Q @ K.transpose(-2, -1)
        weights = torch.softmax(
            scores,
            dim=-1
        )
        output = weights @ V
        return output
#MLP
class TinyMLP(nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(
                hidden_size,
                hidden_size * 4
            ),
            nn.ReLU(),
            nn.Linear(
                hidden_size * 4,
                hidden_size
            )
        )
    def forward(self, x):
        return self.net(x)

#whole block
class TinyTransformerBlock(nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.attn = TinyAttention(
            hidden_size
        )
        self.norm1 = nn.LayerNorm(
            hidden_size
        )
        self.mlp = TinyMLP(
            hidden_size
        )
        self.norm2 = nn.LayerNorm(
            hidden_size
        )
    def forward(self, x):
        # Attention
        attn_out = self.attn(x)
        x = x + attn_out
        x = self.norm1(x)
        print("after attention:",
              x.shape)
        # MLP
        mlp_out = self.mlp(x)
        x = x + mlp_out
        x = self.norm2(x)
        print("after mlp:",
              x.shape)
        return x

x = torch.randn(
    2,
    3,
    4
)

model = TinyTransformerBlock(
    hidden_size=4
)

y = model(x)

print("output:", y.shape)