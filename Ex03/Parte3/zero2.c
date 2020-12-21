#include <math.h>
#include <stdio.h>

double f(const double x) { return x == 0 ? 1 : sin(x) / x; }

int zero(double (*f)(double), const double a, const double b, const int n) {
  int c = 0;     // Contatore zeri
  double xl, xr, // Estremi intervallo k-esimo
      dx;

  dx = (b - a) / n;

  for (int k = 0; k < n; k++) {
    xl = a + k * dx;
    xr = xl + dx;

    if (f(xl) * f(xr) <= 0) {
      c++;
    }
  }

  return c;
}

int main(void) {
  const int n1 = 1, n2 = 14; // Range intervalli

  const double a = -20, b = 20; // Intervallo asse x

  for (int i = n1; i <= n2; i++) {
    printf("%d %d\n", i, zero(f, a, b, i));
  }
}
