"""Тесты алгоритма K-means."""

from kmeans.algorithm import KMeans


def test_three_clusters() -> None:
    """Проверяет разделение точек на три кластера."""
    points = [
        [1.0, 1.0],
        [10.0, 10.0],
        [20.0, 20.0],
        [2.0, 2.0],
        [11.0, 11.0],
        [21.0, 21.0],
        [3.0, 3.0],
        [12.0, 12.0],
        [22.0, 22.0],
    ]

    model = KMeans(n_clusters=3, seed=42)
    labels = model.fit(points)

    assert len(set(labels)) == 3
    assert labels[0] == labels[3] == labels[6]
    assert labels[1] == labels[4] == labels[7]
    assert labels[2] == labels[5] == labels[8]


def test_same_seed() -> None:
    """Проверяет повторяемость результатов с одинаковым seed."""
    points = [[1.0, 1.0], [2.0, 2.0], [10.0, 10.0], [11.0, 11.0]]

    first = KMeans(n_clusters=2, seed=42)
    second = KMeans(n_clusters=2, seed=42)

    assert first.fit(points) == second.fit(points)
    assert first.centers == second.centers


def test_inertia_decreases() -> None:
    """Проверяет, что дополнительные итерации не увеличивают инерцию."""
    points = [
        [1.0, 1.0],
        [2.0, 2.0],
        [3.0, 3.0],
        [10.0, 10.0],
        [11.0, 11.0],
        [12.0, 12.0],
    ]

    first = KMeans(n_clusters=2, max_iter=1, seed=42)
    second = KMeans(n_clusters=2, max_iter=100, seed=42)

    labels_first = first.fit(points)
    labels_second = second.fit(points)

    assert second.inertia(points, labels_second) <= first.inertia(points, labels_first)


def test_different_k() -> None:
    """Проверяет количество центров при разных значениях k."""
    points = [[1.0, 1.0], [5.0, 5.0], [10.0, 10.0]]

    first = KMeans(n_clusters=1)
    second = KMeans(n_clusters=3)

    first.fit(points)
    second.fit(points)

    assert len(first.centers) == 1
    assert len(second.centers) == 3


def test_predict() -> None:
    """Проверяет определение кластеров для новых точек."""
    points = [[1.0, 1.0], [2.0, 2.0], [10.0, 10.0], [11.0, 11.0]]

    model = KMeans(n_clusters=2, seed=42)
    model.fit(points)

    labels = model.predict([[1.5, 1.5], [10.5, 10.5]])

    assert labels[0] != labels[1]
