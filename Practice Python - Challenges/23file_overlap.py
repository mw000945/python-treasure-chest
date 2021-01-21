# https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html
FILE1 = './resources/23numbers1.txt'
FILE2 = './resources/23numbers2.txt'

with open(FILE1, 'r') as f:
    f1cont = []
    for line in f.readlines():
        f1cont.append(str(line).rstrip())
    f.close()

with open(FILE2, 'r') as f:
    f2cont = []
    for line in f.readlines():
        f2cont.append(str(line).rstrip())
    f.close()

l1 = len(f1cont)
l2 = len(f2cont)

overlapping = []
if l1 > l2:
    for x in f1cont[l2:]:
        overlapping.append(x)
elif l2 > l1:
    for x in f2cont[l1:]:
        overlappinga.append(x)

print(overlapping)

# better solution possible? propably
