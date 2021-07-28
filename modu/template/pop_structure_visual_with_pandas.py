import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
from matplotlib import font_manager, rc
rc('font', family = font_manager.FontProperties(fname='C:/Windows/Fonts/H2GTRE.ttf').get_name())
class Population(object):

    data: [] = list()
    home: [] = list()
    away: object = None
    result_name: str = ''

    def read_data(self):
        df = pd.read_csv('./data/202106_202106_연령별인구현황_월간.csv', encoding='UTF-8', thousands = ',', index_col = 0)
        df.to_csv('./data/202106_202106_연령별인구현황_월간_without_comma.csv', sep=',', na_rep='NaN')
        data = csv.reader(open('./data/202106_202106_연령별인구현황_월간_without_comma.csv', 'rt', encoding='UTF-8'))
        next(data)
        self.data = list(data)

    def pop_per_dong(self, dong: str) -> []:
        # [주의 ]csv reader 는 1회 이상 사용하면 GC 가 제거한다
        # print([i for i in self.data])
        arr = []
        [arr.append(int(j)) for i in self.data if dong in i[0] for j in i[3:]]
        print('*'*100)
        print([i for i in arr])
        return arr

    def show_plot(self, arr: []):
        plt.style.use('ggplot')
        plt.plot(arr)
        plt.show()

    def find_home(self, name: str) -> []:
        home = []
        [home.append(int(j)) for i in self.data if name in i[0] for j in i[3:]]
        self.home = home

    def array_to_list(self, arr: object) -> []:
        return arr.to_list()

    def list_to_array(self, ls : []) -> object:
        return np.array(ls)

    def show_plot_home(self, arr: object, name: str):
        plt.title(f'{name} 지역의 인구 구조')
        plt.plot(arr)
        plt.show()

    def find_similar_area(self, name: str):
        mn = 1
        result = 0
        home = []
        for i in self.data:
            if name in i[0]:
                home = np.array(i[3:], dtype=int)/int(i[2])

        self.home = home

        for i in self.data:
            away = np.array(i[3:], dtype=int) / int(i[2])
            s = np.sum((home - away) ** 2)
            if s < mn and name not in i[0]:
                mn = s
                self.result_name = i[0]
                result = away
        self.away = result

    def show_plot_similar_two_cities(self, name: str, home: [], away: []):
        plt.style.use('ggplot')
        plt.figure(figsize=(10, 5), dpi=300)
        plt.title(f'{name} 지역과 가장 비슷한 인구 구조를 가진 지역')
        plt.plot(home, label=name)
        plt.plot(away, label=self.result_name)
        plt.legend()
        plt.show()


if __name__ == '__main__':
    pop = Population()
    pop.read_data()
    # name = input('인구구조가 알고 싶은 지역의 이름(읍면동 단위)를 입력해 주세요')
    pop.find_home('필동')
    pop.home = pop.list_to_array(pop.home)
    pop.find_similar_area('필동')
    pop.show_plot_similar_two_cities('필동', pop.home, pop.away)