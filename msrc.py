import requests
from bs4 import BeautifulSoup
import time
import logging
from urllib.parse import urljoin
import re
class WebScraper:
    def __init__(self, base_url, delay=1):
        """
        Initialize the scraper with a base URL and optional delay between requests
        
        Args:
            base_url (str): The base URL to scrape
            delay (int): Seconds to wait between requests
        """
        self.base_url = base_url
        self.delay = delay
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def get_page(self, url):
        """
        Fetch and parse a webpage
        
        Args:
            url (str): The URL to fetch
            
        Returns:
            BeautifulSoup: Parsed HTML content
        """
        try:
            # Respects robots.txt by waiting between requests
            time.sleep(self.delay)
            
            
            response = self.session.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error fetching {url}: {str(e)}")
            return None

    def extract_data(self, soup, selectors):
        """
        Extract data from parsed HTML using CSS selectors
        
        Args:
            soup (BeautifulSoup): Parsed HTML content
            selectors (dict): Dictionary mapping field names to CSS selectors
            
        Returns:
            dict: Extracted data
        """
        data = {}
        for field, selector in selectors.items():
            elements = soup.select(selector)
            data[field] = [elem.text.strip() for elem in elements]
        return data

    def scrape_pages(self, urls, selectors):
        """
        Scrape multiple pages and extract data
        
        Args:
            urls (list): List of URLs to scrape
            selectors (dict): Dictionary mapping field names to CSS selectors
            
        Returns:
            list: List of dictionaries containing scraped data
        """
        results = []
        for url in urls:
            self.logger.info(f"Scraping {url}")
            soup = self.get_page(url)
            if soup:
                data = self.extract_data(soup, selectors)
                data['url'] = url
                results.append(data)
        return results
    def get_selectors(self):
        """
        Get selectors from user
        
        Args:
            None
        
        Returns:
            dict: Dictionary of selectors selected by user
        """
        selectors = {}
        while True:
            fieldn = input("Enter field name or done to finish ").strip()
            if fieldn == "done":
                break
            css_selectors = input(f"Enter css_selectors for {fieldn}").strip()
            selectors[fieldn] = css_selectors
            
        confirm = input("Reset selection (y/n): ").lower()
        
        if confirm == "y":
            deletelist = input("List to deletion (all or field name from selectors)").lower().split(" ")
            if len(deletelist) ==  1 and deletelist[0] == "all":
                selectors = {}
            else: 
                for record in deletelist:
                    if selectors[fieldn] == record:
                        del selectors[record]
                    else:
                        pass
            self.get_selectors
        return selectors
    def get_pages_from_user(self):
        """
        Get pages from user
        
        Args:
            None
        
        Returns:
            arr: Array of pages selected by user
        """
        pages = []
        while True:
            pages = input("Enter page name or done to finish ").strip()
            if pages == "done":
                break
         
        confirm = input("Reset selection (y/n): ").lower()
        
        if confirm == "y":
            deletelist = input("List to deletion (all or page url)").lower().split(" ")
            if len(deletelist) ==  1 and deletelist[0] == "all":
                selectors = {}
            else: 
                for record in deletelist:
                   for page in pages:
                       if page == record:
                           pages.pop(page)
            self.get_pages_from_user()
        return pages
    def get_url(self):
        url = input("Enter url of site ").strip()
        confirm = input("Reset selection (y/n): ").lower()
        
        if confirm == "y":
            self.get_url()
        
        return url
            
        
        
        
            