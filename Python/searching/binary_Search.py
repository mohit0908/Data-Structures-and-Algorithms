import time

def binarysearch(list, item):
    first = 0
    last = len(list) - 1
    found = False
    while first <= last and not found:
        mid = (last + first)//2
        if list[mid] == item:
            found = True
        elif list[mid] > item:
            last = mid -1
        else:
            first = mid + 1

    return mid

def binarysearch_recursive(list, first, last, item):
    
    if first <= last:
        mid = (first + last)//2
        if list[mid] == item:
            return mid
        elif list[mid] < item:
            return binarysearch_recursive(list, mid +1, last, item)
        else:
            return binarysearch_recursive(list, first, mid -1, item)
    else:
        return -1
        
if __name__ == '__main__':
    item_list = list(range(10000))
    item = 37
    start_time = time.time()
    result_index = binarysearch(item_list, item)
    print('Time taken - Iterative:', time.time() - start_time)
    start_time = time.time()
    recursive_index = binarysearch_recursive(item_list, 0, len(item_list)-1, item)
    print('Time taken - Recursive:', time.time() - start_time)
    print('Index: ', result_index)
    print('Index: ', recursive_index)