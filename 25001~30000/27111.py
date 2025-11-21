import sys
input = sys.stdin.readline
def main():
    N = int(input())
    total = 0
    enter = [0] * 200001
    for _ in range(N):
        x, y = map(int, input().split())
        if y == 0:
            if enter[x] == 0:
                total += 1
            else: enter[x] = 0
        elif y == 1:
            if enter[x] == 1:
                total += 1
            else: enter[x] = 1
    total += sum(enter)
    print(total)
    return 0
if __name__ == "__main__":
    main()