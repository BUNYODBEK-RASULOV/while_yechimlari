# 29-topshiriq
e = float(input("e sonini { 0<e<1 } kiriting:"))
a = 1
f = 2
k = 3
while not (abs(f - a) < e):
    x = f
    f = (a + 2 * f) / 3
    a = x
    print("K={0} \t A({1})={2} \t A({3})={4} \t |A({3})-A({1})|={5}".format(k, k - 1, a, k, f, abs(f - a)))
    k = k + 1
