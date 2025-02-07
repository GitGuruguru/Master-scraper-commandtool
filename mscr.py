from msrc import WebScraper

def main():
    # Get base URL
    base_url = WebScraper.get_url()
    
    # Create scraper instance
    scraper = WebScraper(base_url)
    
    # Get selectors
    selectors = WebScraper.get_selectors()
    
    # Get pages to scrape
    pages = WebScraper.get_pages_from_user()
    
    # Perform scraping
    results = scraper.scrape_pages(pages, selectors)
    
    # Print results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()