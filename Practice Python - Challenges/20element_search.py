# https://www.practicepython.org/exercise/2014/11/11/20-element-search.html
l = [1, 2, 5, 8, 10, 16, 23, 28, 29, 30, 31, 32, 56]

def binarySearch(arr, l, r, x):
    if r >= l:

        mid = l + (r - l) // 2

        if arr[mid] == x:
            return "in the list"
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        return "not in the list"

n = int(input("number: "))
print(binarySearch(l, 0, len(l), n))
