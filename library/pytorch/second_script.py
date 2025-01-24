import torch

z = torch.zeros(5,3)
print(z)
print(z.dtype)
i = torch.ones((5,3), dtype=torch.int16)
print(i)
torch.manual_seed(1729)
r1 = torch.rand(2, 2)
print(f"A random tensor: {r1}")