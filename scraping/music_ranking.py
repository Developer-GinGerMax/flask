from bs4 import BeautifulSoup
import pandas as pd
import requests

from common.menu import print_menu


class MusicRanking(object):
    domain = ''
    query_string = ''
    html = ''
    headers = {'User-Agent': 'Mozilla/5.0'}
    tag_name = ''
    fname = ''
    class_name = []
    artists = []
    titles = []
    dict = {}
    df = None

    def set_html(self):
        self.html = requests.get(f'{self.domain}{self.query_string}', headers=self.headers).text
        print(f'Crawling HTML is {self.html}')
    def get_raking(self):
        soup = BeautifulSoup(self.html, 'lxml')

    def insert_dict(self):
        # 방법 1
        for i in range(0, len(self.tag_name)):
            self.dict[self.titles[i]] = self.artists[i]
        # 방법 2
        for i, j in zip(self.titles, self.artists):
            self.dict[i] = j
        # 방법 3
        for i, j in enumerate(self.titles):
            self.dict[j] = self.artists[i]

        print(dict)

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = f'./data/{self.fname}.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')



def main():
    # 20210720
    # 16
    mr = MusicRanking()
    while 1:
        menu = print_menu(['exit', 'Bugs URL', 'Melon URL', 'Output',
                           'Print Dict', 'Dict To Dataframe', 'Dataframe to CSV' ])
        # 0- exit, 1- Bugs (URL), 2- Melon (URL) 3- output, 4-print dict,
        # 5-dict to dataframe, 6-df to csv
        if menu == 0:
            break
        elif menu == 1:
            mr.domain = 'https://music.bugs.co.kr/chart/track/realtime/total?'
            mr.query_string = 'chartdate=20210721&charthour=09'
            mr.set_html()
        elif menu == 2:
            mr.tag_name = 'p'
            mr.class_name.append('artist')
            mr.class_name.append('title')
            mr.get_raking()
        elif menu == 3:
            pass
        elif menu == 4:
            pass
        elif menu == 5:
            pass



if __name__ == '__main__':
    main()

