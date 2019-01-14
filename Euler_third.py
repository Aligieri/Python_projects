'''

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

'''


x = 600851475143
Divider = 1

while x > 0:
    if x % Divider == 0:
        print(Divider)
        x = x / Divider
        Divider += 1
    else:
        Divider += 1
