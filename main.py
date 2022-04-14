import requests
from bs4 import BeautifulSoup
class vichu:
    def __init__(self,url):
        self.url=url
        self.user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
        self.response = requests.get(url=self.url,headers=self.user_agent).text
        self.soup = BeautifulSoup(self.response, "html.parser")

    def place(self):
        final=[]
        count = 0
        for tag in self.soup.find_all(class_="list"):
            if tag is not None:
                if tag.get('data-name') is not None:
                    count+=1
                    final.append(tag.get('data-name'))
        return final

    def movie_theatre_name(self):
        pass
movie_url = input("Movie url: ")
our_place = input("enter Place: ")
k=0
while(True):
    k+=1
    movie = vichu(url=movie_url)
    place_list = movie.place()
    for i in place_list:
        if i == our_place:
            print(i)
    print(k)
# print(movie.place())
# print(len(movie.place()))
