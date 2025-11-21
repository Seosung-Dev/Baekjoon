def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        result = pow(a, b, 10)
        print(10 if result == 0 else result)

if __name__ == "__main__":
    main()