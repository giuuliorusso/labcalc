#!/usr/bin/env bash

clang circle.c -Wall -Wextra -pedantic -o out/a.out

./out/a.out > ./out/traiettoria.dat

python3 plot.py
