quantity = int(input('enter your quantity: '))
unit_cost = int(input('enter your cost: '))
# discount = 10 %
sum = quantity * unit_cost

if sum >= 1000:
    print('total cost',abs(int(sum * 10 / 100)-sum))
