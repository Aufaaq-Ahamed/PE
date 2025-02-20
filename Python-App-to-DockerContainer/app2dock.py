import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url)
# response.raise_for_status()  

soup = BeautifulSoup(response.content, 'html.parser')

countries_divs = soup.find_all('div', class_='col-md-4 country')

countries_data = []

for country_div in countries_divs:
    name = country_div.find('h3', class_='country-name').text.strip()
    capital = country_div.find('span', class_='country-capital').text.strip()
    population = int(country_div.find('span', class_='country-population').text.strip().replace(',', ''))
    area = float(country_div.find('span', class_='country-area').text.strip().replace(',', ''))

    population_density = population / area if area != 0 else 0

    countries_data.append({
        'Name': name,
        'Capital': capital,
        'Population': population,
        'Area': area,
        'Population Density': population_density
    })

df = pd.DataFrame(countries_data)
df.to_csv('random_countries_with_density.csv', index=False)
print(countries_data)
