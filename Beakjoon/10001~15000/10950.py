def main():
    T = int(input())
    list1 = []
    for _ in range(T):
        A, B = map(int, input().split())
        list1.append(A)
        list1.append(B)
    for i in range(0, T*2, 2):
        print(list1[i]+list1[i+1])
if __name__ == "__main__":
    main()