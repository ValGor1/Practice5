def sqr(num):
    if num % 10 == 1 and num % 100 != 11:
        return 'попугай'
    elif 2 <= num % 10 <= 4 and (num % 100 < 10 or num % 100 >= 20):
        return 'попугая'
    else:
        return 'попугаев'

num = int(input())
result = sqr(num)
print(num, result)