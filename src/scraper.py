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
        self.leaders_info = {}
        self.cookie = self.refresh_cookie()

    def refresh_cookie(self):
        res_cookie = requests.get(f"{self.base_url}{self.cookies_endpoint}")
        return res_cookie

    def get_countries(self):
       
        res_country = requests.get(f"{self.base_url}{self.country_endpoint}", cookies=self.refresh_cookie().cookies)
        if res_country.status_code == 200:
            return res_country.json()
        
        elif res_country.status_code == 403:
            
            raise ValueError(f"Error code: {res_country.status_code}, Cookie is missing ")
            
        else:
            raise ValueError(f"Error code: {res_country.status_code}, Unknown Error ")

    def get_leaders(self, country:str):
      
        param = {'country': country}
        res_leaders = requests.get(f"{self.base_url}{self.leaders_endpoint}", cookies=self.refresh_cookie().cookies, params=param)
        
        if res_leaders.status_code == 200:
            leaders = res_leaders.json()

            for leader in leaders:

                self.leaders_info = {"first_name":leader["first_name"], "last_name":leader["last_name"], "birth_date": leader["birth_date"]
                                 , "wikipedia_url":leader["wikipedia_url"], leader_id : leader["id"]}


            self.leaders_info[country] = []

            def get_first_paragraph(wikipedia_url):
               """returns the first paragraph from the wikipedia url"""
            response = requests.get(wikipedia_url)
                soup = BeautifulSoup(response.content, "html.parser")
                # Find all paragraphs
                paragraphs = soup.find_all("p")
                for paragraph in paragraphs:
                    # Check if the paragraph starts with a <b> tag
                        if paragraph.find("b"):
                            return paragraph.text
                return "No paragraph with bold text found"

                    self.leaders_data[country].append(leader_info)
        elif res_leaders.status_code != 200:
            self.refresh_cookie()
            print("Cookies refreshed")

        else:
            raise ValueError(f"Failed to fetch leaders data for {country}. Status Code: {res_leaders.status_code}")


    def get_first_paragraph(self, wikipedia_url: str):
        
        first_paragraph = ""

    
        r = requests.get(f"{wikipedia_url}").text
        soup = BeautifulSoup(r, "html.parser")
        paragraphs = soup.find_all('p')
        for p in paragraphs:
            if p.find('b'):
                first_paragraph = p.text
                break
            return first_paragraph

            
      
    def to_json_file(self, filepath: str):
       
        with open(filepath, 'w', encoding= "utf-8") as json_file:
            json.dump(self.leaders_data, json_file, indent = 4, separators=(',', ': '), ensure_ascii=False)
            