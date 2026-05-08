def main():
    N = int(input())
    d = 0 #약수의 합
    for i in range(1, N+1):
        if N % i == 0: #약수 판별식
            d += i
    print(d)
    return 0
if __name__ == "__main__":
    main()