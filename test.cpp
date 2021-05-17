#include <stdio.h>

#define LAST(k,n) ((k) & ((1<<(n))-1))
#define MID(k,m,n) LAST((k)>>(m),((n)-(m)))

unsigned int get_first_n_bits(unsigned int x, int n) {
    int mask = ~0 << (32-n);
    return (x & (~0 << (32-n))) >> (32-n);
    return mask;
}

#define HASH_M 8

#define LAST_N_BITS(ADDR) \
  ADDR & ~(~0U << HASH_M)

#define FIRST_N_BITS(ADDR) \
  (ADDR & (~0U << (32-HASH_M))) >> (32-HASH_M)

int main()
{
    unsigned int a = 3019945117;
    int n = 5;
    printf("%d\n", a & ~(~0U << n));
    
    printf("%d\n",  MID(a,11,16));
    
    printf("%d\n",  get_first_n_bits(a, n));
    
    
    printf("%d %d\n",  FIRST_N_BITS(a), LAST_N_BITS(a));

    return 0;
}