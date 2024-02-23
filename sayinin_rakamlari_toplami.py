# ekrandan alinan bir sayinin rakamlari toplamini bulan program yazınız

sayi=str(input("lütfen sayi giriniz:"))
rakam_toplami=0
for i in sayi:
    rakam_toplami+=int(i)
    
print(rakam_toplami)
    