#!/usr/bin/env python3

# Documentation de l'API de coco.fr
# Version 2
# En cours d'écriture, non fonctionnelle pour l'instant
# Nécessite le module requests

import random
import requests
import re

# Génération des valeurs aléatoires

salt   = str(random.randrange(19939050, 99939050))
salt2  = str(random.randrange(19939050, 99939050))
avatar = str(random.randrange(164249067, 964249067))

# Atribution des variables utilisateur

pseudo       = "Caecilius"  # Minimum 4 caractères
age          = "18"         # Minimum 18
sexe         = "1"          # 1 pour homme et 2 pour femme
code_postal  = "69005"      # Uniquement en France

# Récupération du code_ville

r = requests.get(str("http://coco.fr/cocoland/" + code_postal + ".js"))
code_ville = re.search(r'(\d+)', r.text).group(1)

# Génération de l'URL

serveur_url = str("http://87.98.162.169/40" \
+  pseudo + "*" + age + sexe + codeVille + avatar + "0?" + salt + "." + salt2)

# Envoie de la requête GET

r = requests.get(serveur_url)

# Récupération des variables d'identification avec des regex

Identifiant = re.search(r'#\d{2}(\d{6})', r.text).group(1)
ServeurPass = re.search(r'#\d{2}\d{6}(\D{6})', r.text).group(1)

# Récupération de l'IP externe

r = requests.get(r'http://jsonip.com')
IpExterne = r.json()['ip']

# TODO
# Fonction pour chiffrer l'URL (https://bpaste.net/show/f5afa3a02692)
# Génération de l'URL chiffrée
# Envoie de la requête GET
# Formatage de la réponse
