def smallest_divisor(n):
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return divisor
        divisor += 1
    return n


number = int(input("Введите число: "))
print("Наименьший делитель, отличный от единицы:", smallest_divisor(number))