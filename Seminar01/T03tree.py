# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
#     *
#    ***
#   *****
#  *******
# *********

rows = int(input('Введите количество ярусов елки '))
STARS = "*"
SPACE = " "
STEP = 2
count_spaces = rows - 1
count_stars = 1
for row in range(rows):
    print(SPACE * (count_spaces - row) + STARS * (count_stars + row * STEP))

