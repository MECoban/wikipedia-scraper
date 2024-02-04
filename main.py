from src.scraper import WikipediaScraper

def main():

    """
    The main function to execute the WikipediaScraper and store the data into a JSON file.
    """

    scraper = WikipediaScraper()

    scraper.refresh_cookie()

    countries = scraper.get_countries()

    print("Program is working... This will take 1 min...")

    for country in countries:
        try:  # I added try/exept here because there is an error about "be"
            scraper.get_leaders(country)
            for leader in scraper.leaders_data[country]:
                wikipedia_url = leader.get("wikipedia_url")
                if wikipedia_url:
                    leader["first_paragraph"] = scraper.get_first_paragraph(wikipedia_url)
                    leader["cleaned_paragraph"] = scraper.clean_paragraph(leader["first_paragraph"])
        except Exception as e:
            print(f"An error occurred for country {country}: {e}")

    scraper.to_json_file("leaders_data.json")            

if __name__ == "__main__":
    main()
