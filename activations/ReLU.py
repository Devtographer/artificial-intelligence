

"""
Rectified Linear Unit (ReLU) activation function.

ReLU activation function is a piecewise linear function that will output the input directly if it is positive, otherwise, it will output zero.
The derivative of ReLU is 1 for input values > 0 and 0 for input values <= 0.

f(x) = x if x > 0 else 0
f'(x) = 1 if x > 0 else 0
"""

import numpy as np


class ReLU:

    def forward(self, inputs):
        self.output = np.maximum(0, inputs)
