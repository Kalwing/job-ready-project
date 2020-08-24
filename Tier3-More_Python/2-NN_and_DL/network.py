import numpy as np
from typing import Union
import random
import time


def ReLU(z):
    return z * (z > 0)

def ReLU_P(z):
    return (z>0).astype(z.dtype)


def sigmoid(z):
    return 1/(1-np.exp(-z))


def tanh(z):
    return np.tanh(z)


ACTIVATIONS = {
    'ReLU': ReLU,
    'sigmoid': sigmoid,
    'tanh': tanh,
}

ACTIVATIONS_P = {
    'ReLU': ReLU_P,
}


def mean_square_error(y, label):
    total_len = sum([n for n in y.shape])
    mae = np.sum(np.square((y - label)))
    return mae / total_len

def nabla_mean_square_error(y, label):
    return y - label


LOSSES = {
    'mse': mean_square_error,
}
NABLA_LOSSES = {
    'mse': nabla_mean_square_error,
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
        self.activ_prime = ACTIVATIONS_P[activation]
        self.last_preactivation = None
        self.last_error = None
        self.size = size
        self.input_size = input_size

    def initialize(self):
        self.weights = np.zeros((self.size, self.input_size))
        self.biases = np.zeros((self.size, 1))

    def output(self, data):
        self.last_input = data
        self.last_preactivation = np.dot(self.weights, data)
        self.last_preactivation += self.biases
        self.last_output = self.activ_func(self.last_preactivation)
        return self.last_output


class Learner:
    def __init__(self, loss):
        self.network = []
        self.loss = LOSSES[loss]
        self.nabla_loss_a = NABLA_LOSSES[loss]

    def add(self, layer):
        if layer.input_size is None:  # The input hasn't been initialized
            layer.input_size = self.network[-1].size
        self.network.append(layer)

    def feedforward(self, data):
        next_input = np.array(data)
        for layer in self.network:
            next_input = layer.output(next_input)
        return next_input

    def backpropagate(self, output):
        pass

    def SGD(self, data, nb_epoch, lr):
        for epoch in range(nb_epoch):
            mean_loss = None
            # Select a set of training examples
            weight_modifiers = []
            bias_modifiers = []
            for i in range(len(data)):
                x = data[i]
                print(F"{epoch}: {i+1}/{len(data)}: ", end="")
                result = self.feedforward(x[0])
                loss_value = self.loss(result, x[1])
                if mean_loss is None:
                    mean_loss = loss_value
                else:
                    mean_loss = mean_loss * (i/(i+1)) + loss_value / (i+1)
                print(F"loss={mean_loss}", end="\r")
                z_l = self.network[-1].last_preactivation
                p_l = self.network[-1].activ_prime(z_l)
                error = self.nabla_loss_a(result, x[1]) * p_l
                self.network[-1].last_error = error
                # backpropagate
                e = self.network[-1].weights*error
                for layer in self.network[-2::-1]:
                    z_l = layer.last_preactivation
                    error = e * layer.activ_prime(z_l)
                    layer.last_error = error
                    e = layer.weights*error
                time.sleep(0.1)
                # gradient descent
                for i, layer in enumerate(self.network):
                    wm = layer.last_error * layer.last_input
                    try:
                        weight_modifiers[i]
                        bias_modifiers[i]
                    except IndexError:
                        weight_modifiers.append(np.zeros(wm.shape))
                        bias_modifiers.append(np.zeros(layer.last_error.shape))
                    # print("lasterror", layer.last_error.shape, layer.last_input.shape)
                    # print("wieghts", weight_modifiers[i].shape)
                    weight_modifiers[i] += wm
                    bias_modifiers[i] += layer.last_error
                    # calculate weight modifier += (lr/len(data) * (layer.last_error * a_(l-1))
                    # calculate bias modifier += (lr/len(data) * (layer.last_error)
            for i, layer in enumerate(self.network):
                layer.weights -= lr/len(data) * weight_modifiers[i]
                layer.biases -= lr/len(data) * bias_modifiers[i]
            print()

    def summary(self):
        for layer in self.network:
            print(layer)

    def fit(self, data, nb_epoch, learning_rate=0.001):
        for layer in self.network:
            layer.initialize()
        self.SGD(data, nb_epoch, learning_rate)

    def predict(self, data):
        return self.feedforward(data)


data = [(n, n*-0.5 + 5) for n in [random.randint(1, 10) for n in range(100)]]
model = Learner(loss='mse')
model.add(Dense(10, input_size=1))
model.add(Dense(1))
model.summary()
model.fit(data, 10)
model.predict(1)
model.predict(10)
