#!/usr/bin/env python3

# première tentative de documenter l'API de coco.fr

import random
import requests
import re

r = requests.get(r'http://jsonip.com')
IPlocale = r.json()['ip']

pseudo = "caecilius" # doit être en minuscule et de plus de 4 caractères
age = "22"           # minimum "18"
sexe = "1"           # "1" pour homme, "2" pour femme

ville = "PARIS"      # voir en dessous pour obtenir le nom de la ville 
codeville = "30929"  # à récuperer ici http://coco.fr/cocoland/foo.js par exemple pour Paris 15 :
                     # http://coco.fr/cocoland/75015.js va donner "var cityco='30929*PARIS*'; procecodo();"
                     # le codeville est donc "30929"

referenz = "0"       # aucune idée de ce que ça fait, pour l'instant la valeur est toujours "0"

salt = str(random.randrange(100000000, 990000000)) # nombre aléatoir entre 100000000 et 990000000

url = str("http://www.coco.fr/chat/index.html#" \
+ pseudo + "_" + sexe + "_" + age + "_" + codeville + "_0_" + salt + "_" + referenz)

r = requests.get(url)

# récupérer la valeur du cookie d'identification "samedi"
cookie = r.cookies['samedi']

# séparer la valeur "avatar" de la valeur "cookiepass"
avatar = re.match(r'\d*', cookie).group(0)           # récuperer la suite de chiffres au début de la chaine
cookiepass = re.match(r'\d*(\D*)', cookie).group(1)  # récuperer la chaine de caractères juste après

ip = "62.210.198.99"      # pas certain si c'est la bonne ip
                          # autres IP : 94.23.213.192, 95.211.153.95, 87.98.168.15, 91.121.55.112, 87.98.162.169

url2 = str(ip + "/22#" + pseudo + "*" + age + sexe + codeville + avatar + "0" + cookiepass + "?" + salt)

r = requests.get(url2)

# réponse du serveur à passer dans des regex pour récuperer nickid et serveur_pass
serveur_answer = r.text

"""
exemple de serveur_answer

process1('#15238436uQzGlwASMDPAsSATBeKBekSGFBIAaDFH8fPW   "#15" ?  
JKRgonIXWEGdamMWIeATWfKeQUBhWBLWpVEZQOJaIiDDxHUbxUEZQOJ   nickid = 6 premiers chiffres  (dans l'exemple "238436")
aIiDDxHLXxMED0JIawUE3anIXWggz4DKfFKRhWnIXWggz4DKfEUBgoH   serveur_pass = 6 caractères juste après (dans l'exemple "uQzGlw")
lbmKFZAOJARVBD0llXmQECelkQMOGGxKVAsSATBeKBejSGFBOXWFDCo
nIXWggz4DP1FHTZiVMw1jGYWlUZQvPhanIXWggzIlKRogBd8OKCWgAT
AvFSBVhH1KPy01NXfTkRWiJYeILWIQhgJMlbmKFZAOJARVBDellXmQE
CelkQMOFGxnIWaSecoHMx4ODYmlNewPSD8lMQeQFCefNeIHGSQnLWIE
gz0VKQsDHgoMJX5hFZAgJFFff2omKB5VAzAIjwfKRgoTUxRMHHpRlW8
gGTJRUWIgAzWnJXWiB38KKxaQHD8JHAeqgz8lKWbmGzAMLWsgAT4IkR
wlADiTKR8sHAxeIwaEFYMTNxWUGZ9BIAaDFH8fPWRKEZQOLw0EHhajJ
WAehGoHJA0DFZbSNWWghConIXWggz4DL1FHTYwIIWmghhXBNAaDITWh
IWMCAhamMWIeATWfKeRUDZiPMEQSGyafl05EQGRilB8eBzQVKeIgAzA
TKzsUESeSlE5fhYiTKQWiAd8JJB4SED9eJXogHD0yIWeQHSfRjejfhZ
iVMw1jGYWClE5nf3onIXWggz4DJanfh3NRIAaDFH8fPWRmf3tilAsSA
TBeKBekhdNQjemQECelkQMOG31iMZ0NMZ0NjeBHhHXBJXwHGSWVlwWi
FdXBIwMegz0VKQsDHgxMnfmKggJKn0fM');
"""

#Regex
nickid =       # ?
serveur_pass = # ?

url3 = str("35519201080" + "*" + "0" + "*" + "0" + "*" + "0" + "*" + "192.168.1.1" + "*" + IPlocale + serveur_pass)

r = requests.get(url3)
