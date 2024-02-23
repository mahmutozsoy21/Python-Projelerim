import random
import time

kullanicilar=list()


def kullanici_ekle(x):
    print("-"*30)
    print("Kullanici ekleme ekranina hoşgeldiniz:)")
    ekle=input("Lütfen eklenecek kullaniciyi giriniz:")
    kullanicilar.append(ekle) # listeye kullanıcı ekler
    input("Devem etmek için enter tuşuna tiklayiniz...")
    

def kullanici_gör(x): 
    say=1   # sayaç olarak kullandık
    print("-"*30)

    for i in x:
        print(str(say)+"-Kullanici Adi:",i) # iki farklı veri tipi olduğu için hepsini str yaptık
        say+=1
    input("Devem etmek için enter tuşuna tiklayiniz")   

def seç(x):
    say=1
    kişi_seç=int(input("Kaç kişi seçilsin?:")) 
    rastgele_seç=random.sample(x,kişi_seç) # listeye eklenen kullanıcılardan rastgele seçim yapar   

    for i in rastgele_seç:  
        print(str(say)+"-Kullanici Adi:",i) # iki farklı veri tipi olduğu için hepsini str yaptık
        say+=1
        print("Diğer kişi listeden seçiliyor...")
        time.sleep(3)
    print("-"*30)
    input("Devem etmek için enter tuşuna tiklayiniz...")

def karişitir(x):
    say=1
    random.shuffle(x) # listeye eklenen kullanıcıları karıştırır

    for i in x:
        print(str(say)+"-Kullanici Adi:",i) # iki farklı veri tipi olduğu için hepsini str yaptık
        say+=1
    input("Devem etmek için enter tuşuna tiklayiniz...")   

while True:
    print("***Çekiliş Uygulamasina Hoşgeldiniz***")
    print("1-Kullanici Ekle\n2-Kullanici Gör\n3-Kullanici Kariştir\n4-Kullanicilari Seç")
    seçim=int(input("Lütfen yapmak istediğiniz işlemi giriniz:"))
    

    if seçim==1:
        kullanici_ekle(kullanicilar)

    elif seçim==2:
        kullanici_gör(kullanicilar)   

    elif seçim==3:
        karişitir(kullanicilar)    

    elif seçim==4:
        print("Kişi seçimi yapiliyor... ")
        time.sleep(2) # 2 saniye bekletme yapiyor
        seç(kullanicilar)
         
    else:
        print("Hatali giriş yaptiniz lütfen tekrar deneyiniz!!")   

























