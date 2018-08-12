from bs4 import BeautifulSoup, NavigableString, Tag

import requests

def _get_single_news_item(item):
    contents = []
    for child in item.children:
        contents.append(str(child))
    return ''.join(contents).replace('href="', 'href="https://en.wikipedia.org')

def fetch_events_on_day():
    html_doc = requests.get('https://en.wikipedia.org').text

    soup = BeautifulSoup(html_doc, 'html.parser')

    otd_container = soup.find_all(id='mp-otd')[0].find('ul')

    event_list = []

    for child in otd_container.contents:
        if isinstance(child, NavigableString):
            continue
        if isinstance(child, Tag):
            event_list.append(_get_single_news_item(child))
    return event_list

