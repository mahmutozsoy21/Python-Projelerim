import requests
from bs4 import BeautifulSoup
url=requests.get("https://covid19.saglik.gov.tr/")

if url.status_code==200:
    print("Siteden veri çekilebilir")
else:
    print("Siteden veri çekilemez") 


soup=BeautifulSoup(url.content,"html.parser")


yazdir=soup.head.title

print(yazdir)

        












































