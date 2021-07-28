def one_to_ten_sum_1():
    sum = 0
    for i in range(1, 11):
        sum += i
    print(sum)


def one_to_ten_sum_2():
    print(sum(i for i in range(1,11)))


def one_to_ten_sum_3():
    print(sum(range(1, 11)))


if __name__ == '__main__':
    one_to_ten_sum_2()