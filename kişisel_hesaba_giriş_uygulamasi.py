db_ka="mahmut"
db_ps=1234

while True:
    kullanici_adi=input("lütfen kullanici adinizi giriniz:")
    kullanici_sifresi=int(input("lütfen kullanici şifrenizi giriniz:"))
    

    if kullanici_adi==db_ka and kullanici_sifresi==db_ps:
        print("Giriş başarili hoşgeldiniz:",kullanici_adi)
        break
  


