def merge(left, right):
    print('Left and right:', left, right)
    left_index, right_index = 0, 0
    sorted_array = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1
    sorted_array += left[left_index:]
    sorted_array += right[right_index:]
    print('Intermediate result:', sorted_array)
    return sorted_array

def merge_sort(array):

    if len(array) == 1:
        return array
    
    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)

if __name__ == '__main__':
    arr = [9,6,5,0,8,2,7,1,3]

    result = merge_sort(arr)
    print('Sorted array:', result)