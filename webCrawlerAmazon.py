
import requests
from bs4 import BeautifulSoup
def webpage(pagina,paginaUrl):
    if(pagina>0):
        url = paginaUrl
        codigo = requests.get(url)
        plain = codigo.text
        codigoHtml = BeautifulSoup(plain, "html.parser")
        for link in codigoHtml.findAll('a', {'class':'s-access-detail-page'}):
            conteudo = link.get('title')
            print('Nome: ' + conteudo)
            conteudo_2 = link.get('href')
            print('Link: ' + conteudo_2)
            print("")

url1 = 'https://www.amazon.com/s/ref=nb_sb_ss_c_1_9?url=search-alias%3Daps&field-keywords=j+r+r+tolkien&sprefix=j+r+r+tol%2Caps%2C217&crid=3PDZI2FLKJ0HW'
url2 = 'https://www.amazon.com/b/ref=sr_aj?node=16197&ajr=2' 

webpage(1, url2)