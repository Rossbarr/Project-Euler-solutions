#include <iostream>
#include <cmath>

unsigned int num_divisors(unsigned long int num) {
    unsigned int count = 2;
    for (unsigned long int i = 2; i*i <= num; i++) {
        if (num % i == 0) {
            count = count + 2;
        }
    }
    return count;
}

unsigned long int highly_divisible_triangular_numbers(unsigned int limit) {
    bool found = false;
    unsigned int count = 0;
    unsigned int current_number = 0;
    while (!found) {
        count += 1;
        current_number += count;
        std::cout << current_number << "\n";
        if (num_divisors(current_number) >= limit) {
            found = true;
        }
    }
    return current_number;
}

int main() {
    std::cout << highly_divisible_triangular_numbers(500) << "\n";
}
