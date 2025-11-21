def main():
    N = int(input())
    X = 1000-N #거스름돈 총 합
    total_500 = 0
    total_100 = 0
    total_50 = 0
    total_10 = 0 #출력
    if N == 0:
        print(0000)
    else:
        for i in range(4):
            if i == 0:
                A = X//500 #X를 나눴을때의 몫
                total_500 += A
                X -= A*500
            elif i == 1:
                A = X//100
                total_100 += A
                X -= A*100
            elif i == 2:
                A = X//50
                total_50 += A   
                X -= A*50
            else:
                A = X//10
                total_10 += A  
                X -= A*10
    print(total_500, total_100, total_50, total_10)
    return 0
if __name__ == "__main__":
    main()