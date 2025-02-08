from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from tasks.constants import (
    HEADERS
)

class ScrapeArticleLinks():
    def __init__(self,url:str):
        self.url=url
        parsed_url = urlparse(url)
        self.domain = parsed_url.netloc 

    def scrape_articles(self):
        try:
            response = requests.get(self.url,headers=HEADERS)
            if response.status_code != 200:
                raise Exception("Failed to fetch data")
            return response.text
        except Exception as e:
            raise 

    def parse_articles_from_html(self,html:str):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            articles = soup.find_all('article')
            headers=[i.find("h2") for i in articles]
            links=[f'https://{self.domain}{i.find("a")["href"]}' for i in headers]
            return links
        except Exception as e:
            raise Exception(str(e))
    
    def perform_scraping_and_launch_sub_jobs(self):
        html=self.scrape_articles()
        links = self.parse_articles_from_html(html)
        return links
        

    
