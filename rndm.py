import random

count = 1000
def qsort(_data):
    if len(_data) <=1:
        return data
    
    print(len(_data))

    pivot = _data[len(_data)//2]
    smaller = [x for x in _data if x < pivot]
    bigger = [x for x in _data if x > pivot]
    same = [x for x in _data if x == pivot]

    return qsort(smaller) + same + qsort(bigger)




data = [random.randint(0, 99) for _ in range(count)]

data = qsort(data)

data.sort()

print(data)
data = data[80:]
data = data[:len(data)-80]
