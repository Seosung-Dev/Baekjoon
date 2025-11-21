import math
def calculate(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    absolute_value = abs(r1 - r2)
    if d == 0 and r1 == r2:
        return -1
    elif d > r1 + r2:
        return 0
    elif d == r1 + r2:
        return 1
    elif d == absolute_value:
        return 1
    elif absolute_value < d < r1 + r2:
        return 2
    else:
        return 0
def main():
    t = int(input())
    for _ in range(t):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        print(calculate(x1, y1, r1, x2, y2, r2))
if __name__ == "__main__":
    main()