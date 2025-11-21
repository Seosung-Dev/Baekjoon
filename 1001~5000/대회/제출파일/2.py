def main():
    N = int(input())
    X = 0
    answer = 0
    for i in range(1, N+1):
        for j in range(1, i+1):
            X += 1
    for k in range(1, X+1):
        answer += k
    print(answer)
    return 0
if __name__ == "__main__":
    main()