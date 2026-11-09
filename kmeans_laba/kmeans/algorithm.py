"""Реализация алгоритма кластеризации K-means."""

import random


class KMeans:
    """Класс для разделения точек на кластеры."""

    def __init__(
        self, n_clusters: int = 3, max_iter: int = 100, seed: int = 42
    ) -> None:
        """Сохраняет параметры алгоритма."""
        if n_clusters < 1 or max_iter < 1:
            raise ValueError(
                "Количество кластеров и итераций должно быть положительным"
            )

        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.seed = seed
        self.centers: list[list[float]] = []

    def _init_centroids(self, X: list[list[float]]) -> None:
        """Выбирает случайные начальные центры кластеров."""
        generator = random.Random(self.seed)
        self.centers = [point.copy() for point in generator.sample(X, self.n_clusters)]

    def _assign(self, X: list[list[float]]) -> list[int]:
        """Определяет ближайший центр для каждой точки."""
        labels = []

        for point in X:
            nearest = 0
            min_distance = float("inf")

            for i in range(self.n_clusters):
                distance = sum(
                    (point[j] - self.centers[i][j]) ** 2 for j in range(len(point))
                )

                if distance < min_distance:
                    min_distance = distance
                    nearest = i

            labels.append(nearest)

        return labels

    def _update(self, X: list[list[float]], labels: list[int]) -> None:
        """Пересчитывает центры кластеров."""
        new_centers = []

        for i in range(self.n_clusters):
            cluster = [X[j] for j in range(len(X)) if labels[j] == i]

            if cluster:
                center = [
                    sum(point[j] for point in cluster) / len(cluster)
                    for j in range(len(X[0]))
                ]
                new_centers.append(center)
            else:
                new_centers.append(self.centers[i].copy())

        self.centers = new_centers

    def fit(self, X: list[list[float]]) -> list[int]:
        """Обучает модель и возвращает метки кластеров."""
        if not X:
            raise ValueError("Список точек не должен быть пустым")

        if self.n_clusters > len(X):
            raise ValueError("Кластеров не может быть больше, чем точек")

        if not X[0] or any(len(point) != len(X[0]) for point in X):
            raise ValueError("Все точки должны иметь одинаковую ненулевую размерность")

        self._init_centroids(X)

        for _ in range(self.max_iter):
            labels = self._assign(X)
            old_centers = [center.copy() for center in self.centers]

            self._update(X, labels)

            if self.centers == old_centers:
                break

        return self._assign(X)

    def predict(self, X: list[list[float]]) -> list[int]:
        """Определяет кластеры для новых точек."""
        if not self.centers:
            raise ValueError("Сначала необходимо обучить модель")

        if any(len(point) != len(self.centers[0]) for point in X):
            raise ValueError("Размерность точек не совпадает с обучающими данными")

        return self._assign(X)

    def inertia(self, X: list[list[float]], labels: list[int]) -> float:
        """Вычисляет сумму квадратов расстояний до центров."""
        if not self.centers:
            raise ValueError("Сначала необходимо обучить модель")

        if len(X) != len(labels):
            raise ValueError("Количество точек и меток должно совпадать")

        if any(len(point) != len(self.centers[0]) for point in X):
            raise ValueError("Размерность точек не совпадает с обучающими данными")

        if any(label < 0 or label >= self.n_clusters for label in labels):
            raise ValueError("Некорректная метка кластера")

        total = 0.0

        for point, label in zip(X, labels):
            total += sum(
                (point[j] - self.centers[label][j]) ** 2 for j in range(len(point))
            )

        return total
