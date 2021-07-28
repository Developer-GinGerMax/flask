import matplotlib.pyplot as plt
import random

from modu.template import ChangedTemperaturesOnMyBirthday
from modu.template.basic_hist import highest_temperature


def sorted_ramdom_arr() -> []:
    arr = []
    [arr.append(random.randint(1,1000))for i in range(13)]
    return arr

def show_boxplot(arr:[]):
    plt.boxplot(arr)
    plt.show()

def show_boxplot_month(month: str):
    plt.boxplot(highest_temperature(month))
    plt.show()


def show_boxplot_all_month():
    birth = ChangedTemperaturesOnMyBirthday()
    birth.read_data()
    arr = birth.data

    month = [[], [], [], [], [], [], [], [], [], [], [], []]

    '''
    for i in birth.data:
        if i[-1] !='':
            month[int(i[0].split('-')[1])-1].append(float(i[-1]))
    '''

    [month[int(i[0].split('-')[1])-1].append(float(i[-1]))for i in birth.data if i[-1] !='']
    plt.boxplot(month)
    plt.show()


def show_boxplot_per_date(month:str):
    birth = ChangedTemperaturesOnMyBirthday()
    birth.read_data()
    # arr = birth.data

    day = []
    [day.append([])for i in range(31)]

    # for row in birth.data:
    #     if row[-1] !='':
    #         if row[0].split('-')[1] == '08':
    #             day[int(row[0]
    [day[int(row[0].split('-')[2])-1].append(float(row[-1]))
        for row in birth.data
        if row[-1] !=''
        if row[0].split('-')[1] == month]

    plt.style.use('ggplot')
    plt.figure(figsize=(10,5), dpi=300)
    plt.boxplot(day, showfliers=False)
    plt.show()

if __name__ == '__main__':
    #show_boxplot(sorted_ramdom_arr())
    #show_boxplot_month('08')
    #show_boxplot_all_month()
    show_boxplot_per_date('08')

    #이걸 객체지향으로 만들면 어케함?