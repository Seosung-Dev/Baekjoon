def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    answer = []
    for a in A:
        if a < X:
            answer.append(a)
    print(*answer)
    
if __name__ == "__main__":
    main()