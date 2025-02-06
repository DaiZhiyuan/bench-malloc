#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM_ALLOCATIONS 1000
#define MAX_ALLOC_SIZE 1024

int main(void) 
{
    void* allocations[NUM_ALLOCATIONS]; 
    srand(time(NULL)); 

    for (int i = 0; i < NUM_ALLOCATIONS; i++) {
        size_t size = rand() % MAX_ALLOC_SIZE + 1; 
        allocations[i] = malloc(size); 
        if (allocations[i] == NULL) {
            fprintf(stderr, "Memory alloc failed!\n");
            return 1;
        }
    }

    for (int i = 0; i < NUM_ALLOCATIONS; i++) {
        free(allocations[i]); 
    }

    printf("Memory alloc and free completed.\n");

    return 0;
}
