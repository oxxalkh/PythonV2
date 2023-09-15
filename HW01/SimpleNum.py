
# Напишите код, который запрашивает число и сообщает, является ли оно
# простым или составным. Используйте правило для проверки: «Число является
# простым, если делится нацело только на единицу и на себя».
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

MIN_LIM = 0
MAX_LIM = 100000
MIN_PRIME_NUM = 2

input_num = int(input('Введите целое число '))
if input_num < MIN_LIM or input_num >= MAX_LIM:
    print(f"Введено недопустимое число. Допустимы числа от 0 до {MAX_LIM}.")

if input_num >= MIN_PRIME_NUM:
    count_div = 0
    for i in range(1, input_num + 1):
        if input_num % i == 0:
            count_div += 1
    if count_div <= 2:
        print(f'Число {input_num} простое')
    else:
        print(f'Число {input_num} составное')
else:
    print('Числа 0 и 1 не являются ни простыми, ни составными')

