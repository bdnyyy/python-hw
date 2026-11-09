"""Интерфейс командной строки для алгоритма K-means."""

import argparse

import matplotlib.pyplot as plt

from .algorithm import KMeans
from .data import generate_points
from .visualization import plot_clusters, plot_elbow


def main() -> None:
    """Запускает кластеризацию с параметрами пользователя."""
    parser = argparse.ArgumentParser(description="Кластеризация методом K-means")

    parser.add_argument("--samples", type=int, default=300)
    parser.add_argument("--k", type=int, default=3)
    parser.add_argument("--iter", type=int, default=100)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--elbow", action="store_true")

    args = parser.parse_args()

    try:
        points = generate_points(args.samples, args.k, args.seed)

        model = KMeans(
            n_clusters=args.k,
            max_iter=args.iter,
            seed=args.seed,
        )

        labels = model.fit(points)
        total_inertia = model.inertia(points, labels)

    except ValueError as error:
        parser.error(str(error))

    print("Результаты кластеризации K-means")
    print("Количество точек:", args.samples)
    print("Количество кластеров:", args.k)
    print("Количество итераций (максимум):", args.iter)
    print("Seed:", args.seed)

    for i in range(args.k):
        count = labels.count(i)
        print(f"Кластер {i + 1}: {count} точек")

    print(f"Inertia: {total_inertia:.2f}")

    plot_clusters(points, labels, model.centers)

    if args.elbow:
        plot_elbow(points, 10, args.iter, args.seed)

    plt.show()
