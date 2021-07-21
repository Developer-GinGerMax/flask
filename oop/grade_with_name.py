'''
국어 kor, 영어 eng, 수학 math 를 입력받아서
학생이름, 총점, 평균점수를 통해 A ~ F 학점을 출력하시오
'''

class Grade(object):
    def __init__(self, name):
        self.name = name
        self.scores = []

    def addScores(self, score):
        self.scores.append(score)

    def avg(self):
        return sum(self.scores) / len(self.scores)

    @staticmethod
    def main():
        grade = Grade(input('Input Student Name : '))
        '''
        kor = int(input('Korean: '))
        eng = int(input('English: '))
        math = int(input('Math: '))
        '''
        for i in ['Korean' , 'English' , 'Math']:
            grade.addScores(int(input(f'{i} : ')))
        avg = grade.avg()
        if avg >= 90:
            result = 'A'
        elif avg >= 80:
            result = 'B'
        elif avg >= 70:
            result = 'C'
        elif avg >= 60:
            result = 'D'
        elif avg >= 50:
            result = 'E'
        else:
            result = 'F'
        print(f'{result}')


Grade.main()