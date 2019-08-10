import numpy as np
import matplotlib.pyplot as plt

def create_dataset(row_nb):
    """
        Fonction use to generate dataset
    """
    sick = np.random.randn(row_nb, 2) + np.array([-2, -2])
    healthy = np.random.randn(row_nb, 2) + np.array([2, 2])

    features = np.vstack([sick, healthy])

    # print(features)
    # plt.plot(features, 'ro')
    # plt.show()

    targets = np.concatenate((np.zeros(row_nb), np.ones(row_nb)))

    # print(targets)

    return features, targets


def init_variables():
    weight = np.random.normal(size=2)
    bias = 0

    return weight, bias


def pre_activation(features, weight, bias):
    return np.dot(features, weight) + bias


def activation(z):
    return 1/(1+np.exp(-z))


def derivative_activation(z):
    """

    :param z: pre_activation
    :return: derivative sigmoid
    """
    return activation(z) * (1 - activation(z))


def cost(prediction, targets):
    return np.mean((prediction - targets) ** 2)


def train(features, targets, weight, bias):
    predict = np.round(activation(pre_activation(features, weight, bias)))

    epochs = 100
    learning_rate = 0.01

    print('Accuracy = %s' % np.mean(predict == targets))

    for epoch in range(epochs):
        if epoch % 10 == 0:
            a = activation(pre_activation(features, weight, bias))
            print('Cost = %s' % cost(a, targets))
        weight_gradient = np.zeros(weight.shape)
        bias_gradient = 0

        for feature, target in zip(features, targets):
            z = pre_activation(feature, weight, bias)
            y = activation(z)
            # update gradients
            weight_gradient += (y - target) * derivative_activation(z) * feature
            bias_gradient += (y - target) * derivative_activation(z)
        # Update variables
        weight = weight - learning_rate * weight_gradient
        bias = bias - learning_rate * bias_gradient

    predict = np.round(activation(pre_activation(features, weight, bias)))
    print('Accuracy = %s' %np.mean(predict == targets))


    # Plot points
    plt.scatter(features[:, 0], features[:, 1], s=40, c=targets, cmap=plt.cm.Spectral)
    plt.show()


if __name__ == '__main__':
    # Create data
    features, targets = create_dataset(100)
    # Create variables
    weight, bias = init_variables()
    # training
    train(features, targets, weight, bias)
