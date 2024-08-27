car = 150
t1, t2, t3 = map(int, input().split())

if t1 <= car:
    print("터널 통과 불가능")
elif t2 <= car:
    print("터널 통과 불가능")
elif t3 <= car:
    print("터널 통과 불가능")
else:
    print("터널 통과 가능")
