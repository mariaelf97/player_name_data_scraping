import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://www.soccerdonna.de/en/NOT-IMPORTANT/profil/spieler_{number}.html"

data = []

# Loop through the range of player numbers
for number in range(450,650 ):  # <-- increase number here for more players
    url = base_url.format(number=number)
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    name = soup.select_one(".tabelle_spieler h1")
    webpage_url = url
    name = name.text.strip()

    for tr in soup.select(".tabelle_grafik .tabelle_spieler tr"):
        k, v = [
            td.get_text(strip=True, separator=" ").strip(":") for td in tr.select("td")
        ]
        # Append the data to the list
        data.append({'value': v, 'columns': k, 'name': name})

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)
df = df.drop_duplicates()
df = df.pivot(index='name', columns='columns', values='value')
df = df.query('Nationality=="Jamaica" or "Place of birth"=="Jamaica"')
df.to_csv('player_names.csv')
