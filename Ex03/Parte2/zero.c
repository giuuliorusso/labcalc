#include <math.h>
#include <stdio.h>

double f(const double x) { return x == 0 ? 1 : sin(x) / x; }

int main(void) {
  const double a = -20, b = 20; // Intervallo asse x

  const int n = 100; // Numero intervalli

  int c = 0;     // Contatore zeri
  double xl, xr, // Estremi intervallo k-esimo
      dx;

  dx = (b - a) / n;

  for (int k = 0; k < n; k++) {
    xl = a + k * dx;
    xr = xl + dx;

    if (f(xl) * f(xr) <= 0) {
      c++;
      printf("k = %d\txl = %f\txr = %f\n", k, xl, xr);
    }
  }

  printf("Numero zeri: %d", c);
}
