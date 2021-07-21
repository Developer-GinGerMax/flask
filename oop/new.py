'''
이름, 나이, 주소를 입력받아서 자기소개 하는 프로그램을 작성하시오.
출력은 안녕하세요, 제 이름은 Tom 이고, 나이는 28세이고, 서울에서 거주합니다. 로 됩니다.
이때, 여러 사람이면 전부 입력받아서 전체가 일괄 출력되는 시스템이어야 합니다.
'''

class Person(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def toString(self):
        print(f'안녕하세요, 제 이름은{self.name}이고, 나이는{self.age}세 이고, {self.address}에서 거주합니다.')

    @staticmethod
    def main():
        persons = []
        while 1:
            print('MENU 0-EXIT 1-ADD 2-PRINT')
            menu = input('choose num')
            if menu == '0':
                return
            elif menu == '1':
                persons.append(Person(input('이름은?'),input('나이는?'),input('사는곳은?')))
            elif menu =='2':
                for i in persons:
                    i.toString()
Person.main()