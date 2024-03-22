tower1, tower2, tower3 = map(int, input().split())
if tower1>tower2 and tower1>tower3 and tower2>tower3:
    print(tower1,tower2,tower3)
elif tower2>tower1 and tower2>tower3 and tower3>tower1:
    print(tower2,tower3,tower1)
elif tower3>tower1 and tower3>tower2 and tower2>tower1:
    print(tower3,tower2,tower1)
elif tower3>tower1 and tower3>tower2 and tower1>tower2:
    print(tower3,tower1,tower2)
elif tower2>tower1 and tower2>tower3 and tower1>tower3:
    print(tower2,tower1,tower3)
