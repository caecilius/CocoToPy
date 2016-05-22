#!/usr/bin/env python3

# première tentative de documenter l'API de coco.fr

import random
import requests
import re

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

# séparer la valeur "avatar" de la valeur "pass"
avatar = re.match(r'\d*', cookie).group(0)     # récuperer la suite de chiffres au début de la chaine
pass = re.match(r'\d*(\D*)', cookie).group(1)  # récuperer la chaine de caractères juste après

ip = " 62.210.198.99"      # pas certain si c'est la bonne ip
                           # autres IP : 94.23.213.192, 95.211.153.95, 87.98.168.15, 91.121.55.112, 87.98.162.169

url2 = str(ip + pseudo + "*" + age + sexe + codeville + avatar + "0" + pass + "?" + salt)

r = requests.get(url2)
