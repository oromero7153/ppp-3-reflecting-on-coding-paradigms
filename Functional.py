"""Functional Oriented Programming"""

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

"""
1. The data remains unchanged, only change is the formatting.

2. Yes because there are no side effects to the function, the input and output are not changed.

3. It is not because it does take or returns an function.

4. There is other ways, but this method is easier since the data isnt changed.
"""

