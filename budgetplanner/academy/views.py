from django.shortcuts import render
import feedparser
import textwrap
from .models import ArticleAcademy
from django.core.paginator import Paginator
# RSS


def rss_news(urls):
    '''
    Deal with the fetching and processing of RSS data
    '''
    all_news = []

    for url in urls:
        # Parse URL
        feed = feedparser.parse(url)
        top = feed.entries[:10]
        for news in top:
            # Process and format the news item
            news_item = {
                'title': news.title,
                'summary': news.summary[:200],
                'link': news.link
            }
            all_news.append(news_item)

    return all_news

# Article's page


def academy_articles_view(request):
    sources = ArticleAcademy.objects.filter(status=2).order_by('-created_on')

    urls = [source.url for source in sources]

    news_items = rss_news(urls)

    # Pagination
    paginator = Paginator(news_items, 5)
    page_number = int(request.GET.get('page', 1))  # Convert to int
    page_obj = paginator.get_page(page_number)

    return render(request, 'academy_articles.html', {'page_obj': page_obj, 'news_items': news_items})
