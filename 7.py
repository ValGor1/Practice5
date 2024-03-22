N, K, M = map(int, input().split())
quickway_1 = N - K + M - 1
quickway_2 = (M - K) - 1
if quickway_2 <= 0:
    print(quickway_1)
elif quickway_1 > quickway_2:
    print(quickway_2)
else:
    print(quickway_1)