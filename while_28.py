# 28-topshiriq
e = float(input("e sonini kiriting:"))
f = 1.0  # ketmaketlikning A(k)- xadi
a = 0  # ketmaketlikning A(k-1) xadi
k = 1  # tartib raqami
while (not abs(f - a) < e):
    a = f
    f = 2 + 1 / f
    print("k={} ketmaketlikning A({})={}, A({}={}))".format(k, k, a, k + 1, f))
    k = k + 1
