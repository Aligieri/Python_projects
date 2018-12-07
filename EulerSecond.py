x = 1
y = 2
z = 3
SUM = 0

while y <= 4000000:
    if y % 2 == 0:
        print(SUM)
        SUM += y
        x = y
        y = z
        z = x + y
        print(x, y, z)
    else:
        x = y
        y = z
        z = x + y
        print(x, y, z)


print(SUM)
