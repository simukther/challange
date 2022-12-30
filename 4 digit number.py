numbers = 4321
reversed_num = 0

while numbers != 0:
    digit = numbers % 10
    reversed_num = reversed_num * 10 + digit
    numbers //= 10
print('reversed number: ' + str(reversed_num))