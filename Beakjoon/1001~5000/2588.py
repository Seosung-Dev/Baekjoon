def main():
    a = int(input())
    b = int(input())
    print(a*(b%10))
    print(int(a*((b%100)-(b%10))/10))
    print(a*int(b/100))
    print(a*b)
if __name__ == "__main__":
    main()