def selection_sort(arr):
    if len(arr) <=1:
        return 
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

        print('Step {} array:{}'.format(i, arr))

if __name__ == '__main__':
    arr = [9,6,5,0,8,2,7,1,3]

    selection_sort(arr)
    print('Sorted array:', arr)