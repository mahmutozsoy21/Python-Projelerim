import random

print("basit tahmin oyununa hoşgeldiniz!")

sayi=random.randint(1,100)
tahmin_hakki=5

while True:
    tahmin=int(input("tahmininizi giriniz"))

    if tahmin==sayi:
        print("tebrikler doğru tahmin")
        break
    elif tahmin<sayi:
        print("daha büyük sayi giriniz")
    else:
        print("daha küçük sayi giriniz")

    tahmin_hakki-=1

    if tahmin_hakki==0:
        print("deneme hakkiniz bitti doğru cevap=",sayi)             

