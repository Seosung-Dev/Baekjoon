#include <iostream>
#include <list>
#include <algorithm>

int main() {
    int N = 0;
    std::cin >> N;

    std::list<int> A = {};
    int Temp = 0;
    for (int i = 0; i < N; i++) {
        Temp = 0;
        std::cin >> Temp;
        A.push_back(Temp);
    }

    std::cout << *std::min_element(A.begin(), A.end());
    std::cout << " " <<*std::max_element(A.begin(), A.end()) << "\n";

    return 0;
}