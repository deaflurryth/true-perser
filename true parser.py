# coding=utf-8
import requests
import time
from bs4 import BeautifulSoup
from lxml import html
base_url= 'https://kinoteatr.ru'
url_baza= ['https://kinoteatr.ru/raspisanie-kinoteatrov/shchelkovsky/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/chertanovo/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/cdm/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/mega-himki/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/filion/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/tepliy-stan/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/city/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/semenovsky/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/rivera/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/5avenu/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/polezhaevskiy/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/oblaka/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/mozhayka/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/michurinsky/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/metropolis/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/lefortovo/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/ladoga/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/kutuzovskiy/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/kaluzhskij/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/zelenopark/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/evropa/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/global-city/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/waypark/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/butovo-mall/?day=tomorrow',
           'https://kinoteatr.ru/raspisanie-kinoteatrov/belaya-dacha/?day=tomorrow'
           ]
r= requests.get(f'{base_url}/raspisanie-kinoteatrov')
j= requests.get(f'{base_url}/kinoafisha')
soap= BeautifulSoup(r.text, 'lxml')
cinemas= []
for inf in soap.findAll('div', class_='col-md-12 cinema_card'):
    name1= inf.find('h3').text.strip()
    href1= inf.find('a')['href'].strip()
    address1= inf.findAll('span', class_='sub_title')[0].text.strip()
    cinemas.append({
        'name': name1,
        'href': href1,
        'address': address1
    })
    #print(name, href, address, sep='\n', end='\n---------------------\n')
#print(sorted(cinemas), sep="\n")
for inf, cinema in enumerate(cinemas):
    r= requests.get(cinema['href'])
    soap= BeautifulSoup(r.text, 'lxml')
    films= soap.findAll('div', class_='shedule_movie bordered gtm_movie')
    films_dict= []
    for film in films:
        films_dict.append({
        'name':film['data-gtm-list-item-filmname'],
        'href': film.find('a', class_='gtm-ec-list-item-movie')['href'],
        'format': film['data-gtm-format'],
        'genre': film['data-gtm-list-item-genre'],
        'raiting_sub': film.findAll('i', class_='raiting_sub')[0].text.strip(),
        'table': film.findAll('span', class_='shedule_session_time')
        })
cinemas[inf]['films']= films_dict

s= BeautifulSoup(r.text, 'lxml')
a= requests.get(f'{base_url}/raspisanie-kinoteatrov/"url_baza"/?day=tomorrow')
kino= []
for infk, tomk in enumerate(kino):
    a= requests.get(tomk['href'])
    films1= s.findAll('div', class_='shedule_movie bordered gtm_movie')
    tomkino= []
    for kino1 in films1:
        kino_dict.append({
            'name1':kino1['data-gtm-list-item-filmname'],
            'href1': kino1.find('a', class_='gtm-ec-list-item-movie')['href'],
            'format1': kino1['data-gtm-format'],
            'genre1': kino1['data-gtm-list-item-genre'],
            'raitingsub1': kino1.findAll('i', class_='raitingsub')[0].text.strip(),
            'raspisanie1': kino1.findAll('span', class_='shedule_session_time')
        })
    kino[infk]['films1']= toomkino
#print(films_dict, sep=', ', end='\n')
#print(cinemas, sep=', ', end='\n')
print(cinemas)
print(kino)

