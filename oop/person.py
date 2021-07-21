'''
이름, 나이, 주소를 입력받아서 자기소개 하는 프로그램을 작성하시오.
출력은 안녕하세요, 제 이름은 Tom 이고, 나이는 28세이고, 서울에서 거주합니다. 로 됩니다.
이때, 여러 사람이면 전부 입력받아서 전체가 일괄 출력되는 시스템이어야 합니다.
'''

class WhoAmI(object):
    def __init__(self, name):
        self.name = name;
        self.persons = []

    def addPerson(self, person):
        self.persons.append(person)

    def whoami(self, whoami):
        print(f'안녕하세요, 제 이름은 {whoami.persons[i]} 이고, 나이는 {whoami.persons[i]} 세이고, {whoami.persons[i]} 에서 거주합니다.')

    @staticmethod
    def main():
        whoami = WhoAmI(input('Input Student Name : '))
        for i in ['이름' , '나이' , '주소']:
            whoami.addPerson(input(f'{i} : '))

WhoAmI.main()
