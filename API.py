#!/usr/bin/env python3

import random
import requests
import re

# Génération des valeurs aléatoires

Salt   = str(random.randrange(19939050, 99939050))
Salt2  = str(random.randrange(19939050, 99939050))
Avatar = str(random.randrange(164249067, 964249067))

# Atribution des variables utilisateur

Pseudo      = "Caecilius"  # Minimum 4 caractères
Age         = "18"         # Minimum 18
Sexe        = "1"          # 1 pour homme et 2 pour femme
CodePostal  = "69005"      # Uniquement en France

# Récupération du CodeVille

r = requests.get(str("http://coco.fr/cocoland/" + CodePostal + ".js"))
CodeVille = re.search(r'(\d+)', r.text).group(1)

# Génération de l'URL

URL = str("http://87.98.162.169/40" \
+  Pseudo + "*" + Age + Sexe + CodeVille + Avatar + "0?" + Salt + "." + Salt2)

# Envoie de la requête GET

r = requests.get(URL)

# Récupération des variables d'identification avec des regex

Identifiant = re.search(r'#\d{2}(\d{6})', r.text).group(1)
ServeurPass = re.search(r'#\d{2}\d{6}(\D{6})', r.text).group(1)

# Récupération de l'IP externe

r = requests.get(r'http://jsonip.com')
IpExterne = r.json()['ip']

# TODO
# Fonction pour chiffrer l'URL (https://bpaste.net/show/9744211f8e4e)
# Génération de l'URL chiffrée
# Envoie de la requête GET
# Formatage de la réponse
