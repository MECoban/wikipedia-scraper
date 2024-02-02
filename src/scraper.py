import requests
import json
from bs4 import BeautifulSoup
import re

class WikipediaScraper:

    def __init__(self,root_url):
        self.root_url = root_url
        self.cookies_endpoint = "/cookie"
        self.country_endpoint = "/countries"
        self.leaders_endpoint = "/leaders"
    
    def check_url_status(self):
        self.status_url = "status" 
        self.response = requests.get(f"{self.root_url}/{self.status_url}")
        self.request_status = self.response.status_code

        if self.request_status == 200:
            print("Cookie created")
            print(self.response.text)
        else:
            print(f" {self.request_status}")
    
    def refresh_cookie(self):
        self.cookie_response = requests.get(f"{self.root_url}{self.cookies_endpoint}")
        self.cookies = self.cookie_response.cookies
        return self.cookies

    def get_countries(self):
        self.countries_url = self.root_url + self.country_endpoint
        self.cookies = self.refresh_cookie()
        self.countries_response = requests.get(self.countries_url, cookies=self.cookies)
        return(self.countries_response.json())
    
    def get_leaders(self):
        #self.cookies = self.refresh_cookie()
        leader_details = []
        country_list = self.get_countries()
        for countries in country_list:
            params={'country' : countries }
            leader_response = requests.get(f"{self.root_url}{self.leaders_endpoint}", cookies=self.refresh_cookie(),params=params)
            leader_details.append(leader_response.text)
        return(leader_details)
    
    def get_first_paragraph(self):
        leader_details = self.get_leaders()
        for leaders in leader_details:
            leader_dict = json.loads(leaders)
            for leader in leader_dict:
                wiki_url = leader["wikipedia_url"] 
                #leader_birth_year= leader["birth_date"].split('-')[0]
                wiki_content = requests.get(wiki_url).content
                soup = BeautifulSoup(wiki_content, "html.parser")
                first_paragraph = ''
                for tag in soup.find_all("p"):
                    if re.search('^<p><b>',tag):
                        first_paragraph = tag.get_text()
                
                print(first_paragraph)
            
        
        


