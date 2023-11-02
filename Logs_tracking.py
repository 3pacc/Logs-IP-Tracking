import re
import os
from geoip import geolite2

data = r'(\w{3} \d{2} \d{2}:\d{2}:\d{2}).*rhost=([\d\.]+)'
failures = []

# Ouvrir le fichier journal en mode lecture
with open(r"C:\Users\3pac\Desktop\esisalog.py\secure-20220306", "r") as file:
    for line in file:
        match = re.search(data, line)
        if match:
            timestamp, ip_address = match.groups()
            failures.append((timestamp, ip_address))

# Pour chaque adresse IP extraite, effectuer la géolocalisation avec python-geoip-geolite2
for failure in failures:
    timestamp, ip_address = failure
    match = geolite2.lookup(ip_address)
    if match is not None:
        country = match.get("country", "Inconnu")
        city = match.get("city", "Inconnue")

        print(f"Date/Time: {timestamp}, IP Address: {ip_address}, Country: {country}, City: {city}")

# Fermer la base de données GeoLite2
geolite2._close()



