#ekrana girilen sayinin kaç tane pozitif böleni olduğunu bulma

sayi=int(input("sayi giriniz:"))
bölen_sayisi=0

for bölen_sayi in range(1,sayi):

    if sayi%bölen_sayi==0:
        
        bölen_sayisi+=1


print("pozitif bölen sayisi:",bölen_sayisi)













