import requests
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    soup=soup.find_all('div',class_="column is-half")

    for card in soup:
        print("Job Name:"+card.h2.text)
        print("Company:"+card.h3.text)
        print("Location:"+str(card.p.text).strip())
        print("Time:"+card.time.text)
        print("--------------------------")
    
else:
    print("İstek başarısız oldu. Hata kodu:", response.status_code)
