import math

def main():
    T = int(input())
    gcd_list = []
    for _ in range(T):
        sum_gcd = 0
        lists = list(map(int, input().split()))
        for i in range(1, len(lists), 1):
            for j in range(1, len(lists), 1):
                if i<j and i != j:
                    sum_gcd += math.gcd(lists[i], lists[j])
        gcd_list.append(sum_gcd)
    for k in gcd_list:
        print(k)
    return 0
if __name__ == "__main__":
    main()