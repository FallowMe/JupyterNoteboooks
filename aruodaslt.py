import selenium
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time # dėl sleep komandos
import pandas as pd

opcijos = Options()
opcijos.add_argument('--incognito')

driver = uc.Chrome(options=opcijos)

url = "https://www.kaunodiena.lt"

driver.get(url)
time.sleep(3)

source = driver.page_source # pasiimam puslapio html kodą

bs = BeautifulSoup(source, 'html.parser')  # teoriskai isparsiname puslapio html
ResultsSet = bs.find_all('a', {'class':'articles-list-title'}) # skanuoja visa koda ir iesko simbolio 'a' 

sarasas = []

for elementas in ResultsSet:
    # print('::ELEMENTAS::')
    # print(elementas)
    # print(elementas['href'])   # ['href'] is atrinktos kalses leidzia gauti linka (nuoroda, adresa)
    # print(elementas.text)  # pasiekiame elemente esanti teksta, siuo atveju straipsnio pavadinima
    sarasas.append(elementas.text)


dfSarasas = pd.DataFrame()
dfSarasas['Pavadinimas'] = sarasas
dfSarasas.to_csv('KD strapsniu pav.csv', sep=';')


#Surinkite visus kauno dienos straipsnių pavadinimus į pandas dataframe.
#pridėkite naują stulpelį, kuriame būtų žodžių kiekis kiekviename pavadinime
#pridėkite naują stulpelį, kuriame būtų pavadinime esančių simbolių kiekis
#eksportuokite tai į CSV failą


# df = pd.DataFrame()
# df['a'] = np.random.randint(10,50,10)
# df.to_csv('demoDF.csv', sep=';')

# driver.close()