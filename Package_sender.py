'''
Заполняйте текстовый файл случайным набором данных, отдавайте данные пакетами по 32 байта.
Максимальный размер файла 2 МБ (2097152). Случайные данные не должны содержать специальные символы.
Каждый пакет данных должен быть соединен с другим знаком "-".
Когда файл заполнится, выпишите в другой файл повторение каждого символа.
Например:
h - 23 раз
t - 55 раз
7 - 81 раз
и т.д.
'''

import random

stackSize = 32
maxFileSize = 2097152
tempStack = []
writer = open('File.txt', 'w')
counterWriter = open('counterFile.txt', 'w')

alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

elementCounter = [a, b, c, d, e, f, g, h, i, j, k, l, m,
                  n, o, p, q, r, s, t, u, v, w, x, y, z]

packageCount = int(maxFileSize / (stackSize + 1))

for it in range(packageCount):
    for qi in range(stackSize):
        rand = random.randint(0, 25)
        tempStack.insert(qi, alphabetList[rand])
        elementCounter[rand] += 1
    writer.write(''.join(tempStack) + '-')
    tempStack = []

for qw in range(len(elementCounter)):
    counterWriter.write(str(alphabetList[qw]) + ' - ' + str(elementCounter[qw]) + ' times' + '\n')
