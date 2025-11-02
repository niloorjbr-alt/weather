import requests
from bs4 import BeautifulSoup as bs

def get_wetter():
    page = requests.get('https://khabarfarsi.com/weather')

    if page.status_code !=200:
      return None
    soup = bs(page.text , "html.parser")
    cities = soup.find_all("div", class_="weather_cityname")
    min_temps = soup.find_all("div", class_="weather_temp_min")
    max_temps = soup.find_all("div", class_="weather_temp_max")
    
    weather_data = {}

    for i in range(len(cities)):
        city= cities[i].text.strip()
        min_temp = min_temps[i].text.strip() if i < len(min_temps) else "-"
        max_temp = max_temps[i].text.strip() if i < len(max_temps) else "-"
        weather_data[city] = {"min": min_temp, "max": max_temp}

    return weather_data
       
      
       
  