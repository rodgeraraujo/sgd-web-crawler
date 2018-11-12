
import requests
from bs4 import BeautifulSoup


def imprimeInfo(titulo, resumo, autor, imagem, link):
    print "Titulo: " + titulo.text.lstrip() + "\n"
    print "Resumo: " + resumo.string + "\n"
    print "Autor: " + autor.string + "\n"
    print "Imagem: " + imagem + "\n"
    print "Link: " + link + "\n"
    print "--------------------------------------------------------------------------\n"


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

            imprimeInfo(titulo, resumo, autor, imagem, link)


url = 'https://www.nytimes.com/topic/destination/brazil'
crawlerWebPage(1, url)
