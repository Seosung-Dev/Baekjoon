import re

def main():
    N = int(input())
    nums = []
    for i in range(N):
        a = input()
        for x in re.findall(r'\d+', a):
            nums.append(int(x))
    nums.sort()
    for num in nums:
        print(num)
    return 0
if __name__ == "__main__":
    main()