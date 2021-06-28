#include <math.h>
#include <stdio.h>

int main(void) {
  const int n = 50; // Numero punti

  const double R = 6.2, // Raggio (m)
      omega = 0.1;      // Velocità angolare (rad/s)

  double t, // Tempo
      x, y, // x(t), y(t)
      dx;

  printf("t x(t) y(t)\n");

  // sin(2 * PI) = 0
  // => 2 * PI = omega * t
  // => t = (2 * PI) / omega

  dx = ((2 * M_PI) / omega) / n;

  for (int i = 0; i <= n; i++) {
    t = i * dx;
    x = R * cos(omega * t);
    y = R * sin(omega * t);
    printf("%+f %+f %+f\n", t, x, y);
  }
}
