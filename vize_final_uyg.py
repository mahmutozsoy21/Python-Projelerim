
vize_notu=int(input("Vize notunuzu giriniz:"))

final_notu=int(input("Final notunuzu giriniz:"))

gecme_notu=int((vize_notu*0.4)+(final_notu*.6))

print("Vize notu:",vize_notu)
print("Final notu",final_notu)


if final_notu<50: # finalde 50 den düşük almak dersten kalmaya sebep oluyor
    print("FF Kaldi",gecme_notu)
    print("Bütünleme ssinavina giriniz.")

    bütünleme_notu=int(input("Bütünleme notunuzu giriniz"))
    gecme_notu2=int(vize_notu*0.4+bütünleme_notu*0.6)

    if bütünleme_notu<50:  # bütünlemede  50 den düşük almak dersten kalmaya sebep oluyor
        print("Kaldi",gecme_notu2)

    elif bütünleme_notu>=50 and gecme_notu2>45:  # geçme notunu 45 olarak kabul ettik 
        print("Geçti:",gecme_notu2)

    else:
        print("Kaldi:",gecme_notu2)        

elif final_notu>50 and gecme_notu<45: # geçme notunu 45 olarak kabul ettik 
    print("Kaldi:",gecme_notu)

else:
    print("Geçti:",gecme_notu)