import requests
from bs4 import BeautifulSoup

def salvaEmTXT(titulo, resumo, autor, imagem, link):
    filePath = "newsText.txt"
    file = open('newsText.txt', 'a')   
    file.write(
        "Titulo: " + titulo.text.lstrip() + "\n" + 
        "Resumo: " + resumo.string + "\n" + 
        "Autor: " + autor.string + "\n" + 
        "Imagem: " + imagem + "\n" + 
        "Link: " + link + "\n" + 
        "--------------------------------------------------------------------------\n")
    file.close()

def imprimeTXT():
    f = open('newsText.txt','r')
    newsText = f.read()
    print(newsText)
    f.close()

def crawlerWebPage(pagina, paginaUrl):
    if(pagina > 0):
        codigo = requests.get(paginaUrl)
        paginaHTML = BeautifulSoup(codigo.content, "html.parser")

        for noticia in paginaHTML.findAll('article', {'itemtype': 'http://schema.org/NewsArticle'}):
            titulo = noticia.find('h2', {'class': 'headline'})
            resumo = noticia.find('p', {'itemprop': 'description'})
            autor = noticia.find('p', {'itemprop': 'author'})
            imagem = noticia.find('img', {'role': 'presentation'}).get('src')
            link = noticia.find('a', {'class': 'story-link'}).get('href')

            salvaEmTXT(titulo, resumo, autor, imagem, link)
            imprimeTXT()


url = 'https://www.nytimes.com/topic/destination/brazil'
crawlerWebPage(1, url)
