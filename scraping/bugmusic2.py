from bs4 import BeautifulSoup
from urllib.request import urlopen

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
        n_artists = 0
        n_title = 0
        ls = soup.find_all(name='p', attrs={'class':'artist'})
        ls2 = soup.find_all(name='p', attrs={'class':'title'})

        for i in ls:
            n_artists += 1
            print(str(n_artists) + "Rank")
            print("Artist : " + i.find('a').text)

        for j in ls2:
            n_title += 1
            print(str(n_title) + "Rank")
            print("title : " + j.find('a').text)


def main():
    Bugmusic('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20210721&charthour=09').scrap()


if __name__ == '__main__':
    main()