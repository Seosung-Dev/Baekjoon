def main():
    x = int(input())
    y = int(input())

    if y > 0:
        if x > 0:
            print("1")
        elif x < 0:
            print("2")
    elif y < 0:
        if x < 0:
            print("3")
        elif x > 0:
            print("4")

if __name__ == "__main__":
    main()