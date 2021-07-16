# 23-topshiriq
a = int(input("a sonini iriting:"))
b = int(input("b sonini iriting:"))
i = 1
EKUK = 1
# birinchi nechchi sonigacha bo'lib chiqishni aniqlab olamiz minimum operatoridan foydalanib
while i <= min(a, b):
    # kiritilgan eng kichik sonning bo'luvchisini topamiz
    if min(a, b) % i == 0:
        # topilgan bo'luvchi eng katta sonning bo'luvchisimi yuqmi tekshiramiz
        if max(a, b) % i == 0:
            # ikki sonning ham bo'luvchisi bulsa unda printga chiqaradi
            EKUK = i
    i = i + 1
print("EKUK:", EKUK)
