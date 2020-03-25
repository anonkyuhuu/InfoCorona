# coding=utf-8

'''
Author : sCuby07
Fungsi : Get Data Corona
Versi  : 0.1

Jangan recode ya kontol codingan gue ga rapih
'''

import requests,os,runtext,sys,time

os.system('clear')
url = 'https://api.kawalcorona.com/{}'

def provinsi():
 res = requests.get(url.format('indonesia/provinsi')).json()
 time.sleep(5)
 n = []
 for i in res:
  n.append(i['attributes'])
 for a in n:
  pv = a['Provinsi']
  print('\x1b[37m[~] Provinsi : '+pv)
  print('\x1b[37m[+] Positive : '+str(a['Kasus_Posi']))
  print('\x1b[37m[\x1b[32;1m*\x1b[37m]\x1b[32;1m Sembuh : '+str(a['Kasus_Semb']))
  print('\x1b[37m[\x1b[31m×\x1b[37m]\x1b[31m Meninggal : '+str(a['Kasus_Meni'])+'\x1b[37m')


if __name__ == '__main__':
 print('''\x1b[32;1m ▄▄·       ▄▄▄         ▐ ▄  ▄▄▄· 
▐█ ▌▪▪     ▀▄ █·▪     •█▌▐█▐█ ▀█ 
██ ▄▄ ▄█▀▄ ▐▀▀▄  ▄█▀▄ ▐█▐▐▌▄█▀▀█ 
▐███▌▐█▌.▐▌▐█•█▌▐█▌.▐▌██▐█▌▐█ ▪▐▌
·▀▀▀  ▀█▄▀▪.▀  ▀ ▀█▄▀▪▀▀ █▪ ▀  ▀ \x1b[37m0.1
''')
 runtext.runtext('''\x1b[37m[!] Melakukan Requests => \x1b[32;1mSukses
\x1b[37m[!] Mengambil Data => \x1b[32;1mSukses\x1b[37m\n''',0.1)
 provinsi()
