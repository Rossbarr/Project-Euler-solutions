#include <iostream>
#include <vector>

int sum_of_proper_divisors(int n) {
    int i = 1;
    int sum = 1;
    while (i*i <= n) {
        i += 1;
        if (n % i == 0) {
            sum += i;
            int j = n / i;
            if (i != j) {
                sum += j;
            }
        }
    }
    return sum;
}

int sum_of_amicable_numbers(int n) {
    int sum = 0;
    int i = 0;
    while (i < n) {
        i += 1;
        int j = sum_of_proper_divisors(i);
        if (i < j && sum_of_proper_divisors(j) == i) {
            sum += i + j;
        }
    }
    return sum;
}

int main() {
    std::cout << sum_of_amicable_numbers(10000) << "\n";
}
