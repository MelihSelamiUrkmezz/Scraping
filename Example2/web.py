from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    data=[]
    base_url='https://ciceksepeti.com'
    for page in range(1,2):
        url = 'https://www.ciceksepeti.com/cep-telefonu?page='+str(page)
        HEADERS=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'})
        response = requests.get(url,headers=HEADERS)

        if response.status_code==200:
            soup=BeautifulSoup(response.content,'html.parser')
            links=soup.find_all('div',attrs={'class':'products__container-background'})
            
            for link in links:
                telephone_link=base_url+str(link.find_all('a')[0].get('href'))
                telephone_title=link.find_all('img')[0].get('alt')
                telephone_image=link.find('img').get('data-src')
                telephone_url=requests.get(telephone_link,headers=HEADERS)
                soup=BeautifulSoup(telephone_url.content,'html.parser')
                telephone_price=soup.find_all('div',attrs={'class':'product__info__new-price__integer js-price-integer'})[0].text
                product_code=soup.find('div',attrs={'class':'product__code'}).text.split(' ')[-1]
                single_data={
                    "telephone_image": telephone_image,
                    "telephone_title": telephone_title,
                    "product_code": product_code,
                    "telephone_price": telephone_price,
                    "telephone_link": telephone_link
                }
                data.append(single_data)
    return render_template('card.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)