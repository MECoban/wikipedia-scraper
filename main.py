"""from src.scraper import WikipediaScraper


def main() -> None:
    scraper = WikipediaScraper("https://country-leaders.onrender.com")
    scraper.refresh_cookie()
    print("Cookies created")
    
    countries = scraper.get_countries()
    print("Countries:", countries)
    for country_code in countries:
        scraper.get_leaders(country_code)
        print(f"Leaders  {country_code}:", scraper.leaders_data[country_code])

    scraper.to_json_file('leaders_data.json')
    print("Leaders data saved to leaders_data.json")

if __name__ == "__main__":
    main()"""

    # main.py

from scraper import WikipediaScraper

if __name__ == "__main__":
    scraper = WikipediaScraper()

    # Get the list of supported countries
    countries = scraper.get_countries()

    # Get leaders for each country and retrieve the first paragraph from Wikipedia for each leader
    for country in countries:
        scraper.get_leaders(country)
        for leader in scraper.leaders_data[country]:
            wikipedia_url = leader.get("wikipedia_url")
            if wikipedia_url:
                leader["first_paragraph"] = scraper.get_first_paragraph(wikipedia_url)
                leader["cleaned_paragraph"] = scraper.clean_paragraph(leader["first_paragraph"])

    # Save the data into a JSON file
    scraper.to_json_file("leaders_data.json")
