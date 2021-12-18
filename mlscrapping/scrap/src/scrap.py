from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from threading import Thread
import pandas as pd
from produtoBuilder import ProdutoBuilder
from produto import Produto
from textStract import TextStract
import logging

class Scrap(Thread):

    def __init__(self, limit):
        Thread.__init__(self)
        self.__limit = limit

    @staticmethod
    def geradorUrl():
        urls=[]
        page = "https://celulares.mercadolibre.com.ar/celular-smarphones_NoIndex_True"
        for i in range(5):
            if(i==0):
                url = page
            else:
                resultado = (50 *(i-1)) + 51
                page = "_Desde_" + str(resultado) 
                url = "https://celulares.mercadolibre.com.ar/celular-smarphones{}_NoIndex_True".format(page)
            urls.append(url)
        return urls


    def getData(self):
        produtos = []
        urls = self.geradorUrl()
        for url in urls:
            print("page {} ".format(url))
                
            try:
                response = urlopen(url)
                logging.info("Requisicao..." + url)
            except:
                logging.error('URL INVALIDA!')
    

            html = response.read().decode('utf-8')
            soup = BeautifulSoup(html, 'html.parser')
            ol = soup.find_all('ol', {'class': ['ui-search-layout', 'ui-search-layout--stack']})
        
            for li in ol:
                for li in li.findAll('li', {'class':['ui-search-layout__item']}):
                
                    
                    produtoBuilder = ProdutoBuilder() 
                  
                    produtoBuilder.com_titulo(li.h2.getText())
                    
                    produto = produtoBuilder.build()
                
                    produtos.append(produto)
                 
        df = pd.DataFrame([t.__dict__ for t in produtos ])
        df.to_csv('dataset.csv', sep=';', index = False, encoding = 'utf-8-sig')
        
   

    def run(self):
        self.getData()