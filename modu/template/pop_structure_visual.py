import csv
import matplotlib.pyplot as plt
import numpy as np

class Population():

    data: [] = list()


    def read_data(self):
        data = csv.reader(open('./data/202106_202106_연령별인구현황_월간.csv', 'rt', encoding='UTF-8'))
        next(data)
        # print([i for i in data])
        self.data = data

    def pop_per_dong(self, dong: str) -> []:
        arr = []
        [arr.append(int(j)) for i in self.data if dong in i[0] for j in i[3:]]
        return arr

    def show_plot(self, arr: []):
        plt.style.use('ggplot')
        plt.plot(arr)
        plt.show()

    def np_pop(self):
        data = csv.reader(open('./data/202106_202106_연령별인구현황_월간2.csv', 'rt', encoding='UTF-8'))
        home = []
        next(data)
        name = input('인구수가 알고 싶은 지역의 이름을 입력 : ')
        for row in data:
            if name in row[0]:
                home = np.array(row[3:], dtype=int)
        print(home)

        plt.rc('font', family='Malgun Gothic')
        plt.title(name+ '지역의 인구 구조')
        plt.plot(home)
        plt.show()



if __name__ == '__main__':
    pop = Population()
    #pop.read_data()
    #pop.show_plot(pop.pop_per_dong('대치1동'))
    pop.np_pop()
