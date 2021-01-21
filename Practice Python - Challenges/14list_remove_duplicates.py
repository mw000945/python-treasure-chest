# https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
a = [1,1,2,2,3,4,4,4,5,6,7,8,8]

def remove_dup(l):
    return list(set(l))

print(remove_dup(a))
