def main():
    N = int(input())
    lists = []
    answer = []
    for _ in range(N):
        A, B = input().split()
        lists.append((int(A), B))
    lists.sort(key=lambda x: x[0])
    for A, B in lists:
        print(A, B)
    return 0
if __name__ == "__main__":
    main()