# Wikipedia Scraper


888       888 d8b 888      d8b                        888 d8b                 .d8888b.                                                      
888   o   888 Y8P 888      Y8P                        888 Y8P                d88P  Y88b                                                     
888  d8b  888     888                                 888                    Y88b.                                                          
888 d888b 888 888 888  888 888 88888b.   .d88b.   .d88888 888  8888b.         "Y888b.    .d8888b 888d888  8888b.  88888b.   .d88b.  888d888 
888d88888b888 888 888 .88P 888 888 "88b d8P  Y8b d88" 888 888     "88b           "Y88b. d88P"    888P"       "88b 888 "88b d8P  Y8b 888P"   
88888P Y88888 888 888888K  888 888  888 88888888 888  888 888 .d888888             "888 888      888     .d888888 888  888 88888888 888     
8888P   Y8888 888 888 "88b 888 888 d88P Y8b.     Y88b 888 888 888  888       Y88b  d88P Y88b.    888     888  888 888 d88P Y8b.     888     
888P     Y888 888 888  888 888 88888P"   "Y8888   "Y88888 888 "Y888888        "Y8888P"   "Y8888P 888     "Y888888 88888P"   "Y8888  888     
                               888                                                                                888                       
                               888                                                                                888                       
                               888                                                                                888                       


## Overview

The Wikipedia Scraper interacts with a custom API to get information (eader_id" "wikipedia_url", "first_name", "last_name", "birth_date", "place_of_birth", "start_mandate", "end_mandate") about country leaders, and retrieves the first paragraphs from their Wikipedia pages.

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