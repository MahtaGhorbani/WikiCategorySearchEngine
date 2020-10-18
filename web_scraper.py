from urllib.request import urlopen

from bs4 import BeautifulSoup, Comment

from Page import Page
from OccurrenceList import OccurrenceList



def scrape(site, prefix="https://en.wikipedia.org"):
    page = BeautifulSoup(urlopen(site.url), 'html.parser')
    links_to = OccurrenceList()
    for link in page.find_all('a'):
        if link.get('href'):
            url_link = link.get('href')
            if not url_link.startswith("http"):
                url_link = prefix + url_link
            links_to = links_to.union(OccurrenceList([url_link]))

    """
    Remove script tags
    """
    for script in page("script"):
        page.script.extract()

    """
    Remove style tags
    """
    for style in page("style"):
        page.style.extract()

    """
    Remove comments
    """
    comments = page.findAll(text=lambda text: isinstance(text, Comment))
    for comment in comments:
        comment.extract()

    return Page(page.title.string, site.url, page.text, links_to)
