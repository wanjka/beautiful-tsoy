from bs4 import BeautifulSoup as BSoup
import requests as req

from csv_writer import csv_writer

outfile = 'output.csv'

url = 'https://amdm.ru/akkordi/viktor_coi/'
resp = req.get(url)

if resp.status_code == 200:
    soup = BSoup(resp.text, 'lxml')
    links = soup.select_one('table#tablesort').select('a.g-link')
    links_text = (a.text for a in links)
    links_href = (a['href'] if a.get('href') else None for a in links)
    links_href = map(lambda href: f'https:{href}', links_href)
    fieldnames = ['song_name', 'link']
    csv_writer(fieldnames, zip(links_text, links_href), outfile)
    print('Success')
else:
    print(f'Error {resp.status_code}')

