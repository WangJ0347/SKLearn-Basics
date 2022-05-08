from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def best_k(dataset):
    """
    :param dataset:
    :return: elbow heuristics graph between number of clusters and distortion presented as
    inertia
    """
    distortion = []
    k = []
    for i in range(1, 8):
        kmeans = KMeans(i)
        kmeans.fit(x)
        temp = kmeans.inertia_
        distortion.append(kmeans.inertia_)
        k.append(i)
    plt.plot(k,distortion, 'b', marker='o')
    plt.plot(3, distortion[2], marker="o", markersize=10, markerfacecolor="red")
    plt.title('Elbow heuristics')
    plt.xlabel('values of k')
    plt.ylabel('Distortion')
    plt.suptitle('k = 3 is the best number of clusters')
    plt.show()


if __name__ == '__main__':
    data = load_iris()
    x = data.data
    best_k(x)
