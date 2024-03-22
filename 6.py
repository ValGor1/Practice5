first_day = int(input())
second_day = int(input())
third_day = int(input())
if first_day == second_day == third_day:
    print(3)
elif first_day == second_day or first_day == third_day or second_day == third_day:
    print(2)
else:
    print(1)