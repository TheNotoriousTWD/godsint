import httpx
import bs4
from .links import Links
from .scrape import Scrape

class Osint:
    def __init__(self, twitter=None, linktree=None, caard=None, robloxId=None, discordId=None, discordTag=None):
        
        self.users = {
            "twitter": {"url": "https://twitter.com/()", "user": twitter, "scraped": False},
            "linktree": {"url": "https://linktr.ee/()", "user": linktree, "scraped": False},
            "caard": {"url": "https://().carrd.co/", "user": caard, "scraped": False},
            "robloxId": {"url": "https://roblox.com/users/()", "user": robloxId, "scraped": False},
            "discordId": {"url": "unknown", "user": discordId, "scraped": False},
            "discordTag": {"url": "unknown", "user": discordTag, "scraped": False},
        }
        
    def osint(self):
        for i in range(10):
            for social in self.users.keys():
                mediaDict = self.users[social]
                if mediaDict["user"] != None and mediaDict["scraped"] == False:
                    self.linksProgram(mediaDict)
                    
        return self.users
                    
                
    def linksProgram(self, socialMedia):
        url = socialMedia["url"].replace("()", socialMedia["user"])
        
        #scrape and return the url
        info = Links(url).linkProgram()
        socialMedia["scraped"] = True
        
        
        links = Scrape(info=info).findLinks()

        for i in links:
            for key in self.users.keys():
                if self.users[key]["url"].replace("()", "") in i.replace("www.", "") and self.users[key]["user"] == None:
                    user = i.replace("www.", "").replace(self.users[key]["url"].replace("()", ""), "")
                    self.users[key]["user"] = user.split("/")[0]
