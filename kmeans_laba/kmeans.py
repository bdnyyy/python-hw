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
    print("Введённые точки:", points)
    print("Количество кластеров:", k)
