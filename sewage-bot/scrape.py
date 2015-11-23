#!/usr/local/bin/python2.7

import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'https://anrweb.vt.gov/DEC/WWInventory/SewageOverflows.aspx'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

table1 = soup.find('table', attrs={'class': 'dataList', 'id': 'body_GridViewSewageOverflowsUnOfficial'})
table2 = soup.find('table', attrs={'class': 'dataList', 'id': 'body_GridViewSewageOverflowsAuthorized'})
table3 = soup.find('table', attrs={'class': 'dataList', 'id': 'body_GridViewSewageOverflowsOther'})

list_of_rows1 = []
list_of_rows2 = []
list_of_rows3 = []
final_list = []

for row in table1.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows1.append(list_of_cells)

for row in table2.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows2.append(list_of_cells)

for row in table3.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows3.append(list_of_cells)

final_list = list_of_rows1 + list_of_rows2 + list_of_rows3

while [] in final_list:
    final_list.remove([])
    final_list.sort()

outfile = open('/home/vprnet/webapps/bots/bots/sewage-bot/sewage.csv', 'wb')
writer = csv.writer(outfile)
writer.writerow(["Index", "Start Date", "End Date", "Start/End Times", "Municipality", "Location", "Waterbody", "Description of Incident", "Estimated Volume (gallons)", "Wastewater Treatment Facility", "Contact Person"])
list = writer.writerows(final_list)
