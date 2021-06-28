#!/usr/bin/env bash

clang simuladadi.c -Wall -Wextra -pedantic -o out/a.out

echo "12 50" | ./out/a.out
mv istogramma.dat out/istogramma_50.dat

echo "12 100000" | ./out/a.out
mv istogramma.dat out/istogramma_100k.dat

python3 plot.py
