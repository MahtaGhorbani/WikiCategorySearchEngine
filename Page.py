class Page:
    def __init__(self, title, url, text, links_to):

        self.title = title
        self.url = url
        self.text = text
        self.links_to = links_to

    def __str__(self):
        return "{0}: {1}".format(self.title[min(len(self.title), 20):],
                                 self.url[min(len(self.url), 20):])
