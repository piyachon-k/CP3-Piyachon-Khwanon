user_name = input('USERNAME : ')
password = input('PASSWORD : ')
print('')
if user_name == 'customer' and password == '12345':
    print('Welcome to the shop!!!!')
    print('-----------------------')
    print('1. Banana        10 THB')
    print('2. Apple         15 THB')
    print('3. Orange        30 THB')
    print('')
    order_no = int(input('pls choose order number you want to buy : '))
    
    if order_no == 1:
        unit = int(input('how many unit you want to buy : '))
        print('your order is banana', unit, 'unit total price is', unit*10)
    elif order_no == 2:
        unit = int(input('how many unit you want to buy : '))
        print('your order is apple', unit, 'unit total price is', unit*15)
    elif order_no == 3:
        unit = int(input('how many unit you want to buy : '))
        print('your order is orange', unit, 'unit total price is', unit*30)
    else:
        print('there is no order number that you choose')
else:
    print('username or password not correct')