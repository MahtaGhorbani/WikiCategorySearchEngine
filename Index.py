class Index:
    def __init__(self, index, title, url, links_to):
        """
        Index stores the location of the node in the www
        """
        self.index = index
        self.title = title
        self.url = url
        self.links_to = links_to

    def __str__(self):
        return "{0}\n{1}".format(self.title[:min(len(self.title), 50)], self.url[:min(len(self.url), 50)])

    def __repr__(self):
        return "{0} ({1} : {2})".format(self.index, self.title[:min(len(self.title), 30)], len(self.links_to))

    def __lt__(self, other):
        return self.index < other.index

    def __le__(self, other):
        return self.index <= other.index

    def __eq__(self, other):
        return self.index == other.index

    def __ne__(self, other):
        return self.index != other.index

    def __gt__(self, other):
        return self.index > other.index

    def __ge__(self, other):
        return self.index >= other.index
    def __hash__(self):
        return hash(self.url)