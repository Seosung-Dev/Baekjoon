def main():
    M = int(input())
    N = int(input())
    answer = []
    for i in range(M, N+1, 1):
        a = 0
        for j in range(2, i, 1):
            if i % j == 0:
                a = 1
                break
        if a == 0:
            answer.append(i)
    if 1 in answer:
        answer.remove(1)
    if answer == []:
        print(-1)
    else:
        print(sum(answer))
        print(min(answer))
    return 0
if __name__ == "__main__":
    main()