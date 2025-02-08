from celery import shared_task,group,chord
import json
import os
from tasks import ScrapeArticleLinks,ParseArticless

@shared_task
def scrape_article_urls(url:str,pagination:int):
    try:
        article_links=ScrapeArticleLinks(url).perform_scraping_and_launch_sub_jobs()
        job_group = group(parse_articles.s(link) for link in article_links)
        callback = save_parsed_articles.s(os.path.join('output',f'smashingMagazineArticles-{pagination}.json'))
        result = chord(job_group)(callback) 
        return result.id
    except:
        raise Exception("Failed to scrape article links")
    
@shared_task
def parse_articles(url:str):
    try:
        parsed_data=ParseArticless(url).parse()
        return parsed_data
    except:
        raise Exception("Failed to parse article data")
    

@shared_task
def save_parsed_articles(parsed_data, output_file):
    try:
        with open(output_file, "w") as f:
            json.dump(parsed_data, f, indent=4)

    except Exception as e:
        raise Exception(f"Failed to save articles: {e}")