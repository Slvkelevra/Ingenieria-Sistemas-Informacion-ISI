# -*- coding: utf-8 -*-
"""
@author: Alvaro
"""

import requests
from bs4 import BeautifulSoup

# Dirección de la página web
url = "https://www.librovicios.com/"
# Ejecutar GET-Request
response = requests.get(url)
# Analizar sintácticamente el archivo HTML
html = BeautifulSoup(response.text, 'html.parser')

# Guardamos como listas el nombre y el precio, por ejemplo
nombre = html.select('div.col.col-description > h3 > a')
precios = html.select(' div.col-12.col-sm-auto.col-buy > div.product-price-and-shipping > span')
autor = html.select('div.col.col-description > div.features > b:nth-child(2) > u > a')

# Mostramos los datos extraidos
for i in range(len(nombre)):
    print(nombre[i].getText()," | ", precios[i].getText(), " | " ,autor[i].getText())

