
class KMeans:
    def __init__(self, k):
        self.k = k
        self.centers = []
        self.clusters = []

    def fit(self, points):
        self.centers = [point[:] for point in points[:self.k]]

        for step in range(100):
            self.clusters = [[] for i in range(self.k)]

            for point in points:
                nearest = 0
                min_distance = float("inf")

                for i in range(self.k):
                    distance = (point[0] - self.centers[i][0]) ** 2 + (point[1] - self.centers[i][1]) ** 2

                    if distance < min_distance:
                        min_distance = distance
                        nearest = i

                self.clusters[nearest].append(point)

            new_centers = []

            for i in range(self.k):
                if len(self.clusters[i]) > 0:
                    x = sum(point[0] for point in self.clusters[i]) / len(self.clusters[i])
                    y = sum(point[1] for point in self.clusters[i]) / len(self.clusters[i])
                    new_centers.append([x, y])
                else:
                    new_centers.append(self.centers[i])

            if new_centers == self.centers:
                break

            self.centers = new_centers

        self.centers = new_centers
        return self.clusters, self.centers


if __name__ == "__main__":
    points = [[1, 1], [10, 10], [2, 2], [9, 9], [3, 3]]
    k = 2

    model = KMeans(k)
    clusters, centers = model.fit(points)

    for i in range(k):
        print("Кластер", i + 1, ":", clusters[i])
        print("Центр:", centers[i])
