numbers = list(map(int, input('Введите числа через пробел: ').split()))

print('Чётные числа в обратном порядке:')

for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] % 2 == 0:
        print(numbers[i], end=' ')