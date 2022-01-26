#include <iostream>
#include <map>

struct IntDefaultedToMinusOne {
    unsigned long int v = -1;
};

std::map<unsigned long int, IntDefaultedToMinusOne> g_nums;

unsigned long int next_num(unsigned long int x) {
    unsigned long int result;
    if (x % 2 == 0) {
        result = x / 2;
    } else {
        result = 3 * x + 1;
    }
    return result;
}

unsigned long int recursive_part(unsigned long int num) {
    if (g_nums[num].v != -1) {return g_nums[num].v;}

    unsigned long int seq_length = recursive_part(next_num(num)) + 1;
    g_nums[num].v = seq_length;
    return seq_length;
}

unsigned long int collatz_length() {
    unsigned long int longest_sequence = 0;
    unsigned long int longest_seq_num = 0;

    unsigned long int seq_length;
    for (unsigned long int i = 1; i < 1000000; i++) {
        std::cout << i << "\n";
        seq_length = recursive_part(i);
        if (seq_length > longest_sequence) {
            longest_sequence = seq_length;
            longest_seq_num = i;
        }
    }
    return longest_seq_num;
}


int main() {

    g_nums[1].v = 1;
    g_nums[2].v = 2;
    g_nums[4].v = 3;

    std::cout << collatz_length() << "\n";
}
