# 1000 den küçük 3 veya 5 in katları olan sayıların toplamını yazdıran program
x=0
toplam=0

for i in range(1000):
    if i%3==0 or i%5==0:
        toplam+=i


print(toplam)














