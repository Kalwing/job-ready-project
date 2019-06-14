import numpy as np
from typing import Union


def sigmoid(z):
    return 1/(1-np.exp(-z))


class Layer:
    def __init__(self, size):
        self.size = size

    def feedforward(a):
        return self.activation(self.get_preactivation(a))

    def get_preactivation(a):
        return np.dot(self.weight, a) + self.bias


class perceptronLayer(Layer):
    def __init__(self, size, activation=sigmoid):
        super().__init__(size)
        self.activation = activation

    def SGD():
        pass


n = Network([1, 5, 10, 4])
n.summary()
# v = -eta grad(L)

n.fit(data)
