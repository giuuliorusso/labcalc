#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void placeBet(int* betAmount, int* betType, int* chips);
bool check(int winningNumber, int betType);

int main(void) {
  srand(time(NULL));

  int round = 1;
  const int maxRound = 10;

  int chips = 100;
  int betsSum = 0;

  int betAmount;
  int betType;
  // 1 = Even
  // 2 = Odd
  // 3 = Manque
  // 4 = Passe

  int winningNumber;

  while (round <= maxRound && chips > 0) {
    printf("ROUND %d\n", round++);
    printf("\tChips = %d\n", chips);

    placeBet(&betAmount, &betType, &chips);
    betsSum += betAmount;

    winningNumber = rand() % 36 + 1;
    printf("\n\tWinning number = %d\n\n", winningNumber);

    if (check(winningNumber, betType)) {
      printf("\tYOU WON!\n\n");
      chips += betAmount * 2;
    } else {
      printf("\tYOU LOST!\n\n");
    }
  }

  printf("-----\n");
  printf("Rounds = %d\n", round - 1);
  printf("Bets' sum = %d\n", betsSum);
  printf("Chips left = %d\n", chips);
}

void placeBet(int* const betAmount, int* const betType, int* const chips) {
  // Bet amount
  while (true) {
    printf("\n\tBet amount: ");
    scanf("%d", betAmount);

    if (*betAmount > *chips)
      printf("\n\tYou don't have enough chips. Try again.\n");
    else if (*betAmount <= 0)
      printf("\n\tEnter a valid number. Try again.\n");
    else
      break;
  }

  // Bet type
  while (true) {
    printf("\n\tBet on:\n");
    printf("\t1) Even\n");
    printf("\t2) Odd\n");
    printf("\t3) Manque\n");
    printf("\t4) Passe\n");

    printf("\t> ");
    scanf("%d", betType);

    if (*betType < 1 || *betType > 4)
      printf("\n\tEnter a valid number. Try again.\n");
    else
      break;
  }

  *chips -= *betAmount;
}

bool check(const int winningNumber, const int betType) {
  switch (betType) {
    case 1: return winningNumber % 2 == 0; // Even
    case 2: return winningNumber % 2 != 0; // Odd
    case 3: return winningNumber <= 18;    // Manque
    case 4: return winningNumber > 18;     // Passe
    default: return false;
  }
}
