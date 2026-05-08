def main():
    import math
    N = int(input())
    N_measure = list(map(int, input().split()))
    print(max(N_measure)*min(N_measure))
    return 0
if __name__ == "__main__":
    main()