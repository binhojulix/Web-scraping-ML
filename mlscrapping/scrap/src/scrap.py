# Importando bibliotecas
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pandas as pd



# Declarando variável cards
cards = []

## Obtendo o HTML e o total de páginas
url = "https://celulares.mercadolibre.com.ar/celular-smarphones_NoIndex_True"
response = urlopen(url)
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

num_pages = 5
num_items = 50
current_page = 1

 
response = urlopen(url)
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
print(url)
ol = soup.find_all('ol', {'class': ['ui-search-layout', 'ui-search-layout--stack']})

for li in ol:
    
    for li in li.findAll('li', {'class':['ui-search-layout__item']}):
        card={}
    

     
        card['titulo'] =  li.h2.getText()
        card['preco'] = li.findAll('span', {'class': ['price-tag-fraction']})[0].getText()
        
        
        amounts = li.findAll('span', {'class':['ui-search-reviews__amount']})
        for amount in amounts:
            if(not amount.getText()):
                card['reviews__amount'] ='0'
            else:
                card['reviews__amount'] = amount.getText()

        fretes = li.findAll('p', {'class': ['ui-search-item__shipping', 'ui-search-item__shipping--free']})
        for frete in fretes:
            if(not frete.getText()):
                card['frete'] ='0'
            else:
                card['frete'] = frete.getText()
                
                
                
                
                
        cores = li.findAll('span', {'class': ['ui-search-item__group__element', 'ui-search-item__variations-text']})
        for cor in cores:
            if(not cor.getText()):
                card['cores_disponiveis'] ='0'
            else:
                card['cores_disponiveis'] = cor.getText()

                
            
        cards.append(card)
       # print(cards)
      

    dataset = pd.DataFrame(cards)
    dataset.to_csv('dataset.csv', sep=';', index = False, encoding = 'utf-8-sig')