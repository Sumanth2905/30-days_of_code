'''
program to convert decimal into binary and find max number of consecutive 1's.
'''
if __name__ == '__main__':
    n = int(input())
    count = 0
    while n:
        n &= n << 1
        count += 1
    print(count)