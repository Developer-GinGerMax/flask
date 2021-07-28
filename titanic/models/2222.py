def te1st():

    names = [ '초' , '루' , '상' , '조' ]
    names.append('해적왕')
    [print(name, '왔니?')for name in names if len(name) > 0 ]
    print( [(i, '왔니') for i in names if len(i) > 0] )

if __name__ == '__main__':
    te1st()
