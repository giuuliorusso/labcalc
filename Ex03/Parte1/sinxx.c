#include <math.h>
#include <stdio.h>

double f(const double x) { return x == 0 ? 1 : sin(x) / x; }

int main(void) {
  const double a = -20, b = 20; // Intervallo asse x

  int n; // Numero punti

  double x, y, dx;

  do {
    scanf("%d", &n);
  } while (n < 100);

  dx = (b - a) / n;

  for (int i = 0; i <= n; i++) {
    x = a + i * dx;
    y = f(x);
    printf("%+f %+f\n", x, y);
  }
}
