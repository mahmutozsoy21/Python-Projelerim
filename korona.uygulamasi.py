isim=input("hastanin adini giriniz:")
soy_isim=input("hastanin soy ismini giriniz:")
yas=int(input("hastanin yaşini giriniz:"))
kronik=input("hastanin kronik hastaliği varmi varsa VAR yok ise YOK giriniz:")
ateş=float(input("hastanin ateşini giriniz:"))
öksürük=input("hastanin öksürüğü varmi:").upper()
  
  
if yas>65:
    print("yaşli bölümüne götürünüz.")
    if kronik=="VAR" and ateş>40:
        print("1. dereceden korona şüphelisi hastaya korona testi yapin ")
        korona_testi=input("testi sonucunu yaziniz:").upper()
        if korona_testi=="POZİTİF":
            print(isim,soy_isim,"korona hastasi")
        else:
            print(isim,soy_isim,"korona değil taburcu olabilir")    
    elif kronik=="VAR" or ateş>40:
        print(isim,soy_isim,"ikinci dereceden korona şüphelisi hastaya korona testi yapin")
        korona_testi=input("testi sonucunu yaziniz:").upper()
        if korona_testi=="POZİTİF":
             print(isim,soy_isim,"korona hastasi")
        else:
             print(isim,soy_isim,"korona değil taburcu olabilir") 
    else:
        print(isim,soy_isim,"gerekli kontrolllerden sonra taburcu olabilir")    
else:
    print("normal bölüme götürünüz")
    if kronik=="VAR" and ateş>45:
        print("1. dereceden korona şüphelisi hastaya korona testi yapin.")
        korona_testi=input("testi sonucunu yaziniz:").upper()
        if korona_testi=="POZİTİF":
            print(isim,soy_isim,"korona hastasi")
        else:
            print(isim,soy_isim,"korona değil taburcu olabilir") 
    elif kronik=="VAR" or ateş>40:
        print(isim,soy_isim,"ikinci dereceden korona şüphelisi hastaya korona testi yapin")
        korona_testi=input("testi sonucunu yaziniz:").upper()
        if korona_testi=="POZİTİF":
             print(isim,soy_isim,"korona hastasi")
        else:
             print(isim,soy_isim,"korona değil taburcu olabilir") 
    else:
        print(isim,soy_isim,"gerekli kontrolllerden sonra taburcu olabilir")           
 

        
    

 
  

