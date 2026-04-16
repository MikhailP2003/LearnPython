def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def digit_count(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


number = int(input("Введите число: "))

sum_digits = digit_sum(number)
count_digits = digit_count(number)

print("Сумма чисел:", sum_digits)
print("Количество цифр в числе:", count_digits)
print("Разность суммы и количества цифр:", sum_digits - count_digits)