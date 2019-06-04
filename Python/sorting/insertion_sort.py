def insertion_sort(arr):
    sorted_length = 1
    for i in range(sorted_length, len(arr)):
        for j in range(sorted_length, 0, -1):
            if arr[j] < arr[j-1]:
                print('Condition met:', arr[j], arr[j-1])
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
                print('Step array:', arr)
            else:
                break
        print('Step {} completed. Array : {}'.format(sorted_length, arr))
        sorted_length += 1

if __name__ == '__main__':
    arr = [9,6,5,0,8,2,7,1,3]

    insertion_sort(arr)
    print('Sorted array:', arr)