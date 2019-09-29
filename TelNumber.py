from itertools import product

tel_numbers = {
               '0': ' ',
               '1': '#',
               '2': ('a', 'b', 'c'),
               '3': ('d', 'e', 'f'),
               '4': ('g', 'h', 'i'),
               '5': ('j', 'k', 'l'),
               '6': ('m', 'n', 'o'),
               '7': ('p', 'q', 'r'),
               '8': ('s', 't', 'v'),
               '9': ('w', 'x', 'y', 'z')}
S = input()
A = []
for i in S:
    A.append(my_dict[i])
listik = list(product(*A))
listik2 = []
for i in range(len(listik)):
    listik2.append(''.join((listik[i])))
print(listik2)
