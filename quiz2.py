import numpy as np

id = 'YOUR STUDENT ID'

def gen_data_regression():
    x = np.random.rand(1000) * 5
    y = np.polyval(np.random.randn(np.random.randint(3, 6)), x) + np.random.rand(len(x))
    return x, y


def gen_data_clustering():
    x1 = np.random.randn(100, 2) * 2 + np.random.randint(2, 10, 2)
    x2 = np.random.randn(100, 2) * 2 + np.random.randint(-10, -2, 2)
    x = np.vstack((x1, x2))
    return x


def gen_data_classification():
    x1 = np.random.randn(100, 2) * 2 + np.random.randint(2, 10, 2)
    x2 = np.random.randn(100, 2) * 2 + np.random.randint(-10, -2, 2)
    x3 = np.random.randn(100, 2) * 2 + np.array([-5, 5])
    x = np.vstack((x1, x2, x3))
    y = ['a'] * len(x1) + ['b'] * len(x2) + ['c'] * len(x3)
    y = np.array(y)
    return x, y


id = int(id)
np.random.seed(id % 1000)

x, y = gen_data_regression()
xtest1 = 20
# TODO 1 (5 points)
# use nonlinear regression (degree = 3)
# find ytest for xtest1 = 20
print(f'{ytest:.02f}')

x = gen_data_clustering()
xtest2 = np.array([0, 0])
# TODO 2 (5 points)
# use k-means (k = 2)
# find cluster_index for xtest2 = np.array([0, 0])
print(cluster_index)

x, y = gen_data_classification()
xtest3 = np.array([[0, 0]])
# TODO 3 (5 points)
# classification with MLP
# learning rate=0.1, epochs=100, 3 hidden layers with number of nodes = [10, 20, 10]
# find label for xtest3 = np.array([[0, 0]])
print(label)

