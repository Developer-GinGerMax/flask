

class Person(object):
    def __init__(self, name, age, adds):
        self.name = name
        self.age = age
        self.adds = adds

    def to_string(self, param):
        print(f'안녕하세요, 제 이름은 {param.name} 이고, 나이는 {param.age} 이고, {param.adds} 에 거주합니다.')


    @staticmethod
    def main():
        count = int(input('How many?'))
        for i in range(count):
            person = Person(input('name '), input('age '), input('adds '))
        for i in range(count):
            person.to_string(person)

Person.main()