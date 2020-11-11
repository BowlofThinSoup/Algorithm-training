'''
Name:Sort.py
Data:2020-11-11
Author:QingTang
'''

IN = [12,23,2,35,5,8,42,98,75,35]

def BubbleSort(ListBeforeSort):
    Input = ListBeforeSort
    listLen = len(Input)
    for i in range(0,listLen):
        for j in range(0,listLen-i-1):
            if Input[j] > Input[j+1]:
                k = Input[j+1]
                Input[j+1] = Input[j]
                Input[j] = k
    return Input

def SelectionSort(ListBeforeSort):
    Input = ListBeforeSort
    ListLen = len(Input)
    for i in range(0,ListLen):
        MinIndex = i
        for j in range(i,ListLen):
            if Input[j] < Input[MinIndex]:
                MinIndex = j
        a = Input[i]
        Input[i] = Input[MinIndex]
        Input[MinIndex] = a
    return Input


print(BubbleSort(IN))
print(SelectionSort(IN))


