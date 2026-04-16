count = int(input('Количество контейнеров: '))

containers = []

for _ in range(count):
    weight = int(input('Введите вес контейнера: '))
    while weight > 200 or weight <= 0:
        print('Ошибка: вес должен быть от 1 до 200.')
        weight = int(input('Введите вес контейнера: '))
    containers.append(weight)

new_weight = int(input('\nВведите вес нового контейнера: '))
while new_weight > 200 or new_weight <= 0:
    print('Ошибка: вес должен быть от 1 до 200.')
    new_weight = int(input('Введите вес нового контейнера: '))

position = 1

for weight in containers:
    if weight >= new_weight:
        position += 1
    else:
        break

print('\nНомер, который получит новый контейнер:', position)