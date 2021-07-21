from bs4 import BeautifulSoup
import pandas as pd
import requests

class MusicRangking(object):
    domain = ''
    query_string = ''
    html = ''
    cname = ''
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    artists = []
    titles = []
    dict = {}
    fname = ''
    df = None

    def set_html(self):
        self.html = requests.get(f'{self.domain}{self.query_string}', headers=self.headers).text
        print(f'Crawling HTML is {self.html}')

    def get_ranking(self):
        soup = BeautifulSoup(self.html, 'lxml')
        _ = 0
        artist = soup.find_all(name=self.cname, attrs={'class':self.class_name[0]})
        title = soup.find_all(name=self.cname, attrs={'class':self.class_name[1]})
        for i, j in zip(artist, title):
            _ += 1
            print(f"Rank {str(_)} Artist : {i.find('a').text}, Title : {j.find('a').text}")
        self.class_name.clear()

    def insert_dict(self):
        '''
        # 방법 1
        for i in range(0, len(self.tag_name)):
            self.dict[self.titles[i]] = self.artists[i]
        '''
        soup = BeautifulSoup(self.html, 'lxml')
        artist = soup.find_all(name=self.cname, attrs={'class': self.class_name[0]})
        title = soup.find_all(name=self.cname, attrs={'class': self.class_name[1]})
        for i, j in zip(artist, title):
            self.artists.append(f"{i.find('a').text}")
            self.titles.append(f"{j.find('a').text}")
        self.class_name.clear()
        print(self.titles)
        # 방법 2
        for i, j in zip(self.titles, self.artists):
            self.dict[i] = j
        # 방법 3

        # for i, j in enumerate(self.titles):
        #     self.dict[j] = self.artists[i]
        print(dict)

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        print(self.df)

    def df_to_csv(self):
        self.fname = input('file name : {}')
        path = f'./data/{self.fname}.csv'
        self.df.to_csv(path, sep='-', na_rep='NaN')

def print_menu(ls):
    # return '\t'.join(ls)
    t = ''
    for i, j in enumerate(ls):
        t += str(i)+'-'+j+'\t'
    return int(input(t))

def main():
    # 20210720
    # 16
    mr = MusicRangking()
    while 1:
        menu = print_menu(['EXIT', 'BUGS URL', 'MELON URL', 'OUTPUT',
                           'PRINT DICT', 'DICT TO DATAFRAME', 'DF TO CSV'])
        if menu == 0:
            break
        elif menu == 1:
            mr.domain = 'https://music.bugs.co.kr/chart/track/realtime/total?'
            mr.query_string = 'chartdate=20210721&charthour=09'
            mr.set_html()
            mr.class_name.append('artist')
            mr.class_name.append('title')
            mr.cname = 'p'
        elif menu == 2:
            mr.domain = 'https://www.melon.com/chart/index.htm?dayTime='
            mr.query_string = '2021072016'
            mr.set_html()
            mr.class_name.append('ellipsis rank02')
            mr.class_name.append('ellipsis rank01')
            mr.cname = 'div'
        elif menu == 3:
            mr.get_ranking()
        elif menu == 4:
            mr.insert_dict()
            pass
        elif menu == 5:
            mr.dict_to_dataframe()
        elif menu == 6:
            mr.df_to_csv()
        else:
            return

if __name__ == '__main__':
    main()