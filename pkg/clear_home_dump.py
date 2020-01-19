import sys
import get_data

if __name__ == '__main__':

    class_, weekday = get_data.get(sys.argv)

    with open(class_, 'r') as inp:

        FILE = inp.readlines()
        access_indexes = list(range(len(FILE)))

        for item in range(len(FILE)):
            try:
                if FILE[item].split()[0] == weekday:
                    access_indexes.remove(item)
            except:
                pass
    with open(class_, 'w') as ouf:
        for item in access_indexes:

            ouf.write(FILE[item])
            ouf.write('\n')
