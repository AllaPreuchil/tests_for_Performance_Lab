import sys
import math


def check_distance_to_circle(circle_x1, circle_y1, radius, point_x2, point_y2):
    distance = math.sqrt(abs((circle_x1 - point_x2) ** 2 + (circle_y1 - point_y2) ** 2))
    if distance == radius:
        return 0
    elif distance < radius:
        return 1
    elif distance > radius:
        return 2


if __name__ == '__main__':
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    mylist = []
    with open(file1) as fh:
        for item in fh:
            mylist.append(item.split())
    x1 = int(mylist[0][0])
    y1 = int(mylist[0][1])
    r = int(mylist[1][0])

    with open(file2) as fh:
        for item in fh:
            a = item.split()
            x2 = int(a[0])
            y2 = int(a[1])
            print(check_distance_to_circle(x1, y1, r, x2, y2))
