class Site:

    
    def __init__(self,url , complete, html_doc=None):
        if complete ==True :
            self.url = url
        else:
            self.url = "https://en.wikipedia.org"+url
            self.html_doc = html_doc

    def __str__(self):
        return self.url[:min(len(self.url), 30)]

    def __repr__(self):
        return self.url[:min(len(self.url), 30)]
