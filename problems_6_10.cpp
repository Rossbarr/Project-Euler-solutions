#include <iostream>
#include <string>

unsigned long int sum_square_difference(unsigned int low, unsigned int high) {
	unsigned long int sum_squares = 0;
	unsigned long int square_sum = 0;
	for (unsigned int i = low; i <= high; i++) {
		square_sum = square_sum + i;
		sum_squares = sum_squares + i*i;
	}
	square_sum = square_sum * square_sum;
	return square_sum - sum_squares;
}

bool is_prime(unsigned long int num) {
	for (int i = 2; i <= num/2; i++) {
		if (num % i == 0) {
			return false;
		}
	}
	return true;
}

unsigned long int nth_prime(unsigned int num) {
	unsigned long int i = 1;
	while (num > 0) {
		i++;
		if (is_prime(i)) {
			num = num - 1;
		}
	}
	return i;
}

unsigned long int largest_product_in_a_series(unsigned int n) {
	std::string series = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450";
	unsigned long int product = 0;
	for (unsigned int i = 0; i < (series.length() - n); i++) {
		unsigned long int current = 1;
		for (unsigned int j = 0; j < n; j++) {
			int integer = series[i+j] - '0';
			current = current * integer;
		}
		if (current >= product) {
		product = current;
		}
	}
	return product;
}

unsigned int special_pythagorean_triplet() {
	int thousand = 1000;
	int a = 1;
	int b = 1;
	int c = 1;
	int c_squared = c*c;
	while (thousand == thousand) {
		c_squared = c*c;
		if (a + b + c == thousand && a*a + b*b == c_squared) {
			std::cout << a << "\n" << b << "\n" << c << "\n";
			return a*b*c;
		} else if (a < b) {
			a = a + 1;
		} else if (a == b && b < c) {
			a = 1;
			b = b + 1;
		} else if (b == c) {
			a = 1;
			b = 1;
			c = c + 1;
		} else {
			std::cout << "Error" << "\n";
			return 1;
		}
	}
}

unsigned long int summation_of_primes(unsigned long int limit) {
	unsigned long int sum = 0;
	unsigned long int i = 2;
	while (i < limit) {
		if (is_prime(i)) {
			sum = sum + i;
		}
		i = i + 1;
		std::cout << i << "\n";
	}
	return sum;
}

int main() {
		std::cout << summation_of_primes(2000000);
}
