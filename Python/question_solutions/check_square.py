import numpy as np


def calculate_distance(point1, point2):
    # Calculate Euclidean distance between 2 points
    distance = np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    return distance

def check_diag(distance):
    # Find diagonal point and checks if diagonal distance is np.sqrt(side)
    index = 1
    if (distance[index] == distance[index + 1] != distance[index + 2]) and np.sqrt((distance[index]**2)*2) == distance[index + 2]:
        diagonal_point = index + 2
    elif (distance[index] == distance[index + 2] != distance[index + 1]) and np.sqrt((distance[index]**2)*2) == distance[index + 1]:
        diagonal_point = index + 1
    elif (distance[index] != distance[index + 2] == distance[index + 1]) and np.sqrt((distance[index + 1]**2)*2) == distance[index]:
        diagonal_point = index
    else:
        diagonal_point = False
    return diagonal_point

def check_angle(point1,point2, point3):
    # Checks angle between 3 points. Point 1 being common point between 2 vectors
    # Formula: cos(theta) = np.dot(vector1, vector2)/(|vector1|*|vector2|)
    vector21 = np.array(point2) - np.array(point1)
    vector31 = np.array(point3) - np.array(point1)
    angle = np.dot(vector21, vector31)/(np.linalg.norm(vector21) * np.linalg.norm(vector31))
    angle = np.arccos(angle)    
    return np.degrees(angle)

def check_square(coordinates):
    status = False
    d_list = []
    for index in range(len(coordinates)):
        if index > 0:
            d_list.append(calculate_distance(coordinates[0], coordinates[index]))
    l = [0]
    l.extend(d_list)
    diagonal_point = [check_diag(l)]
    side_distance = []
    if diagonal_point[0]:
        non_diag_point = list(set(list(range(4))) - set(diagonal_point))
        status = True
        if status:
            for i in range(len(coordinates)):
                if i != 0 and i != diagonal_point[0]:
                    side_distance.append(calculate_distance(coordinates[diagonal_point[0]], coordinates[i]))
                    same_distance = l[i]
            if side_distance[0] == side_distance[1] == same_distance:
                status = True
            else:
                status = False
                return status
            angle = check_angle(coordinates[non_diag_point[0]], coordinates[non_diag_point[1]],coordinates[non_diag_point[2]])
            if angle == 90:
                status = True
            else:
                status = False
                return status
    else:
        return status
    return status

#  Input accepting code
# E.g. Space separated coordinate values
# 2
# 10 10 20 20 10 20 20 10
# 1 1 2 2 1 -1 -1 2

#  Number of test cases

try:
    num_test_cases = int(input())

    # Iterate for number of test cases and accept coordinates input
    for k in range(num_test_cases):
        coordinates = []
        try:
            num = list(map(int, input().strip().split()))
        except:
            print('Enter integer input')
            continue
        if len(num) < 8:
            print('Enter 8 coordinates...')
            continue
        coordinates.extend([(num[0], num[1]),(num[2], num[3]),(num[4], num[5]),(num[6], num[7])])
        status = check_square(coordinates)
        if status is True:
            status = 'Yes'
        else:
            status = 'No'
        print(status)
except:
    print('Enter integer input')
        