def get(argv):

    if argv[1] == '-a':
        class_ = '11А.txt'
    elif argv[1] == '-b':
        class_ = '11Б.txt'
    elif argv[1] == '-v':
        class_ = '11В.txt'
    elif argv[1] == '-g':
        class_ = '11Г.txt'

    if argv[2] == '0':
        weekday = 'понедельник'
    elif argv[2] == '1':
        weekday = 'вторник'
    elif argv[2] == '2':
        weekday = 'среда'
    elif argv[2] == '3':
        weekday = 'четверг'
    elif argv[2] == '4':
        weekday = 'пятница'

    return class_, weekday
