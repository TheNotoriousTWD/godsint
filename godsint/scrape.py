class Scrape:
    
    def __init__(self, info=None, link=None):
        self.info = info
        self.link = link
        
    def findLinks(self):
        links = []
        for key in self.info.keys():
            if type(self.info[key]) == str:
                for word in self.info[key].split(" "):
                    if "https://" in word: links.append(word)
                    
            elif type(self.info[key]) == list:
                for word in self.info[key]:
                    if "https://" in word: links.append(word)
                    
        return links
    
    def scrapeLink(self):
        linksScraped = []
        if type(self.link) == list:
            for i in self.link:
                linksScraped.append(self.getUrlInfo(i))
                
        elif type(self.link) == str:
            linksScraped.append(self.getUrlInfo(self.link))
            
                
        return linksScraped
    
    def getUrlInfo(self, url):
        splittedLink = url.split("/")
        domain = splittedLink[2]
        try:
            user,path = splittedLink[4],splittedLink[3]
            return {"domain": domain, "user": user, "url": f"https://{domain}/{path}"}
        except:
            user = splittedLink[3]
            return {"domain": domain, "user": user, "url": f"https://{domain}"}
