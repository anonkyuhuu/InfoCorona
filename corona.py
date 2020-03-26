# coding=utf-8
'''
Author : sCuby07
Fungsi : Get Data Corona
Versi  : 0.3 (Latest Update)

Jangan recode ya kontol codingan gue ga rapih
'''

import requests,os,runtext,sys,time,re
from difflib import get_close_matches as src

os.system('clear')
url = 'https://{}'

def indonesia():
 res = requests.get(url.format('api.kawalcorona.com/indonesia/provinsi')).json()
 time.sleep(5)
 b = requests.get(url.format('api.kawalcorona.com/indonesia')).json()
 for x in b:
  runtext.load('\x1b[37m[+] Positive : '+x['positif'])
  runtext.load('\x1b[37m[\x1b[32;1m*\x1b[37m]\x1b[32;1m Recover : '+x['sembuh'])
  runtext.load('\x1b[37m[\x1b[31m-\x1b[37m]\x1b[31m Died : '+x['meninggal'])
  time.sleep(3)
 ask = raw_input('\x1b[37mTampilkan Wilayah (y/n) ')
 if 'y' in ask:
  n = []
  for i in res:
   n.append(i['attributes'])
  for a in n:
   pv = a['Provinsi']
   print('\x1b[37m[~] Province : '+pv)
   print('\x1b[37m[+] Positive : '+str(a['Kasus_Posi']))
   print('\x1b[37m[\x1b[32;1m*\x1b[37m]\x1b[32;1m Recover : '+str(a['Kasus_Semb']))
   print('\x1b[37m[\x1b[31m-\x1b[37m]\x1b[31m Died : '+str(a['Kasus_Meni'])+'\x1b[37m')
 if 'n' in ask:
  exit()

def all_country():
 p = requests.get(url.format('api.kawalcorona.com')).text
 cnt = re.findall('"Country_Region":"(.*?)"',p)
 while True:
  mm = raw_input('Negara : ')
  wrl = "".join(src(mm,cnt,n=1,cutoff=0))
  t= r'{"OBJECTID":.*?,"Country_Region":"'+wrl+'","Last_Update":.*?,"Lat":.*?,"Long_":.*?,"Confirmed":(.*?),"Deaths":(.*?),"Recovered":(.*?),"Active":.*?}}'
  xx = re.search(t,p)
  print('\n{} Info'.format(wrl))
  print('''\x1b[37m[+] Positive : {}
\x1b[37m[\x1b[32;1m*\x1b[37m]\x1b[32;1m Recover : {}
\x1b[37m[\x1b[31m-\x1b[37m]\x1b[31m Died : {}\x1b[37m'''.format(xx.group(1),xx.group(2),xx.group(3)))

def main():
 print('''1. Indonesian Status
2. All Country Status
''')
 while True:
  nanya = int(raw_input('Country >> '))
  if nanya == 1:
   indonesia()
  if nanya == 2:
   all_country()

if __name__ == '__main__':
 os.system('clear')
 print('''\x1b[32;1m ▄▄·       ▄▄▄         ▐ ▄  ▄▄▄·
▐█ ▌▪▪     ▀▄ █·▪     •█▌▐█▐█ ▀█
██ ▄▄ ▄█▀▄ ▐▀▀▄  ▄█▀▄ ▐█▐▐▌▄█▀▀█
▐███▌▐█▌.▐▌▐█•█▌▐█▌.▐▌██▐█▌▐█ ▪▐▌
 ▀▀▀  ▀█▄▀▪.▀  ▀ ▀█▄▀▪▀▀ █▪ ▀  ▀ \x1b[37mv0.3
''')
 main()
