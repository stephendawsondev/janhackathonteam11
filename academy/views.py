from django.shortcuts import render
import feedparser
import textwrap
from .models import ArticleAcademy
from django.core.paginator import Paginator
from datetime import datetime
from urllib.parse import urlparse
import requests
import random

# RSS


def can_embed_url(url):
    try:
        response = requests.get(url, timeout=10)
        csp = response.headers.get('Content-Security-Policy', '')
        x_frame_options = response.headers.get('X-Frame-Options', '')

        # Check for 'frame-ancestors' in CSP
        if "frame-ancestors" in csp:
            if "'self'" in csp or "yourdomain.com" in csp:
                return False
            else:
                return True

        # Check for 'X-Frame-Options'
        elif x_frame_options:
            if x_frame_options.lower() in ['deny', 'sameorigin']:
                return False
            else:
                return True
        else:
            return True
    except requests.RequestException as e:
        print(f"Error checking URL {url}: {e}")
        return False


def rss_news(urls):
    '''
    Deal with the fetching and processing of RSS data
    '''
    all_news = []

    for url in urls:
        # Parse URL to get the domain name
        parsed_uri = urlparse(url)
        domain = '{uri.netloc}'.format(
            uri=parsed_uri).replace('www.', '').capitalize()

        # Remove '.com' and capitalize
        if domain.endswith('.com'):
            domain = domain[:-4].capitalize()
        else:
            domain = domain.capitalize()

        # Parse the RSS feed
        feed = feedparser.parse(url)
        top = feed.entries[:3]
        image = ''

        for news in top:
            # Find an image URL
            if 'enclosures' in news:
                for enclosure in news.enclosures:
                    if 'image' in enclosure.type:
                        image = enclosure.url
                        break

            if 'image' in news and not image:
                image = news.image["href"]

            # Parse and format the publication date
            date_str = news.published.replace(' GMT', ' +0000')
            formatted_date = datetime.strptime(
                date_str, "%a, %d %b %Y %H:%M:%S %z")
            clean_date = formatted_date.strftime("%a, %d %b %Y")

            # Check if the news link can be embedded
            url_proctect = news.link
            can_embed = can_embed_url(url_proctect)

            # Process and format the news item
            news_item = {
                'can_embed': can_embed,
                'title': news.title,
                'summary': f'{news.summary[:150]}...',
                'link': news.link,
                'base': news.title_detail.base,
                'image': image,
                'published': clean_date,
                'domain_name': domain,
            }
            all_news.append(news_item)
    return all_news


# Article's page


def academy_articles_view(request):
    sources = ArticleAcademy.objects.filter(status=2).order_by('-created_on')

    urls = [source.url for source in sources]

    news_items = rss_news(urls)

    # Pagination
    paginator = Paginator(news_items, 6)
    page_number = int(request.GET.get('page', 1))
    page_obj = paginator.get_page(page_number)

    return render(request, 'academy_articles.html', {'page_obj': page_obj})
