import torch
import torch.nn as nn


class NeuralNet(nn.Module):
    def __init__(self, i_size, h_size, n_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(i_size, h_size)
        self.l2 = nn.Linear(h_size, h_size)
        self.l3 = nn.Linear(h_size, n_classes)
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        # no activation and no softmax at the end
        return out