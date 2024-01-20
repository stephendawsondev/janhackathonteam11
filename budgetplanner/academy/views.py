from django.shortcuts import render
import feedparser
from bs4 import BeautifulSoup
import textwrap
from .models import ArticleAcademy
from django.core.paginator import Paginator
from datetime import datetime

# RSS


def rss_news(urls):
    '''
    Deal with the fetching and processing of RSS data
    '''
    all_news = []

    for url in urls:
        # Parse URL
        feed = feedparser.parse(url)
        top = feed.entries[:4]
        image = ''

        for news in top:
            if 'enclosures' in news:
                for enclosure in news.enclosures:
                    if 'image' in enclosure.type:
                        image = enclosure.url

            if 'description' in news:
                soup = BeautifulSoup(news.description, 'html.parser')
                images = soup.find_all('img')
                for img in images:
                    image = img['src']

            if 'media_content' in news:
                for media in news.media_content:
                    if 'image' in media.get('type', ''):
                        image = media["url"]

            if 'content' in news:
                soup = BeautifulSoup(news.content[0].value, 'html.parser')
                images = soup.find_all('img')
                for img in images:
                    image = img['src']

            if 'image' in news:
                image = news.image["href"]

            # Parse time
            date_str = news.published
            formatted_date = datetime.strptime(
                date_str, "%a, %d %b %Y %H:%M:%S %z")
            clean_date = formatted_date.strftime("%a, %d %b %Y %H:%M")

            # Process and format the news item
            news_item = {
                'title': news.title,
                'summary': f'{news.summary[:200]}...',
                'link': news.link,
                'base': news.title_detail.base,
                'image': image,
                'published': clean_date,
            }
            all_news.append(news_item)

    return all_news

# Article's page


def academy_articles_view(request):
    sources = ArticleAcademy.objects.filter(status=2).order_by('-created_on')

    urls = [source.url for source in sources]

    news_items = rss_news(urls)

    # Pagination
    paginator = Paginator(news_items, 12)
    page_number = int(request.GET.get('page', 1))
    page_obj = paginator.get_page(page_number)

    return render(request, 'academy_articles.html', {'page_obj': page_obj, 'news_items': news_items})
