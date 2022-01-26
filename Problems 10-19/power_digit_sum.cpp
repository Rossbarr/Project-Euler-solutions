#include <iostream>
#include <vector>

typedef std::vector<unsigned int> digits;

unsigned int power_digit_sum(unsigned int exponent) {
    std::vector<digits> cache;
    cache.push_back({ 1 });

    for (unsigned int current = cache.size(); current <= exponent; current++) {
        auto power = cache.back();
        unsigned int carry = 0;
        for (auto& i : power) {
            i = i * 2 + carry;

            if (i >= 10) {
                i -= 10;
                carry = 1;
            } else {
                carry = 0;
            }
        }

        if (carry != 0) {
            power.push_back(carry);
        }

        cache.push_back(power);
    }

    unsigned int sum = 0;
    for (auto i : cache[exponent]) {
        sum += i;
    }
    return sum;
}

int main() {
    std::cout << power_digit_sum(1000) << "\n";

    return 0;
}
