#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <errno.h>

// Task: Find the two entries that sum to 2020
// and then multiply those two numbers together.

const int64_t target = 2020;
const int64_t max_elems = 200;     // wc -l input => 200

static inline int cmp(const void * a, const void * b) {
    return *(int64_t *)a - *(int64_t *)b;
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
    qsort(elems, sizeof(elems) / sizeof(elems[0]), sizeof(elems[0]), &cmp);

    // two pointers approach (start, end)
    int64_t *start = elems;
    int64_t *end = &elems[max_elems - 1];
    int64_t sum = 0;
    int found = 0;

    while( start < end ) {

        sum = *start + *end;
        if ( target < sum ) {
            end -= 1;
        }
        else if ( target > sum ) {
            start += 1;
        }
        else {
            found = 1;
            break;
        }
        
    }

    if ( found ) {
        printf("%ld + %ld = %ld\n", *start, *end, sum);
        printf("%ld * %ld = %ld\n", *start, *end, ((*start) * (*end)));
    }

    return 0;    
}