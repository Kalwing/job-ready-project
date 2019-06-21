import numpy as np
from typing import Union
import random


def ReLU(z):
    return z * (z > 0)


def sigmoid(z):
    return 1/(1-np.exp(-z))


def tanh(z):
    return np.tanh(z)


ACTIVATIONS = {
    'ReLU': ReLU,
    'sigmoid': sigmoid,
    'tanh': tanh,
}


class Layer:
    def __init__(self):
        self.last_input = None
        self.last_output = None
        self.size = None
        self.input_size = None

    def __repr__(self):
        return F"{self.__class__} of size {self.size} (takes data of size {self.input_size})"


class Dense(Layer):
    def __init__(self, size, input_size=None, activation="ReLU"):
        super().__init__()
        self.activ_func = ACTIVATIONS[activation]
        self.last_preactivation = None
        self.last_error = None
        self.size = size
        self.input_size = input_size

    def initialize(self):
        self.weights = np.zeros((self.input_size, self.size))
        self.biases = np.zeros((1, self.size))

    def output(self, data):
        self.last_input = data
        self.last_preactivation = np.dot(self.weights, data) + self.biases
        self.last_output = self.activ_func(self.last_preactivation)
        return self.last_output


class Learner:
    def __init__(self):
        self.network = []

    def add(self, layer):
        if layer.input_size is None:  # The input hasn't been initialized
            layer.input_size = self.network[-1].size
        self.network.append(layer)

    def feedforward(self, data):
        next_input = data
        for layer in self.network:
            next_input = layer.output(next_input)
        return next_input

    def backpropagate(self, output):
        pass

    def SGD(self, data, batch_size, lr):
        pass

    def summary(self):
        for layer in self.network:
            print(layer)

    def fit(self, data, batch_size=2, learning_rate=0.001):
        for layer in self.network:
            layer.initialize()
        self.SGD(data, batch_size, learning_rate)

    def predict(self, data):
        return self.feedforward(data)


data = [(n, n*-0.5 + 5) for n in [random.randint(1, 10) for n in range(1000)]]
model = Learner()
model.add(Dense(10, input_size=1))
model.add(Dense(2))
model.summary()
model.fit(data)
model.predict(1)
