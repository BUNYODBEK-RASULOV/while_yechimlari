# 26-topshiriq
n = int(input("n sonini kiriting:"))
f = 1
x = 1
i = 3
a = 0
while f < n:
    a = f
    f = f + x
    print(i, f)
    x = a
    i = i + 1
if f == n:
    print("F({})={} < {} < F({})={}".format(i - 2, a, n, i, f + x))
else:
    print("Fibonanchi sonlari orasida kiritgan soningizga teng had yuq")
