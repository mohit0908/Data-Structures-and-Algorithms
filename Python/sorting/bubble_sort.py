def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            print(i, j)
            if arr[j] >  arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print('Middle array:', arr)
        print('Step {} array:{}'.format(i, arr))


if __name__ == '__main__':
    arr = [9,6,5,0,8,2,7,1,3]

    bubble_sort(arr)
    print('Sorted array:', arr)