def main():
    N, M = map(int, input().split())
    if M != 1:
        lists = []
        answer = []
        for i in range(1, N*(N-1)):
            for j in range(1, N+1):
                x = j
                for k in range(1, M+1):
                    lists.append(k)
                    if len(lists) == M-1 and [x, *lists] not in answer:
                        print(x, lists)
                        if x not in lists:
                            lists = [x, *lists]
                            answer.append(lists)
                        lists = []
        answer.sort()
        for g in answer:
            print(*g)
    else:
        for i in range(1, N+1):
            print(i)
    return 0
if __name__ == "__main__":
    main()