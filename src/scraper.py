import requests
from bs4 import BeautifulSoup
import json
import re

class WikipediaScraper:

    """
     A class to scrape political leaders' data from a web API and retrieve information from Wikipedia.
     
     
     Attributes:
     -------------------------------------------

     - base_url (str): The base URL of the API.
     - country_endpoint (str): The endpoint to get the list of supported countries.
     - leaders_endpoint (str): The endpoint to get the list of leaders for a specific country.
     - cookies_endpoint (str): The endpoint to get a valid cookie to query the API.
     - leaders_data (dict): A dictionary to store the data retrieved from the API.
     - cookie (object): The cookie object used for API calls.
    """

    def __init__(self):
        self.base_url = "https://country-leaders.onrender.com"
        self.country_endpoint = "/countries"
        self.leaders_endpoint = "/leaders"
        self.cookies_endpoint = "/cookie"
        self.leaders_data = {}
        self.cookie = self.refresh_cookie() 

    def refresh_cookie(self):

        """
        Refreshes the API cookie.

        Returns:
        - object: The updated cookie.
        """
         
        response = requests.get(self.base_url + self.cookies_endpoint)
        if response.status_code == 200:
            return response.cookies
        elif response.status_code == 403:
            print(f"Error code: {response.status_code}, Cookie is missing. Refreshing the cookie ")
            return response.cookies
        else:
            raise ValueError(f"Error code: {response.status_code}, Unexpected status code ")

    def get_countries(self):

        """
        Gets the list of supported countries from the API.

        Returns:
        - list: A list of supported countries.
        """

        response = requests.get(self.base_url + self.country_endpoint, cookies = self.refresh_cookie())
        countries = response.json()

        if response.status_code == 200:
            return countries
        elif response.status_code == 403:
            print(f"Error code: {response.status_code}, Cookie is missing ")
            self.cookie = self.refresh_cookie()
            return self.cookie
        else:
            raise ValueError(f"Error code: {response.status_code}, Unexpected status code ")

    def get_leaders(self, country: str):

        """
        Retrieves the list of leaders for a specific country from the API.

        Args:
        - country (str): The country code.

        Returns:
        - list: A list of leaders for the specified country.
        """

        param = {'country': country}
        response = requests.get(self.base_url + self.leaders_endpoint, cookies = self.refresh_cookie(), params=param)
        leaders = response.json()

        if response.status_code == 200:
            self.leaders_data[country] = leaders

        elif response.status_code == 403:
            print(f"Error code: {response.status_code}, Cookie is missing ")
            self.cookie = self.refresh_cookie()
            return self.cookie
        else:
            raise ValueError(f"Error code: {response.status_code}, Unexpected status code ")
    

    def clean_paragraph(self, first_paragraph):

        """
        Cleans the first paragraph by removing unwanted patterns.

        Args:
        - first_paragraph (str): The raw first paragraph.

        Returns:
        - str: The cleaned first paragraph.
        """

        patterns = [(r'\[.*?\]|\(.*?\)|<.*?>'), r"(\[|\/).+(\/|\])(.*;)?", r"\(?\w+ⓘ ?\)?"]

        cleaned_paragraph = first_paragraph

        for pattern in patterns: # created for loop for more than 1 pattern
            cleaned_paragraph = re.sub(pattern, '', cleaned_paragraph)
        return cleaned_paragraph   


    def get_first_paragraph(self, wikipedia_url: str):

        """
        Retrieves the first paragraph of a Wikipedia page.

        Args:
        - wikipedia_url (str): The URL of the Wikipedia page.

        Returns:
        - str: The first paragraph.
        """

        first_paragraph = ""
        response = requests.get(wikipedia_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = soup.find_all("p") #finds paragraphs
            for paragraph in paragraphs:
                if paragraph.find('b'):# find paragraf with bold. <b>leader_name</b> this is how first_paragrapgh starts in wikipedia.
                    first_paragraph = paragraph.text
                    break
            return first_paragraph
        else:
            print(f"Error code: {response.status_code} Cookie is missing ")
            self.cookie = self.refresh_cookie()

    def to_json_file(self, filepath: str):

        """
        Stores the data structure into a JSON file.

        Args:
        - filepath (str): The path to the JSON file.
        """

        with open(filepath, 'w', encoding="utf-8") as json_file:
            json.dump(self.leaders_data, json_file, indent = 4, separators=(',', ': '), ensure_ascii=False)      
