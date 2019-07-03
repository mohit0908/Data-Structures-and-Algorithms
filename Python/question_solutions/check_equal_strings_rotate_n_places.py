def check_string(str1, str2, n):
    status = False
    if len(str1) < 2 or len(str2) < 2:
        return status
    
    reconstruct1 = str2[-2:] + str2[:-2]
    reconstruct2 = str2[2:]+str2[:2]
    print('Reconstruct:', reconstruct1, reconstruct2)
    if str1 == reconstruct1:
        status = True
    elif str1 == reconstruct2:
        status = True
    else:
        status = False

    return status


num = int(input())
rotate = 2
for i in range(num):
    str1 = input()
    str2 = input()

    status = check_string(str1, str2, rotate)
    if status is True:
        print(1)
    else:
        print(0)
