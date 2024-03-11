array = [5, 3, 8, 6, 2,7,9]

import random
class Bubble:
    
    def Sort(arr):
        for x in range(0,len(arr)):
            for i in range(0,len(arr)-1):# Compare the the element with the next element
                if arr[i] > arr[i+1]:# If the element is greater than the next element, swap them
                   arr[i], arr[i+1] = arr[i+1], arr[i]# Shorthand to swap elements.
                   # Repeat this whole process for each item in the array.
                   # Un-optimized
        return arr

    def optimizedSort(arr):
        for x in range(0,len(arr)):
                for i in range(0,len(arr)-x-1):
                    # Since you are pushing the biggest element to the end each time,
                    # The last item is already sorted so there is no need to compare it.
                    if arr[i] > arr[i+1]:
                       arr[i], arr[i+1] = arr[i+1], arr[i]
        return arr

    def furtherOptimizedSort(arr):
        for x in range(0,len(arr)):
            swap = False# If no swap occurs, the array is sorted.
            for i in range(0,len(arr)-x-1):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    swap = True
            if swap == False:# If no swap occurs, the array is sorted which means we can break the loop.
                break
        return arr

    def testAll():
        arr = random.sample(range(-99, 99), 7)
        print(f'Original: {arr}')
        print(Bubble.Sort(arr))
        print(Bubble.optimizedSort(arr))
        print(Bubble.furtherOptimizedSort(arr))
     
    def randomCheck():
        for x in range(0,10):
            arr = random.sample(range(-99, 99), 7)
            regBubble = Bubble.Sort(arr)
            optBubble = Bubble.optimizedSort(arr)
            furtherOptBubble = Bubble.furtherOptimizedSort(arr)
            sortedArr = sorted(arr)
            if sortedArr != regBubble:
                print(f'Failed Regular Bubble Sort: {arr}')
            if sortedArr != optBubble:
                print(f'Failed Optimized Bubble Sort: {arr}')
            if sortedArr != furtherOptBubble:
                print(f'Failed Further Optimized Bubble Sort: {arr}')
                

Bubble.randomCheck()
Bubble.testAll()





"""
take item  (from second)
compare to previous, if it is less than, swap,
else, pass.

"""
def insertion(arr):
    for pos in range(1,len(arr)):# Starting from the second element, got through the whole array
        current = arr[pos]# Store the value at the current element
        i = pos-1 # The position of the previous element 
        
        while i >= 0 and current < arr[i]:# If the previous element is actually in the array and the current element is smaller than the one before it       
            arr[i+1] = arr[i]             # set the item stored in i+1 (which would be 'pos') to whats stored in position i
            i -= 1                        # Decrement i
        arr[i+1] = current                # Set the value of the previous element to the current element
        

    return arr
#insertion(arr)

def testInsertion():
    print("Insertion Sort")
    for x in range(0,2):
        arr = random.sample(range(-99, 99), 7)
        print(f'Original: {arr}')
        print(insertion(arr))

testInsertion()

