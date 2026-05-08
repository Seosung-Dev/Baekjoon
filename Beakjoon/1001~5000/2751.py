import sys
input = sys.stdin.readline

def main():
    N = int(input())
    lists = set()
    for _ in range(N):
        lists.add(int(input()))
    lists = sorted(lists)
    for i in lists:
        print(i)
    return 0
if __name__ == "__main__":
    main()