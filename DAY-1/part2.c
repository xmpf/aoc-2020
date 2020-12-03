#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <stddef.h>
#include <errno.h>
#include <assert.h>

// Task: Find the two entries that sum to 2020
// and then multiply those two numbers together.

const int64_t target = 2020;
const int64_t max_elems = 200;     // wc -l input => 200

static inline int cmp(const void * a, const void * b) {
    return *(int64_t *)a >= *(int64_t *)b;
}

int main(int argc, char *argv[])
{
    errno = 0;
    FILE *fin = fopen("input", "r");
    if ( NULL == fin ) {
        fprintf(stderr, "Error occured while opening file: %m\n");
        exit(EXIT_FAILURE);
    }

    int64_t elems[max_elems];
    int64_t ix = 0;

    int ret = 0;

    errno = 0;
    while ( max_elems > ix && (ret = fscanf(fin, "%ld", &elems[ix])) != EOF ) {

        if ( 1 != ret ) {
            fprintf(stderr, "Error occured while reading from file: %m\n");
            fclose(fin);
            exit(EXIT_FAILURE);
        }

        ix += 1;
        errno = 0;
    }

    errno = 0;
    if ( 0 != fclose(fin) ) {
        fprintf(stderr, "Error occured: %m\n");
        exit(EXIT_FAILURE);
    }

    // sort elements
    qsort(elems, max_elems, sizeof(int64_t), &cmp);

    // two pointers approach (start, end)
    int start = 0;
    int end = max_elems - 1;
    int64_t sum = 0;
    int64_t diff = 0;
    int found = 0;
    
    while ( end > start ) {

        sum = elems[start] + elems[end];
        diff = target - sum;
        
       
        if ( diff <= elems[start]  ) {  // diff is not in range [start + 1, end - 1]
            end -= 1;
            continue;
        }
        else if ( diff >= elems[end] ) { // diff is not in range [start + 1, end - 1]
            start += 1;
            continue;
        }

        for (int ix = start + 1; ix < end; ix++) {  // diff is in range [start + 1, end - 1]
            if ( elems[ix] == diff ) { // check if it is also a member of the array
                goto L_FOUND;
            }
        }
        start += 1;
    }

    return 1;

L_FOUND:
    printf("%ld %ld %ld\n", elems[start], elems[end], diff);
    printf("%ld\n", elems[start] * elems[end] * diff);

    return 0;    
}