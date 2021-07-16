# 22-topshiriq
n=int(input("n sonini (n>1) kiriting:"))
i=2
tubsonmi=False
print("Bo'luvchilari:",1)
while(i<=n/2):
    if(n%i==0):
        print("Bo'luvchilari:",i)
        tubsonmi=True
    i=i+1
print("Bo'luvchilari:",n)
if tubsonmi :
    print("tub son emas")
else:
    print("tub son")

