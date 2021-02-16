def find_uniq(arr):
    for x in arr:
        if x != arr[0]:
            return x

print(find_uniq([ 1, 1, 1, 1, 1, 3 ]))