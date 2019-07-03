def find_smaller(num_list):
    stack = []

    for num in num_list:
        while len(stack) > 0 and stack[-1] > num:
            stack.pop() 
        if len(stack) == 0:
            print('_', end = ',')
        else:
            print(stack[-1], end = ',')


        stack.append(num)



num = int(input())

for _ in range(num):
    num_list = list(map(int, input().strip().split()))
    print('Num list:', num_list)
    find_smaller(num_list)