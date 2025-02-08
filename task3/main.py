from jobs import scrape_article_urls
from utils.celery_init import celery_init_app
import sys
celery=celery_init_app()

if __name__ == "__main__":
    '''
    Change the range to scrape more pages i=pagination number
    id is task id to get job results
    '''
    i=sys.argv[1]
    print(f"Scraping {i} pages")
    for i in range(1,int(i)+1):
        if i==1:
            id=scrape_article_urls.apply_async(args=[f"https://www.smashingmagazine.com/articles",i])
        id=scrape_article_urls.apply_async(args=[f"https://www.smashingmagazine.com/articles/page/{i}",i])
