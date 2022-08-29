import httpx
import bs4


class Links:
    
    def __init__(self, link):
        self.link = link

    def linkProgram(self):
        if "https://www.roblox.com/groups/" in self.link: return self.robloxGroup()
        elif "https://roblox.com/users/" in self.link: return self.robloxUser()
        elif "https://linktr.ee/" in self.link: return self.linktree()
        elif "https://twitter.com/" in self.link: return self.twitter()
        else: return None
        
    def robloxUser(self):
        userId = self.link.split("/")[4]
        userInfo = httpx.get(f"https://users.roblox.com/v1/users/{userId}").json()
        return userInfo
    
    def robloxGroup(self):
        groupId = self.link.split("/")[4]
        groupInfo = httpx.get(f"https://groups.roblox.com/v1/groups/{groupId}").json()
        return groupInfo
        
    def linktree(self):
        
        info = {"links": []}
        user = self.link.split("/")[3]
        r = httpx.get(f"https://linktr.ee/{user}")
        if r.status_code == 200:
            soup = bs4.BeautifulSoup(r.text, features="html5lib")
            for a in soup.find_all('a', href=True):
                if "https://" in a["href"]:
                    info["links"].append(a['href'])
        return info
    
    def twitter(self):
        user = self.link.split("/")[3]
        r = httpx.get(f"https://nitter.fdn.fr/{user}")
        if r.status_code == 200:
            soup = bs4.BeautifulSoup(r.text, features="lxml")
            bio = soup.find("div", {"class": "profile-bio"})
            
            if bio != None:
                bio = bio.text
                
            website = soup.find("div", {"class": "profile-website"})
            if website != None:
                website = website.find("a", href=True)['href']
                
            location = soup.find("div", {"class": "profile-location"})
            if location != None:
                location = location.text.replace("\n", "")
                
            return {"bio": bio, "website": website, "location": location}
           
        else:
            return None
