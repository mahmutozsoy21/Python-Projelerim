# 1000 den küçük 3 veya 5 in katları olan sayıların toplamını yazdıran program
toplam=0


for i in range(1000):# 0 dan 999 a kadar sayıları deniyor

    if i%3==0 or i%5==0:# sayinin 3 veya 5 in katı olup olmadığını kontrol ediyor
        
        toplam+=i# eğer sonuçlar doğru ise i sayısını toplama ekliyor


print("Sonuç:",toplam)














