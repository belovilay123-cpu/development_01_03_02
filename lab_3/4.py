def print_prime_factors(n, d=2):
    if n <= 1:
        return
    
    # Если квадрат делителя больше n, значит оставшееся n — простое число
    if d * d > n:
        print(n)
        return
    
    if n % d == 0:
        print(d)
        # Делим n на d и проверяем этот же делитель еще раз
        print_prime_factors(n // d, d)
    else:
        # Переходим к следующему возможному делителю
        print_prime_factors(n, d + 1)

