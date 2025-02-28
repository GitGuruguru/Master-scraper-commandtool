# Master scraper

![Nova](pantera.png)

## Overview
WebScraper is a Python-based web scraping tool that allows users to extract structured data from web pages. It utilizes `requests` for HTTP requests and `BeautifulSoup` for HTML parsing, offering functionalities for retrieving pages, extracting data using CSS selectors, and handling multiple pages efficiently.

## Features
- Fetch and parse web pages with built-in delay for respectful scraping.
- Extract data using customizable CSS selectors.
- Handle multiple page scrapes efficiently.
- Interactive user input for URLs and CSS selectors.
- Logging support for error tracking and debugging.

## Requirements
This project requires Python 3 and the following dependencies:

```
pip install requests beautifulsoup4
```

## Installation
Clone the repository and install the required packages:
```sh
git clone "https://github.com/GitGuruguru/Master-scraper-commandtool.git"
cd WebScraper
pip install -r requirements.txt
```

## Usage
1. **Run the script**:
```sh
python msct.py
```
2. **Provide a base URL** when prompted.
3. **Specify pages to scrape**.
4. **Define CSS selectors** to extract required elements.
5. The scraper will fetch and display the extracted data.

## Example Code
```python
scraper = WebScraper("https://example.com")
pages = ["https://example.com/page1", "https://example.com/page2"]
selectors = {"title": "h1", "links": "a"}
data = scraper.scrape_pages(pages, selectors)
print(data)
```

## Notes
- The scraper respects `robots.txt` by adding delays between requests.


## License
This project is open-source under the MIT License.

## Author
Developed by GitGuruGuru

