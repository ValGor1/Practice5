NAME = str(input("Имя игрока?: "))
ATT = float(input("Введите ATT: "))
COMP = float(input("Введите COMP: "))
YDS = float(input("Введите YDS: "))
TD = float(input("Введите TD: "))
INT = float(input("Введите INT: "))
def Rating(ATT, COMP, YDS, TD, INT):
    a = (((COMP/ATT)-0.3) * 5)
    b = (((YDS/ATT)-3) * 0.25)
    c = ((TD/ATT) * 20)
    d = (2.375 - ((INT/ATT) * 25))
    return round(((a + b + c + d) / 6) * 100, 1)
if Rating(ATT, COMP, YDS, TD, INT) < 16:
    print('выраженный дефицит массы тела')
elif 16 <= Rating(ATT, COMP, YDS, TD, INT) <= 18.49:
    print('недостаточная масса тела')
elif 18.5 <= Rating(ATT, COMP, YDS, TD, INT) <= 24.99:
    print('норма')
elif 25 <= Rating(ATT, COMP, YDS, TD, INT) <= 29.99:
    print('избыточная масса тела')
elif 30 <= Rating(ATT, COMP, YDS, TD, INT) <=34.99:
    print('ожирение первой степени')
elif 35 <= Rating(ATT, COMP, YDS, TD, INT) <= 39.99:
    print('ожирение второй степени')
elif 40 <= Rating(ATT, COMP, YDS, TD, INT):
    print('ожирение третьей степени')