from text_churner import get_keywords
from web_scraper import scrape
from Index import Index
from OccurrenceList import OccurrenceList
from PatriciaTrie import Trie
from Site import Site
import bs4 as bs
import urllib.request
import re
import numpy as np
import nltk


class WikiFinder:
    web = OccurrenceList()
    keywords = Trie

    def __init__(self, urls=None):
        
        url_list =[]
        html = urllib.request.urlopen('https://en.wikipedia.org/wiki/Category:Class-based_programming_languages')
        bsObj = bs.BeautifulSoup(html,features="lxml")
        for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
            if 'href' in link.attrs:
                url_list.append(link.attrs['href'])

        self.urls = list(map(lambda x: Site(x,False), url_list))
        self.populate_web()

    def populate_web(self):
        """
        Populates the web and the inverted index keyword
        dictionary with the urls provided
        """
        occurdic={}
        for url in self.urls:
            page = scrape(url)
            keywords = get_keywords(page.text)
            index = len(self.web)
            self.web.append(Index(index, page.title, page.url, page.links_to))

            for word in keywords:
                value = OccurrenceList()
                value.append(index)
                occurdic[word.lower()]=value
                self.keywords.add(word.lower(), value)
        self.rank_page(occurdic,len(self.web))
        


    def search(self, query):
        query = get_keywords(query)
        pages = OccurrenceList()
        first = True
        for word in query:
            node = self.keywords.search(word.lower())
            if node and node.value:
                this_page_results = OccurrenceList()
                for page_index in node.value:
                    this_page_results = this_page_results.union(OccurrenceList([self.web[page_index]]))

                if first:
                    pages = this_page_results
                    first = False
                else:
                    pages = pages.intersect(this_page_results)

        return self.final_rank(pages,query)

    def rank_page(self, occurdic,n):
        
        a = [[0 for i in range(n)] for j in range(n)]
        for key,values in occurdic.items():
            for i in range(len(values)):
                for j in range(len(values)):
                    a[values[i]][values[j]] += 1
        for i in range(len(a)):
            for j in range(len(a)):
                x = a[i][j]
                if x != 0:
                    a[i][j] = 1/x
        a = np.matrix(a)
        b = (1/n) * np.matrix([[1 for i in range(n)] for j in range(n)])
        m = 0.85 * a + 0.15 * b
        v = (1/n) * np.matrix([[1] for i in range(n)])
        def page_rank(v):
            if sum(abs(m*v-v)) > 0.001:
                return page_rank(m*v)
            return m*v
        result = page_rank(v)
        result = [cell.item(0,0) for cell in result]
        self.PR = result
    
    
    def similarity_score(self,query , url):
        page = scrape(Site(url,True))
        keywords = get_keywords(page.text)
        score =0 
        for word in query :
            if word in keywords:
                score +=1
        return(score)
        
    def final_rank(self,pages,query):
        scores = list()
        for page in pages:
            s_score = self.similarity_score(query , page.url)
            pr_score = self.PR[page.index]
            f_score = (0.7)*s_score +(0.3)*pr_score
            scores.append((page,f_score))
        sorted_x = sorted(scores, key=lambda kv: kv[1],reverse = True)  
        
        return sorted_x[:5]

    