x = 600851475143
Divider = 1

while x > 0:
    if x % Divider == 0:
        print(Divider)
        x = x / Divider
        Divider += 1
    else:
        Divider += 1
