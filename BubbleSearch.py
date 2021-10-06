"""
Bubble_sort Algorythm

"""

oldlist = [10, 75, 43, 15, 24, -4, 27]

def bubble_sort(mylist):
    last_item = len(mylist) - 1
    for i in range(0, last_item):
        for x in range(0, last_item - i):
            print(mylist)
            if mylist[x] > mylist[x+1]:
                mylist[x], mylist[x+1] = mylist[x+1], mylist[x]
    return mylist

print("Old list:", oldlist)
newlist = bubble_sort(oldlist).copy()
print("Newlist", newlist)