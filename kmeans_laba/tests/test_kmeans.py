
from kmeans.algorithm import KMeans


def test_two_clusters():
    points = [[1, 1], [10, 10], [2, 2], [9, 9], [3, 3]]

    model = KMeans(2)
    clusters, centers = model.fit(points)

    assert clusters[0] == [[1, 1], [2, 2], [3, 3]]
    assert clusters[1] == [[10, 10], [9, 9]]
    assert centers == [[2.0, 2.0], [9.5, 9.5]]


def test_one_cluster():
    points = [[1, 1], [3, 3], [5, 5]]

    model = KMeans(1)
    clusters, centers = model.fit(points)

    assert clusters == [points]
    assert centers == [[3.0, 3.0]]


def test_empty_cluster():
    points = [[1, 1], [1, 1], [5, 5]]

    model = KMeans(2)
    clusters, centers = model.fit(points)

    assert sum(len(cluster) for cluster in clusters) == len(points)
    assert len(centers) == 2
