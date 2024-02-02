import requests
from bs4 import BeautifulSoup
import re
#from scripts.scraper import WikipediaScraper as ws
import json



#from scripts.scraper import WikipediaScraper as ws


def main():
    # run the program from here
    scraper = WikipediaScraper()

    countries = scraper.list_countries()
    for country in countries:
        scraper.refresh_cookie()
        scraper.get_leaders(country)

    scraper.to_json_file("./leaders_data.json")
    # print(scraper.leaders_data)
    # for dict in scraper.leaders_data:
    # url = dict.get("wikipedia_url")
    # scraper.get_first_paragraph(url)


# print(scraper.leaders_data)
# scraper.to_json_file("./leaders_data.json")


if __name__ == "__main__":
    main()