#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 12

void parte1();
void parte2();

int getIndex(const double vec[], double x);

double epsilon(const int conf[]);
void printConf(int iconf, const int conf[], double epsilon);
void saveFreq(const char* filename, const double energie[], int size);
void spinconf(int conf[]);

int main(void) {
  srand(time(NULL));

  parte1();
  parte2();
}

// Distribuzione esatta delle energie.
void parte1() {
  int conf[N], iconf = 0;

  double energie1[(int)pow(2, N)];

  // TODO
  // Genera tutte le configurazioni possibili
  int i[N];
  for (i[0] = 1; i[0] <= 2; i[0]++) {
    for (i[1] = 1; i[1] <= 2; i[1]++) {
      for (i[2] = 1; i[2] <= 2; i[2]++) {
        for (i[3] = 1; i[3] <= 2; i[3]++) {
          for (i[4] = 1; i[4] <= 2; i[4]++) {
            for (i[5] = 1; i[5] <= 2; i[5]++) {
              for (i[6] = 1; i[6] <= 2; i[6]++) {
                for (i[7] = 1; i[7] <= 2; i[7]++) {
                  for (i[8] = 1; i[8] <= 2; i[8]++) {
                    for (i[9] = 1; i[9] <= 2; i[9]++) {
                      for (i[10] = 1; i[10] <= 2; i[10]++) {
                        for (i[11] = 1; i[11] <= 2; i[11]++) {
                          iconf++;

                          for (int j = 0; j < N; j++) {
                            conf[j] = (int)pow(-1, i[j]);
                          }

                          const double e = epsilon(conf);
                          energie1[iconf - 1] = e;

                          if (iconf <= 10)
                            printConf(iconf, conf, e);
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }

  saveFreq("histo1.dat", energie1, (int)pow(2, N));
}

// Campione statistico della distribuzione delle energie.
void parte2() {
  const int min = (int)1e3, max = (int)1e4;
  int M;

  double energie2[max];

  do {
    printf("M: ");
    scanf("%d", &M);
  } while (M < min || M > max);

  printf("\n");

  for (int i = 0; i < M; i++) {
    int conf[N];
    spinconf(conf);

    const double e = epsilon(conf);
    energie2[i] = e;

    if (i < 10)
      printConf(i + 1, conf, e);
  }

  saveFreq("histo2.dat", energie2, M);
}

// -

// Cerca l'elemento nel vettore e ritorna l'indice della prima occorrenza.
// Ritorna -1 se l'elemento non è presente.
int getIndex(const double vec[], const double x) {
  for (int i = 0; i < N; i++) {
    if (vec[i] == x)
      return i;
  }

  return -1;
}

// Calcola l'energia della configurazione.
double epsilon(const int conf[]) {
  double x = 0;

  for (int i = 0; i < N; i++) {
    x += conf[i] * conf[(i + 1) % N];
  }

  return -(1. / N) * x;
}

// Stampa la configurazione e la relativa energia.
void printConf(const int iconf, const int conf[], const double epsilon) {
  printf("Configurazione n. %2d ", iconf);

  for (int j = 0; j < N; j++) {
    printf("|%+d", conf[j]);
  }

  printf("| Eps = %+f\n", epsilon);
}

// Salva la frequenza delle energie su un file.
void saveFreq(const char* filename, const double energie[], const int size) {
  FILE* fp;

  int n = 0; // Numero valori energie
  double valoriEnergie[N];
  double contatoriEnergie[N] = {0};

  for (int i = 0; i < size; i++) {
    const double e = energie[i];

    int j = getIndex(valoriEnergie, e);

    // Il valore 'e' non è mai stato incontrato
    if (j == -1) {
      valoriEnergie[n] = e;
      contatoriEnergie[n]++;
      n++;
    }
    // Il valore 'e' è stato incontrato almeno una volta
    else {
      contatoriEnergie[j]++;
    }
  }

  fp = fopen(filename, "w");

  for (int i = 0; i < n; i++) {
    fprintf(fp, "%+f\t%f\n", valoriEnergie[i], contatoriEnergie[i] / size);
  }

  fclose(fp);
}

// Genera una configurazione casuale.
void spinconf(int conf[]) {
  for (int i = 0; i < N; i++) {
    const int n = rand() % 2 + 1;
    conf[i] = (int)pow(-1, n);
  }
}
