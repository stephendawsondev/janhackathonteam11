from django.shortcuts import render
import feedparser
import textwrap
# RSS


def rss_news(self, url):
    '''
    Deal with the fetching and processing of RSS data
    '''
    # Parse URL
    feed = feedparser.parse(url)
    top = feed.entries[:3]
    x = 0

    for news in top:
        x += 1
        print(f'\n{BOLD}Coindesk RSS News {x}{RESET}\n')

        # Title
        title_lines = textwrap.wrap(news.title, width=70)
        full_title = '\n'.join(title_lines)
        print(f'{bullet_point} {full_title}:\n')

        # Summary
        text_lines = textwrap.wrap(news.summary[:200], width=70)
        # get rid of brackets and add space in between
        full_text = '\n'.join(text_lines)
        print(f'{BOLD}{full_text}...{RESET}\n')

        # Link
        print(f'{bullet_point}', news.link)

# Article's page

def academy_articles_view(request):

    return render(request, 'academy_articles.html',)
