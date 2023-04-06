import requests
from bs4 import BeautifulSoup

def parse_ukd_data():
    url = "https://ukd.edu.ua/"
    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')
    specialities = soup.find('a', string='Спеціальності').parent.find_all('li')

    for speciality in specialities:
        print(speciality.text.strip())

parse_ukd_data()