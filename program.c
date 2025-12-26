#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * Check each member in an array to determine if it's a palindrom.
 *
 * @param  str_arr      Array of strings to check
 * @param  count        Number of elements in str_arr
 * @return Number of palindromes in the array
 */
int determine_palindromes(char **str_arr, int count);
int check_palindromes(char *str);

int main(void)
{
    char* str_arr[] = { "bob", "bat", "racecar", "Rotor" };
    assert(determine_palindromes(str_arr, 4) == 3);

    puts("Tests Passed!");
    return 0;
}

/** DO NOT EDIT ABOVE THIS LINE **/

int determine_palindromes(char **str_arr, int count) {
	int palindromes = 0;
	for (int i = 0; i < count; i++) {
		if (check_palindromes(str_arr[i])) palindromes++;
	}
	printf("%d\n", palindromes);
	return palindromes;
}


int check_palindromes(char *str) {
	int i = 0;
	while(str[i] != '\0') {
		i++;
	}
	
	for (int j = 0; j < i/2; j++) {
		char a = str[j], b = str[i-j-1];
		if (a < 'a') a += 'a' - 'A';
		if (b < 'a') b += 'a' - 'A';
		
		if (a != b) return 0;
	}
	printf("%s\n", str);	
	
	return 1;
} 
