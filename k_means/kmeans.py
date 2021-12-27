import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class KMeans:
    def __init__(
            self,
            k=3,
            toler=0.0001,
            max_iterations=500):
        self.k = k
        self.toler = toler
        self.max_iterations = max_iterations
        self.centroids = {}
        self.classes = {}

    def fit(self, data):

        self.centroids = {}

        for j in range(self.k):
            self.centroids[j] = data[j]

        for i in range(self.max_iterations):
            self.classes = {}
            for j in range(self.k):
                self.classes[j] = []

            for features in data:
                distances = [np.linalg.norm(features - self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classes[classification].append(features)

            previous = dict(self.centroids)

            for classification in self.classes:
                self.centroids[classification] = np.average(self.classes[classification], axis=0)

            is_optimal = True

            for centroid in self.centroids:

                original_centroid = previous[centroid]
                curr = self.centroids[centroid]

                if np.sum((curr - original_centroid) / original_centroid * 100.0) > self.toler:
                    is_optimal = False

            if is_optimal:
                break

    def predict(self, data):
        distances = [np.linalg.norm(data - self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification


def main():
    df = pd.read_csv("ipl.csv")
    df = df[['one', 'two']]

    x = df.values

    km = KMeans(3)
    km.fit(x)

    colors = 10 * ["r", "g", "c", "b", "k"]

    for centroid in km.centroids:
        plt.scatter(km.centroids[centroid][0], km.centroids[centroid][1], s=130, marker="x")

    for classification in km.classes:
        color = colors[classification]
        for features in km.classes[classification]:
            plt.scatter(features[0], features[1], color=color, s=30)

    plt.show()


if __name__ == "__main__":
    main()
