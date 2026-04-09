#include <stdio.h>

int main() {

	int n = 0; 
    printf("Enter the number of rows: ");
    scanf("%d", &n);
    if (n <= 0 || n > 20) {
		printf("Invalid number of rows. Valid values 1 to 20\n");
		return 1;
	}

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < (n - i - 1) * 3; j++)
            printf(" ");

        int val = 1;
        for (int k = 0; k <= i; k++) {
            printf("%6d", val);
          
            val = val * (i - k) / (k + 1);  
        }
        printf("\n");
    }

    return 0;
}
