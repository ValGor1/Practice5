Pin = int(input())
Pin_4 = Pin % 10
Pin_3 = (Pin % 100) // 10
Pin_2 = (Pin //100) % 10
Pin_1 = Pin // 1000
if Pin//10000 > 1:
    print('Error')
elif Pin_4 == Pin_3 or Pin_4 == Pin_2 or Pin_4 == Pin_1 or Pin_3 == Pin_2 or Pin_3 == Pin_1 or Pin_2 == Pin_1:
    print('Error')
elif 2050>= Pin >=1900:
    print('Error')
else:
    print('OK')
