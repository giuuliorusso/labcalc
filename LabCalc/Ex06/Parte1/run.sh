#!/usr/bin/env bash

clang bernoulli.c -Wall -Wextra -pedantic -o out/a.out

ns=(2 4 8 12)

for n in "${ns[@]}"; do
  echo $n | ./out/a.out
  mv bernoulli.dat out/bernoulli_$n.dat
done

python3 plot.py
