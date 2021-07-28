"""
학생이름, 국어 kor, 영어 eng, 수학 math 를 입력받아서
학생이름, 평균, 학점을 출력하시오
"""
class Grade(object):

    def __init__(self, name):
        self.name = name
        self.scores = []

    def addScores(self, score):
        self.scores.append(score)

    def avg(self):
        return sum(self.scores) / len(self.scores)


def main():
    grade = Grade(input('Input Student Name:'))
    for i in ['Korean','English','Math']:
        grade.addScores(int(input(f'{i}: ')))
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


if __name__ == '__main__':
    main()



