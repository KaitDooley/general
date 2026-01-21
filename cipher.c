#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main() {
	// open input file for reading
	FILE* fp = fopen("input.txt", "r");
    if (fp == NULL) {
		printf("Error opening file.\n");
        exit(EXIT_FAILURE);
    }

	char enc[BUFSIZ];
	char str[BUFSIZ];

	while (fgets(enc, sizeof(enc), fp) && fgets(str, sizeof(str), fp)) {
		int valid = 1;
		if (strlen(enc) != strlen(str)) { // valid strings must have the same length
			valid = 0;
		}

		int let_enc[26] = {0};
		int let_str[26] = {0}; // define maps
		if (valid) {
			for (int i = 0; i < strlen(enc); i++) { // count occurances of each letter
				let_enc[enc[i]-'A'] ++;
				let_str[str[i]-'A'] ++;
			}

			for (int i = 0; i < 26; i++) { // check each string has equal frequencies
				if (let_enc[i] == 0) continue;
				int found = 0;
				for (int j = 0; j < 26; j++) {
					if (let_enc[i] == let_str[j]) {
						found = 1;
						let_str[j] = 0;
						break;
					}
				}
				if (found == 0) {
					valid = 0;;
					break;
				}
			}
		}

		if (valid) {
			printf("YES\n");
		} else { 
			printf("NO\n");
		}
	}

	fclose(fp);
	return 0;	
}
