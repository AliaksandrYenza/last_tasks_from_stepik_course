def reader_from_file(filename):
    list = []
    a = {}
    with open(filename, encoding="utf8") as f:
        a = {str(i): [0] for i in range(1, 12)}
        for line in f:
            list += line.split()
    for i in range(0,len(list),3):
        if list[i] in a.keys():
            a[list[i]].append(int(list[i+2]))
    return a


def print_res(a):
    for i in range(1,12):
        if a[str(i)] == [0]:
            a[str(i)] = '-'
        else:
            theSum = 0
            c = 0
            for j in a[str(i)]:
                theSum = theSum + j
                c += 1
            a[str(i)] = theSum / (c-1)

    for g in a.keys():
        print(f'{g} {a[g]}')



if __name__ == '__main__':
    a = reader_from_file('file.txt')
    print_res(a)