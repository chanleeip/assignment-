from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from tasks.constants import (
    HEADERS,
    OutputFormatData
)

class ParseArticless():
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
            main_content = soup.find("main", id="main").find("article")
            author_name=main_content.find("li",class_="article-header--meta-item article-header--meta-item__author").text
            author_link=main_content.find("li",class_="article-header--meta-item article-header--meta-item__author").find('a')["href"]
            date=main_content.find("li",class_="article-header--meta-item article-header--meta-item__date").find("time")["datetime"]
            title=main_content.find('h1',id='main-heading').text
            tags=main_content.find('li',class_='meta-box--item meta-box--tags').find_all('a')
            summary=main_content.find('section',attrs={'aria-label':'Quick summary'}).text
            content_elements = main_content.find("div", class_="c-garfield-summary").find_next_siblings()
            stop_element = main_content.find(id="further-reading-on-smashingmag")
            content=[]
            for element in content_elements:
                if element == stop_element:
                    break
                content.append(element.get_text(strip=True))
            
            data=OutputFormatData(
                url=self.url,
                title=title,
                author_name=author_name,
                author_page_link=f'https://{self.domain}{author_link}',
                date=date,
                categories=[i.text for i in tags],
                summary=summary,
                content=' '.join(content)
            )
            return data.to_dict()

        except Exception as e:
            raise Exception(str(e))
    
    def parse(self):
        html=self.scrape_articles()
        parsed_data=self.parse_articles_from_html(html)
        return parsed_data
        

    
