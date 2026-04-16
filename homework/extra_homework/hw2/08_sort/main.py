numbers = [1, 4, -3, 0, 10]

print('Изначальный список:', numbers)

for i in range(1, len(numbers)):
    current = numbers[i]
    j = i - 1

    while j >= 0 and numbers[j] > current:
        numbers[j + 1] = numbers[j]
        j -= 1

    numbers[j + 1] = current

print('\nОтсортированный список:', numbers)