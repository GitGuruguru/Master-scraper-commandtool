from msrc import *

def main():
    print("Write a url ex. amazon.com or https://amazon.com")
    url = WebScraper.get_url()
    scraper = WebScraper(url)
    selctors = WebScraper.get_selectors()
    pages = WebScraper.get_pages_from_user()
    
    results = scraper.scrape_pages(pages, selctors)