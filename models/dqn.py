import torch
import torch.nn as nn

class RainbowDQN(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(RainbowDQN, self).__init__()
        self.fc1 = nn.Linear(input_dim, 128)
        self.fc2 = nn.Linear(128, 128)
        self.value_stream = nn.Linear(128, 1)
        self.advantage_stream = nn.Linear(128, output_dim)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        value = self.value_stream(x)
        advantage = self.advantage_stream(x)
        q_value = value + (advantage - advantage.mean(dim=1, keepdim=True))
        return q_value
