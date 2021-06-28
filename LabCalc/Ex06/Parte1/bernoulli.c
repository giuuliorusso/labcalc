#include <math.h>
#include <stdio.h>

long long int factorial(int n);
double binomialDist(int n, double p, int k);

int main(void) {
  FILE* fp;

  const double p = 1. / 6; // Probabilità
  int n;                   // Numero lanci

  do {
    printf("n: ");
    scanf("%d", &n);
  } while (n < 0);

  fp = fopen("bernoulli.dat", "w");

  for (int k = 0; k <= n; k++) {
    fprintf(fp, "%d %lf\n", k, binomialDist(n, p, k));
  }

  fclose(fp);
}

long long int factorial(const int n) {
  return n == 0 ? 1 : n * factorial(n - 1);
}

double binomialDist(const int n, const double p, const int k) {
  const long long int f1 = factorial(n) / (factorial(k) * factorial(n - k));
  const double f2 = pow(p, k);
  const double f3 = pow(1 - p, n - k);

  return (double)f1 * f2 * f3;
}
