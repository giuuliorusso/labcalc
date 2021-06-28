#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_DADI 100

int dado() { return rand() % 6 + 1; }

int main(void) {
  srand(time(NULL));

  FILE* fp;

  int nDadi, nLanci;

  const int v = 3;           // Valore di cui contare le occorrenze
  int k = 0;                 // Contatore occorrenze v nel lancio di nDadi
  int c[MAX_DADI + 1] = {0}; // Contatori occorrenze k in nLanci

  // nDadi
  do {
    printf("n dadi: ");
    scanf("%d", &nDadi);
  } while (nDadi <= 0 || nDadi > MAX_DADI);

  // nLanci
  do {
    printf("n lanci: ");
    scanf("%d", &nLanci);
  } while (nLanci <= 0);

  for (int i = 0; i < nLanci; i++, k = 0) {
    for (int j = 0; j < nDadi; j++) {
      if (dado() == v)
        k++;
    }
    c[k]++;
  }

  fp = fopen("istogramma.dat", "w");

  for (int i = 0; i <= nDadi; i++) {
    fprintf(fp, "%d %f\n", i, (double)c[i] / nLanci);
  }

  fclose(fp);
}
