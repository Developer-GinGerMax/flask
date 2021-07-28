import matplotlib.pyplot as plt
import random
from modu.template import ChangedTemperaturesOnMyBirthday


# def random_dice():
#     dice = []
#     [dice.append(random.randint(1,6)) for i in range(5)]
#     print(dice)
#
# def show_hist():
#     plt.hist(dice, bins=6)
#     plt.show()

def highest_temperature(month: str) -> []:
    birth = ChangedTemperaturesOnMyBirthday()
    # [print(i) for i in birth.data]

    # 줄이기 전 원본
    # for i in birth.data:
    #     month = i[0].split('-')[1]
    #     if i[-1] != '':
    #         if month == '08':
    #             aug.append(float(i[-1]))
    # 줄이기 후
    # aug = [(float(i[-1])) for i in birth.data if i[-1] != '' if i[0].split('-')[1] == '08']

    birth.read_data()
    # 줄이기 전 원본
    # jan = []
    # for i in birth.data:
    #     month = i[0].split('-')[1]
    #     if i[-1] != '':
    #         if month == '01':
    #             jan.append(float(i[-1]))
    # 줄이기 후
    arr = []
    [arr.append(float(i[-1])) for i in birth.data if i[-1] != '' if i[0].split('-')[1] == month]
    return arr

    # plt.hist(aug, bins=100, color='r', label='Aug')


def show_hist_about(arr: [], month: str):
    plt.hist(arr, bins=100, color='b', label=f'{month} Month')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # dice = random_dice(1000000)
    # # random_dice()
    # show_hist(dice)
    show_hist_about(highest_temperature('01'), month='01')