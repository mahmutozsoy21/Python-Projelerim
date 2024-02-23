# ekrandan girilen bir sayinin asal sayi olup olmamasını bulan program

sayi=int(input("Sayi giriniz:"))

if sayi>1: # en küçük asal sayi 2 olduğu için 2 den başlattık
    for i in range(2,sayi):

        if sayi%i==0:
          print(sayi,"sayisi asal değildir")
          break

     

        else:
           print(sayi,"sayisi asaldir")
  

else:
    print(sayi,"sayisi asal değildir")
























