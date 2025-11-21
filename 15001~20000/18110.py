import sys
input = sys.stdin.readline

def main():
    N = int(input())
    lists = []
    list_2 = []
    for _ in range(N):
        lists.append(int(input()))
    lists.sort()
    a = round(N/6)
    list_2 = lists[a: -a]
    print(round(sum(list_2)/len(list_2)))
    return 0
if __name__ == "__main__":
    main()