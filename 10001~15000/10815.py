def main():
    import sys
    input = sys.stdin.readline

    answer = []

    N = int(input())
    numbers_on_cards = set(map(int, input().split()))
    M = int(input())
    queries = set(map(int, input().split()))
    # Check(N, numbers_on_cards, M, queries)

    for i in queries:
        if i in numbers_on_cards:
            answer.append(1)
        else:
            answer.append(0)

    print(*answer)
    return 0

#def Check(N, numbers_on_cards, M, queries):
#    if N < 1 or N > 10000000:
#        print("Error")
#    if min(numbers_on_cards) < -10000000 or max(numbers_on_cards) > 10000000:
#        print("Error")
#    if M < 1 or M > 500000:
#        print("Error")
#    if min(queries) < -10000000 or max(queries )> 10000000:
#        print("Error")

if __name__ == "__main__":
    main()