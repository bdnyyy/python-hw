"""Построение графиков для алгоритма K-means."""

import matplotlib.pyplot as plt

from .algorithm import KMeans


def plot_clusters(
    points: list[list[float]],
    labels: list[int],
    centers: list[list[float]],
) -> None:
    """Показывает точки по кластерам и их центры."""
    plt.figure(figsize=(8, 6))

    for i in range(len(centers)):
        cluster = [points[j] for j in range(len(points)) if labels[j] == i]

        if cluster:
            x = [point[0] for point in cluster]
            y = [point[1] for point in cluster]

            plt.scatter(x, y, label=f"Кластер {i + 1}")

    center_x = [center[0] for center in centers]
    center_y = [center[1] for center in centers]

    plt.scatter(
        center_x,
        center_y,
        color="black",
        marker="X",
        s=180,
        label="Центры",
    )

    plt.title("Кластеризация K-means")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)


def plot_elbow(
    points: list[list[float]],
    max_k: int,
    max_iter: int,
    seed: int,
) -> None:
    """Строит график зависимости Inertia от числа кластеров."""
    k_values = list(range(1, min(max_k, len(points)) + 1))
    inertias = []

    for k in k_values:
        model = KMeans(n_clusters=k, max_iter=max_iter, seed=seed)
        labels = model.fit(points)
        inertias.append(model.inertia(points, labels))

    plt.figure(figsize=(8, 6))
    plt.plot(k_values, inertias, marker="o")

    plt.title("Метод локтя")
    plt.xlabel("Количество кластеров (k)")
    plt.ylabel("Inertia")
    plt.xticks(k_values)
    plt.grid(True)
