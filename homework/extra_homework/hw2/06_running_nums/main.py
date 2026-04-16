k = int(input('Сдвиг: '))
numbers = list(map(int, input('Введите список через пробел: ').split()))

print('Изначальный список:', numbers)

k %= len(numbers)
numbers = numbers[-k:] + numbers[:-k]

print('Сдвинутый список:', numbers)