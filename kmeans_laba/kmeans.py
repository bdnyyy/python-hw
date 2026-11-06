n = int(input("Введите количество точек: "))

points = []

for i in range(n):
    x = float(input("Введите X: "))
    y = float(input("Введите Y: "))
    points.append([x, y])

k = int(input("Введите количество кластеров: "))

if n <= 0 or k <= 0 or k > n:
    print("Ошибка: неверное количество точек или кластеров")
else:
    centers = points[:k]

    for step in range(100):
        clusters = [[] for i in range(k)]

        for point in points:
            nearest = 0
            min_distance = float("inf")

            for i in range(k):
                distance = (point[0] - centers[i][0]) ** 2 + (point[1] - centers[i][1]) ** 2

                if distance < min_distance:
                    min_distance = distance
                    nearest = i

            clusters[nearest].append(point)

        new_centers = []

        for i in range(k):
            if len(clusters[i]) > 0:
                x = sum(point[0] for point in clusters[i]) / len(clusters[i])
                y = sum(point[1] for point in clusters[i]) / len(clusters[i])
                new_centers.append([x, y])
            else:
                new_centers.append(centers[i])

        if new_centers == centers:
            break

        centers = new_centers

    for i in range(k):
        print("Кластер", i + 1, ":", clusters[i])
        print("Центр:", new_centers[i])
