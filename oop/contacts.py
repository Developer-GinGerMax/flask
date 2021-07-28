"""
name, phone, email, address
"""


class Contacts(object):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_string(self):
        print(f'{self.name}, {self.phone}, {self.email}, {self.address}')


def set_contact() -> object:
    return Contacts(input('name'),input('phone'),input('email'),input('address'))


def get_contacts(ls):
    for i in ls:
        i.to_string()


def del_contact(ls, name):
    for i, j in enumerate(ls):
        if name == j.name:
            del ls[i]


def print_menu(ls) -> int:
    # return '\t'.join(ls)
    t = ''
    for i, j in enumerate(ls):
        t += str(i)+'-'+j+'\t'
    return int(input(t))

def main():
    ls = []
    while 1:
        menu = print_menu(['exit', 'add', 'print', 'delete'])
        if menu == 1:
            t = set_contact()
            ls.append(t)
        elif menu == 2:
            get_contacts(ls)
        elif menu == 3:
            del_contact(ls, input('Del Name'))
        else:
            break


if __name__ == '__main__':
    # ls = ['0-exit', '1-add', '2-print', '3-delete']
    # ls2 = ['exit', 'add', 'print', 'delete']
    # print(menu(ls2))
    main()