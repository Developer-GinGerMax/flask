
class Person(object):
    def __init__(self,name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def to_string(self):
        print(f'\n[Person Info] \nName: {self.name} \nAge: {self.age} \nAddress: {self.address}\n')

    @staticmethod
    def main():
        persons = []
        while 1:
            print('0-EXIT 1-ADD 2-PRINT')
            menu = input('Choose One Number')
            if menu =='1':
                persons.append(Person(input('name'),input('age'),input('address')))
            elif menu =='2':
                for i in persons:
                    i.to_string()
            elif menu =='0':
                return

Person.main()