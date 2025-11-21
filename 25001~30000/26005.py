def main():
    N = int(input())
    N_square = N**2 + 0.0000001
    if N == 1:
        print(0)
    elif N%2 == 0: print(int(N_square / 2))
    else: print(int((N_square / 2) + 1))
    return 0
if __name__ == "__main__":
    main()