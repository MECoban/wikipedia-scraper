# Wikipedia Scraper

## Overview

The Wikipedia Scraper pragram interacts with a custom API to get information about country leaders. Extracts the first paragraph from the Wikipedia page of each leader. and cleans up unwanted patterns from the paragraphs using regular expressions. Saves the collected data into a JSON file as:

 - leader_id 
 - wikipedia_url
 - first_name
 - last_name
 - birth_date
 - place_of_birth
 - start_mandate
 - end_mandate
- first_paragraphs
- cleaned_paragraph

Wikipedia Scraper program saves "first_paragraphs" and "cleaned_paragraph". You will be able to see original and cleaned version of Wikipedia paragraph.


### Supported Countries: 

Morocco (Ma), Belgium (Be), Frace (Fr), U.S.A (U.S), Russia (Ru)


## Features

* Retrieve a list of supported countries from the API.
* Get information about leaders for each country.
* Extract the first paragraph from the Wikipedia page of each leader.
* Clean up unwanted patterns from the paragraphs using regular expressions.
* Save the collected data into a JSON file.

## Installation

To install Wikipedia Scraper, follow these steps:

Clone the repository to your machine. 

```
git clone https://github.com/MECoban/wikipedia-scraper.git
```

```
cd LeaderScraper
```
### Install dependencies

Before running the Wikipedia Scraper install the requirements file. For the requirements:

 ``` 
 pip install -r requirements.yml
```
## Features
LeaderScraper provides the following features:


### How to Use
Run the main.py script using the command:
```
python main.py
```
The script will fetch information about supported countries, leaders, and scrape Wikipedia pages.

The extracted data will be saved to a JSON file named "leaders_data.json".


## Contributing
If you'd like to contribute to this project, feel free to open an issue or submit a pull request. 

Contributions are welcome!
