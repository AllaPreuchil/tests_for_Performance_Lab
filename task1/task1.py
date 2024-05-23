import sys


def get_route(arg1):
    n = int(arg1[1])
    m = int(arg1[2])

    mylist = [i + 1 for i in range(n)]
    route = []
    num1 = 0
    num2 = m - 1
    route.append(str(mylist[num1]))
    while num2 != 0:
        num1 = num2
        num2 = (num2 + m - 1) % n
        route.append(str(mylist[num1]))

    return ''.join(route)



if __name__ == '__main__':

    print(get_route(sys.argv))
