import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

import time
import selenium
# import undetected_chromedriver as uc
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

opcijos = Options()
opcijos.add_argument('--incognito')
# opcijos.add_argument('--headless')

# driver = uc.Chrome(options=opcijos)
driver = webdriver.Firefox(options=opcijos)

# jūsų atrankoje, kiek automobilių buvo au atomatu, mech, kokios jų buvo vidutinės kainos?
#advanced: su pie plot atvaizduokite gamintojų užimamą rinkos dalį (5 didžiausi + visi kiti)

pavadinimai = []
pagaminimo_metai = []
#pavaru_dezes = []

for puslapis in range(1,2):
    url = f'https://autoplius.lt/skelbimai/naudoti-automobiliai?page_nr={puslapis}'
    driver.get(url)
    time.sleep(10)
    source = driver.page_source
    bs = BeautifulSoup(source, 'html.parser')
    SkelbimuSarasas = bs.find_all('div', {'class':'announcement-content'})

    for skelbimas in SkelbimuSarasas:
        try:            
            pavadinimas = skelbimas.find('div', {'class': 'announcement-title'}).text.strip()
            pavadinimai.append(pavadinimas)

            pagaminimo_data = skelbimas.find('div', {'class': 'announcement-parameters'}).text.strip()[:4]
            pagaminimo_metai.append(pagaminimo_data)

            pavaru_deze = skelbimas.find('div', {'class':'announcement-parameters-block'}).find('div', {'class': 'announcement-parameters'}).text.strip().replace('\n', '').replace('   ', '').split()[1]


            bendras = skelbimas.find('div', {'class':'announcement-parameters-block'}).find('div', {'class': 'announcement-parameters'}).text.strip().replace('\n', ' ').replace('   ', '')
           
            #kint = skelbimas.find('div', {'class':'announcement-parameters-block'}).find('div', {'class': 'announcement-parameters'}).text.strip().replace('\n', ';').replace('   ', '')


            print(pavadinimas)
            print(pagaminimo_data)
            print(pavaru_deze)
            print(bendras)
            #print(kint)
            print('-------------------KITAS------------------------')
        


#             addres_element  = skelbimas.find('div', {'class':'list-adress-v2'})
#             tag = addres_element.find('h3').find('a', href=True)
#             linkas = tag['href']
#         # tekstą galima pasiekti ir per 
#         # .contents atributą
#             tekstas = tag.contents #jums gražina list objektą su teksto gabalais
#             f = ''
#             for i in tekstas:
#                 f = f + str(i).strip() # str - kad garantuotai būtų tekstas
#             adresas = f.replace('<br/>', ', ')

#             kainaRaw = addres_element.find('div', {'class':'price'}).find('span', {'class':'list-item-price-v2'})
#             kainaFloat = float(kainaRaw.text.strip().replace(' ', '').replace('€', ''))
            
#             kaina_uz_m2Raw = addres_element.find('div', {'class':'price'}).find('span', {'class':'price-pm-v2'})
#             kaina_uz_m2Float = float(kaina_uz_m2Raw.text.replace('\n', '').replace(' ', '').replace('€/m²', ''))
            
#             plotasRaw = skelbimas.find('div', {'class':'list-AreaOverall-v2'})
#             plotasFloat = float(plotasRaw.text.strip().replace(' ', '').replace('m²', ''))

#             kambariaiRaw = skelbimas.find('div', {'class':'list-RoomNum-v2'})
#             kambariaiFloat = float(kambariaiRaw.text.strip().replace(' ', '').replace(' kamb.', ''))
#             Kambariu_skaicius.append(kambariaiFloat)
#             Adresas.append(adresas)
#             Kaina.append(kainaFloat)
#             Kaina_uz_m2.append(kaina_uz_m2Float)
#             Plotas.append(plotasFloat)
        except Exception as klaida:
            print(klaida)
#     # time.sleep(np.random.randint(10,100))
#     time.sleep(5)
driver.close()