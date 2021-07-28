class Integer(object):
    def integer_checker(self, t):
        assert type(t) is int, 'not int'


if __name__ == '__main__':
    instance = Integer()
    while 1:
        menu = input('\n0-Exit \n1-Integer Checker\n')
        if menu == '0':
            break
        elif menu == '1':
            ls = [1, 3, 6, 3, 8, 7, 13, 23, 13, 2, 3.14, 2, 3, 7]
            for i in ls:
                instance.integer_checker(i)







