#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int count_subsets(int n);

// Main Execution
int main() {
	int n = 0;
    while (scanf("%d", &n) == 1) {
		printf("%d\n", count_subsets(n));
	}
    return EXIT_SUCCESS;
}


// Functions
int count_subsets(int n) {
	int count = 0;
	
	for (int bitset = 0; bitset < (1<<10) ; bitset++) {
		int total = 0;
		for (int i = 0; i < 10; i++) {
			if (bitset & (1 << i)) total += i; 
		}

		if (total % n == 0) count++;	
	}

	return count;
}
