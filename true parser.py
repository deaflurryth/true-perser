# coding=utf-8
import requests
import time
import urllib
from bs4 import BeautifulSoup
from lxml import html    #r= requests.get(f'{base_url}/raspisanie-kinoteatrov//?day=tomorrow')
from urllib import parse
base_url= 'https://kinoteatr.ru'
r= requests.get(f'{base_url}/raspisanie-kinoteatrov/')
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

tom= requests.get(f'{base_url}/raspisanie-kinoteatrov//?day=tomorrow')
soupb= BeautifulSoup(tom.text, 'lxml')
cinemat= []
for infl in soupb.findAll('div', class_='col-md-12 cinema_card'):
    nameb= infl.find('h3').text.strip()
    hrefb= infl.find('a')['href'].strip()
    addressb= infl.findAll('span', class_='sub_title')[0].text.strip()
    cinemat.append({
        'name': nameb,
        'href': hrefb,
        'address': addressb
    })
for infl, cinema in enumerate(cinemat):
    tom= requests.get(cinema['href'])
    soupb= BeautifulSoup(tom.text, 'lxml')
    filmt= soupb.findAll('div', class_='shedule_movie bordered gtm_movie')
    films_tom= []
    for film_ in filmt:
        films_tom.append({
        'name':film_['data-gtm-list-item-filmname'],
        'href': film_.find('a', class_='gtm-ec-list-item-movie')['href'],
        'format': film_['data-gtm-format'],
        'genre': film_['data-gtm-list-item-genre'],
        'raiting_sub': film_.findAll('i', class_='raiting_sub')[0].text.strip(),
        'table': film_.findAll('span', class_='shedule_session_time')
        })
cinemat[infl]['filmt']= films_tom
#print(films_dict, sep=', ', end='\n')
#print(cinemas, sep=', ', end='\n')
print(cinemas)
#print(films_dict)
print(cinemat)
