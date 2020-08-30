# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 18:58:44 2019

@author: GOVIND A M
"""

import requests
from bs4 import BeautifulSoup
import xlsxwriter
book=xlsxwriter.Workbook('torr_data_comments_100.xlsx')
sheet=book.add_worksheet()
nofepi=7
def write_mag(url):
  page=requests.get(url)
  page_soup=BeautifulSoup(page.content)
  mag_img=page_soup.find('img',src="https://dyncdn.me/static/20/img/magnet.gif")
  sheet.write(j,2,mag_img.previous_element['href'])
  
for j in range(1,nofepi+1):
  url='https://rarbgunblock.com/torrents.php?search='+'true+detective+s03e'+format(j,'02')+'&category%5B%5D=18&category%5B%5D=41&category%5B%5D=49'
  df=requests.get(url)
  soup = BeautifulSoup(df.content)
  torr_list=soup.find_all('tr',class_='lista2')
  sizelist=list(torrent.find_all('td')[3].text for torrent in torr_list)
  un_conv_list=list(item.split(' ')[0] for item in sizelist)
  gb_mb=list(item.split(' ')[1] for item in sizelist)
  for i in range(0,len(gb_mb)):
    un_conv_list[i]= float(un_conv_list[i])*1024 if gb_mb[i]=='GB' else float(un_conv_list[i])
  min_size=min(un_conv_list)  
  title=torr_list[un_conv_list.index(min_size)].find_all('td')[1].a['title']
  torrent_link='https://rarbgunblock.com'+torr_list[un_conv_list.index(min_size)].find_all('td')[1].a['href']
  sheet.write(j,0,title)
  sheet.write(j,1,torrent_link)
  write_mag(torrent_link)
  sheet.write(j,3,min_size)
book.close()
    
  
    