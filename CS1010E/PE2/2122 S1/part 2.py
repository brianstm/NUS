# PE2 Part 2


def create_map_file():
    pmap1list = ['0000011111',
                 '0000X11111',
                 '0000111111',
                 '000X111111',
                 '0001111111',
                 '0222111111',
                 '2222211111',
                 '2222222111',
                 '2222222211',
                 '2222222222',
                 '2222222222']
    pmap2list = ['000000X22222',
                 '00000X222222',
                 'XXXXX2222222',
                 '111122222222',
                 '111122222222',
                 '111X22222222',
                 '111222222222',
                 '111222222222',
                 '11X222222222',
                 '112222222222']
    f1 = open("pmap1.txt", "w")
    for line in pmap1list:
        f1.write(line+'\n')
    f1.close()
    f2 = open("pmap2.txt", "w")
    for line in pmap2list:
        f2.write(line+'\n')
    f2.close()


create_map_file()


def buyable_map(filename):
    with open(filename, 'r') as f:
        map = [list(line.strip()) for line in f]

    buyable = [['.' for _ in row] for row in map]

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'X':
                buyable[i][j] = 'X'
                continue

            for n in [-1, 0, 1]:
                for m in [-1, 0, 1]:
                    if (n != 0 or m != 0) and (0 <= i+n < len(map)) and (0 <= j+m < len(map[i])):
                        if map[i+n][j+m] != map[i][j]:
                            buyable[i][j] = map[i][j]
                            break

    return '\n'.join(''.join(row) for row in buyable)


print(buyable_map('pmap1.txt'))
print(buyable_map('pmap2.txt'))
