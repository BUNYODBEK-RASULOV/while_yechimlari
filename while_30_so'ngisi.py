# 30-topshiriq
a=int(input("To'rt burchakning A tomonnini kiriting:"))
b=int(input("To'rt burchakning B tomonnini kiriting:"))
c=int(input("Kvadratning C tomonnini kiriting:"))
i=0
j=0
while (a-c>=0):
    i=i+1
    a=a-c
while b-c>=0:
    j=j+1
    b=b-c
print("{} ta tomini {} ga teng  kvadrat joylashtirish mumkin.".format(j*i,c))

