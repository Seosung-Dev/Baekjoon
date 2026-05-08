import math
def main():
    n, m = map(int, input().split(":"))
    a = math.gcd(n, m)
    n/=a
    m/=a
    print(f"{int(n)}:{int(m)}")
    return 0
if __name__ == "__main__":
    main()