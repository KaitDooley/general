#include <stdio.h>
#include <stdlib.h>

int main() {
    printf("Compiler works!\n");
    
    int *ptr = (int *)malloc(sizeof(int));
    if (ptr == NULL) {
        fprintf(stderr, "Allocation failed\n");
        return 1;
    }
    
    *ptr = 42;
    printf("Value: %d\n", *ptr);
    
    free(ptr);
    return 0;
}
