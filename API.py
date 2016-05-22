#!/usr/bin/env python3

# première tentative de documenter l'API de coco.fr

import random
import requests

pseudo = "caecilius" # doit être en minuscule et de plus de 4 caractères
age = "22"           # minimum "18"
sexe = "1"           # "1" pour homme, "2" pour femme

codeville = "30929"  # à récuperer ici http://coco.fr/cocoland/foo.js par exemple pour Paris 15 :
                     # http://coco.fr/cocoland/75015.js va donner "var cityco='30929*PARIS*'; procecodo();"
                     # le codeville est donc "30929"

referenz = "0"       # aucune idée de ce que ça fait, pour l'instant la valeur est toujours "0"

salt = str(random.randrange(100000000, 999999999))

url = str("http://coco.fr#" + pseudo + "_" + sexe + "_" + age + "_" + codeville + "_0_" + salt + "_" + referenz)

r = requests.get(url)
