#include <iostream>

int multiples_of_3_and_5() {
	int sum = 0;
	for (int i = 1; i < 1000; i ++) {
		if (i % 3 == 0 || i % 5 == 0) {
			sum = sum + i;
		}
	}
	return sum;
}

int even_fibonacci_numbers() {
	int sum = 2;
	int x = 1;
	int y = 2;
	int z;
	while (z < 4000000) {
		z = x + y;
		x = y;
		y = z;
		if (z % 2 == 0) {
			sum = sum + z;
		}
	}
	return sum;
}

bool is_prime(unsigned long int num) {
	for (int i = 2; i < num; i++) {
		if (num % i == 0) {
			return false;
		}
	}
	return true;
}

unsigned long int largest_prime_factor(unsigned long int num) {
	int lpf = 1;
	for (int i = 2; i < num; i++) {
		if (num % i == 0 && is_prime(i)) {
			lpf = i;
		}
	}
	return lpf;
}

bool is_palindrome(unsigned long int num) {
	unsigned long int n = num;
	unsigned long int rev = 0;
	unsigned short int digit = 0;
	do {
		digit = num % 10;
		rev = (rev * 10) + digit;
		num = num / 10;
	} while (num != 0);
	return (n == rev);
}

int largest_palindrome_product() {
	int result = 0;
	for (int a = 900; a < 1000; a++) {
		for (int b = 900; b < 1000; b++) {
			if (a * b > result && is_palindrome(a * b)) {
					result = a * b;
					std::cout << "updated result as " << result << "\n";
			}
		}
	}
	return result;
}

unsigned int smallest_multiple() {
	unsigned int max;
	for (unsigned short int i = 1; i <= 20; i++) {
		max = max * i;
	}
	for (unsigned int i = 2520; i <= max; i++) {
		unsigned short int counter = 0;
		for (unsigned short int d = 2; d <= 20; d++) {	
			if (i%d == 0) {
				counter ++;
			}
		}
		if (counter == 19) {
			return i;
		}
	}
	return 0;
}

int main() {
	std::cout << smallest_multiple() << '\n';
}
