#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
  srand(time(NULL));

  const int n = rand() % 36 + 1;

  printf("%d ", n);

  if (n % 2 == 0)
    printf("E "); // Even
  else
    printf("O "); // Odd

  if (n <= 18)
    printf("M\n"); // Manque
  else
    printf("P\n"); // Passe
}
