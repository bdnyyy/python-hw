"""Генерация тестовых данных для алгоритма K-means."""

import math
import random


def generate_points(samples: int, k: int, seed: int) -> list[list[float]]:
    """Создаёт точки вокруг заданного количества центров."""
    if samples < 1 or k < 1 or k > samples:
        raise ValueError("Количество точек должно быть не меньше числа кластеров")

    generator = random.Random(seed)
    points = []

    for i in range(samples):
        cluster = i % k
        angle = 2 * math.pi * cluster / k

        center_x = 10 * math.cos(angle)
        center_y = 10 * math.sin(angle)

        x = generator.gauss(center_x, 1)
        y = generator.gauss(center_y, 1)

        points.append([x, y])

    generator.shuffle(points)

    return points
