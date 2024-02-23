# ekrana girilen sayilarin en küçüğünü ve en büyüğünü yazdiran kod

sayilar=[]

for i in range(5):# 5 tane sayi listeye eklenecek
    sayi=int(input("sayi giriniz:"))

    sayilar.append(sayi)

print("En büyük sayi:",max(sayilar))
print("En küçük sayi",min(sayilar))



















