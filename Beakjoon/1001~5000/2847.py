def main():
    N = int(input())
    lists = []
    answer = 0
    x = 0
    for _ in range(N):
        a = int(input())
        lists.append(a)
    x = lists[N-1]
    for i in range(len(lists)-1, -1, -1):
        if i != len(lists)-1:
            if lists[i] >= x:
                while lists[i] >= x:
                    answer += 1
                    lists[i] -= 1
            x = lists[i]
    print(answer)
    return 0
if __name__ == "__main__":
    main()