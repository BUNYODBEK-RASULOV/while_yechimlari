# 25-topshiriq
n = int(input("n sonini kiriting:"))
f = 1
x = 1
i = 3
a = 0
while f <= n:
    a = f
    f = f + x
    print(i, "\t- xadi F=", f)
    x = a
    i = i + 1
print("{} sonidan katta {} Feboanchi soni.".format(n, f))
