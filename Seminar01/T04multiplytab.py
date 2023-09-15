# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке
COLUMN = 4
for i in range(2, 10, COLUMN):
    for j in range(2, 11):
        for k in range(i, i + COLUMN):
            print(f'{k:>3} * {j:>3} = {k * j:>3}', end='\t')
        print()
    print()





