def main():
    N = int(input()) #구구단을 출력(하기위해 받는 입력(N단)
    for i in range(1, 10, 1):
        print(N, "*", i, "=", N*i)
if __name__ == "__main__":
    main()