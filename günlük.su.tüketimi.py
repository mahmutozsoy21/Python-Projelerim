# bir insanin günlük içmesi gereken su miktari kilo*0.03 tür

def su_hesapla(kilo):
  e_hesapla=float(kilo*0.04)
  k_hesapla=float(kilo*0.03)
  
  cinsiyet=input("lütfen cinsiyetinizi giriniz:Kadin\Erkek:").lower() # girilen kelimenin tüm harflerini küçük yapar

  if cinsiyet =="erkek":
    print("cinsiyetiniz:",cinsiyet)
    print(e_hesapla,"litre su içmelisiniz...")
 

  elif cinsiyet=="kadin":
    print("cinsiyetiniz:",cinsiyet)
    print(k_hesapla,"litre su içmelisiniz")

  elif not cinsiyet:
    print("bu alan boş birakilamaz lütfen cinsiyetinizi seçiniz")
  else:
    print("hatali giriş yaptiniz")

kilo_al=int(input("lütfen kilonuzu giriniz:"))
     
su_hesapla(kilo_al)










































