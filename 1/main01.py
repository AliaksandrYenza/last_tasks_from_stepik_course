#https://stepik.org/lesson/3380/step/1?unit=963
import itertools

def read_from_file():
    st = [line.rstrip('\n') for line in open('from.txt')]
    x_list = [line.split(';') for line in st]
    print(f'x_list = {x_list}')
    vs = [(x[0], x[2]) for x in x_list]
    print(f'vs = {vs}')
    import itertools
    clubs = set(itertools.chain.from_iterable(vs))
    print(f'clubs = {clubs}')
    res = {club: [0, 0, 0, 0, 0] for club in clubs}
    for kom1, gol1, kom2, gol2 in x_list:
        res[kom1][0] += 1
        res[kom2][0] += 1
        if int(gol1) > int(gol2):
            res[kom1][1] += 1
            res[kom1][4] += 3
            res[kom2][3] += 1
        elif int(gol1) < int(gol2):
            res[kom2][1] += 1
            res[kom2][4] += 3
            res[kom1][3] += 1
        elif int(gol1) == int(gol2):
            res[kom1][2] += 1
            res[kom1][4] += 1
            res[kom2][2] += 1
            res[kom2][4] += 1
    for club in clubs:
        a = ' '.join(map(str, res[club]))
        print('{}:{}'.format(club, a))


if __name__ == '__main__':
    read_from_file()
