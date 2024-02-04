import requests
from bs4 import BeautifulSoup
import json
import re

class WikipediaScraper:
    def __init__(self):
        self.base_url = "https://country-leaders.onrender.com"
        self.country_endpoint = "/countries"
        self.leaders_endpoint = "/leaders"
        self.cookies_endpoint = "/cookie"
        self.leaders_data = {}
        self.cookie = self.refresh_cookie() 

    def refresh_cookie(self):
        response = requests.get(self.base_url + self.cookies_endpoint)
        if response.status_code == 200:
            return response.cookies
        elif response.status_code == 403:
            print(f"Error code: {response.status_code}, Cookie is missing ")
            return self.cookie
        else:
            raise ValueError(f"Error code: {response.status_code}, Unexpected status code ")

    def get_countries(self):
        response = requests.get(self.base_url + self.country_endpoint, cookies=self.cookie)
        countries = response.json()

        if response.status_code == 200:
            return countries
        elif response.status_code == 403:
            print(f"Error code: {response.status_code}, Cookie is missing ")
            self.cookie = self.refresh_cookie()
            return self.get_countries()
        else:
            raise ValueError(f"Error code: {response.status_code}, Unexpected status code ")

    def get_leaders(self, country: str):
        param = {'country': country}
        response = requests.get(self.base_url + self.leaders_endpoint, cookies=self.cookie, params=param)
        leaders = response.json()

        if response.status_code == 200:
            self.leaders_data[country] = leaders

        else:
            raise ValueError(f"Error code: {response.status_code}, Unexpected status code ")

        
    

    def clean_paragraph(self, first_paragraph):
        patterns = [(r'\[.*?\]|\(.*?\)|<.*?>'), r"(\[|\/).+(\/|\])(.*;)?", r"\(?\w+ⓘ ?\)?"]

        cleaned_paragraph = first_paragraph

        for pattern in patterns:
            cleaned_paragraph = re.sub(pattern, '', cleaned_paragraph)
        return cleaned_paragraph   


    def get_first_paragraph(self, wikipedia_url: str):
        first_paragraph = ""
        response = requests.get(wikipedia_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = soup.find_all("p")
            for paragraph in paragraphs:
                if paragraph.find('b'):
                    first_paragraph = paragraph.text
                    break
            return first_paragraph
        else:
            print(f"Error code: {response.status_code} Cookie is missing ")
            self.cookie = self.refresh_cookie()

    def to_json_file(self, filepath: str):
        with open(filepath, 'w', encoding="utf-8") as json_file:
            json.dump(self.leaders_data, json_file, indent = 4, separators=(',', ': '), ensure_ascii=False)      
