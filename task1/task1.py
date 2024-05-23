import sys


if __name__ == '__main__':
    n = int(sys.argv[1])
    m = int(sys.argv[2])

    mylist = [i + 1 for i in range(n)]
    route = []
    num1 = 0
    num2 = m - 1
    route.append(mylist[num1])
    while num2 != 0:
        num1 = num2
        num2 = (num2 + m - 1) % n
        route.append(mylist[num1])

    print(*route, sep='')
