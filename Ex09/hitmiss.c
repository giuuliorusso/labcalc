#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int inserimento();
double genera_coordinata(int a, int b);
bool check(double x, double y);

int main(void) {
  srand(time(NULL));

  FILE* fp;

  const int a = -2, b = 2; // Intervallo
  const int l = 4;         // Lato quadrato
  const int Aq = l * l;    // Area quadrato

  const int Np = inserimento();
  int Nh = 0;

  fp = fopen("ellisse.dat", "w");

  for (int i = 0; i < Np; i++) {
    const double x = genera_coordinata(a, b);
    const double y = genera_coordinata(a, b);

    if (check(x, y)) {
      Nh++;
      fprintf(fp, "%+f %+f\n", x, y);
    }
  }

  fclose(fp);

  printf("Np: %d\n", Np);
  printf("Nh: %d\n", Nh);
  printf("Area stimata: %f\n", (double)Aq * Nh / Np);
  printf("Area esatta: %f\n", 4 * asin(4. / 5));
}

// Chiede l'inserimento di un numero intero compreso tra [1000, 10^5].
int inserimento() {
  int n;

  do {
    printf("Np: ");
    scanf("%d", &n);
  } while (n < 1000 || n > 1e5);

  printf("\n");

  return n;
}

// Genera un numero razionale casuale compreso tra [a, b].
double genera_coordinata(const int a, const int b) {
  return a + (b - a) * (double)rand() / RAND_MAX;
}

// Controlla se il punto (x, y) risiede nell'intersezione delle 2 ellissi.
bool check(const double x, const double y) {
  const bool e1 = pow(x, 2) / 4 + pow(y, 2) <= 1; // Ellisse 1
  const bool e2 = pow(x, 2) + pow(y, 2) / 4 <= 1; // Ellisse 2

  return e1 && e2;
}
