def main():
    A, B = map(int, input().split())
    C = int(input())
    total = A*60 + B + C
    Hour = (total // 60) % 24
    Minute = total % 60
    print(Hour, Minute)
if __name__ == "__main__":
    main()