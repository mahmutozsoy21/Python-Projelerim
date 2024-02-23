# ekrandan alinan bir sayinin rakamlari toplamini bulan program yazınız

sayi=str(input("lütfen sayi giriniz:"))# sayinin rakamlarini indexlemek için str yaptık


rakam_toplami=0

for i in sayi:
    
    rakam_toplami+=int(i)# burda str ifadesini int değer ile toplamak için int yaptık
    
    
print(rakam_toplami)
    
