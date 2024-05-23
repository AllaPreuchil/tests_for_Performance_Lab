import sys


if __name__ == '__main__':
    file_nums = sys.argv[1]
    nums = []
    with open(file_nums) as fh:
        for item in fh:
            nums.append(int(item))
    len_sum = 0
    list_len = []
    num1 = min(nums)
    num2 = max(nums)
    for i in range(num2 - num1 + 1):
        if num1 <= num2:
            for j in nums:
                length = abs(num1 - j)
                len_sum += length
        if len_sum != 0:
            list_len.append(len_sum)
        num1 += 1
        len_sum = 0
    print(min(list_len))



