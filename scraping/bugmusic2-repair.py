import urllib.request

from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.parse

"""
지원하는 Parser 종류
"html.parser" : 빠르지만 유연하지 않기 때문에 단순한 HTML문서에 사용합니다.
"lxml" : 매우 빠르고 유연합니다.
"xml" : XML 파일에만 사용합니다.
"html5lib" : 복잡한 구조의 HTML에 대해서 사용합니다.
"""

class Bugmusic(object):
    def __init__(self, url):
        self.url = url


    def to_string(self):
        print(f'\n {self.artists} , {self.titles}')


    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        _ = 0
        artists = soup.find_all(name='p', attrs={'class': 'artist'})
        titles = soup.find_all(name='p', attrs={'class': 'title'})
        for i, j in zip(artists, titles):
            _ += 1
            print(f"Rank {str(_)} Artist : {i.find('a').text}, Title : {j.find('a').text}")


class Melon(object):
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def scrap(self):
        req = urllib.request.Request(self.url, headers= self.headers)
        soup = BeautifulSoup(urllib.request.urlopen(req).read(), 'lxml')
        _ = 0
        artists = soup.find_all(name='div', attrs={'class': 'ellipsis rank02'})
        titles = soup.find_all(name='div', attrs={'class': 'ellipsis rank01'})
        for i, j in zip(artists, titles):
            _ += 1
            print(f"Rank {str(_)} Artist : {i.find('a').text},  Title : {j.find('a').text}")


def main():
    Bugmusic('https://music.bugs.co.kr/chart/track/realtime/total?chartdate={20210721}&charthour={09}').scrap()


if __name__ == '__main__':
    Melon('https://www.melon.com/chart/index.htm?dayTime=2021072016').scrap()