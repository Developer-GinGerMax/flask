'''
아래의 요소를 포함한 주소록 만들기
name email phone address
'''


class Contacts(object):
    def __init__(self,name,email,phone,address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address


    def to_string(self):
        print(f'이름은{self.name} 이메일 주소는 {self.email} 전화번호는 {self.phone} 주소는 {self.address} 입니다.')


def set_contact():
    return Contacts(input('name') , input('email') , input('phone') , input('address'))


def get_contact(ls):
    for i in ls:
        print(f'이름은{i.name} 이메일 주소는 {i.email} 전화번호는 {i.phone} 주소는 {i.address} 입니다.')


def del_contact(ls, name):
    for i in enumerate(ls):
        ls.remove(i.name)


def menu_s(ls):
    t = ''
    for i, j in enumerate(ls):
        t += str(i)+'-'+j+'\t'
    return int(input(t))


def main():
    ls = []
    while 1:
        menu = menu_s(['EXIT', 'ADD', 'PRINT', 'DELETE'])
        if menu == 1:
            t = set_contact()
            ls.append(t)
        elif menu == 2:
            get_contact(ls)
        elif menu == 3:
            del_contact(ls, input('Del Name'))
        else:
            break


if __name__ == '__main__':
    #ls = ['EXIT' , 'ADD' , 'PRINT' , 'DELETE' , 'UPDATA' , 'DEBUG']
    #print(menu(ls))
    main()