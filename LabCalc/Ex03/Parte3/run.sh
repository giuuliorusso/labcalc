#!/usr/bin/env bash

clang zero2.c -Wall -Wextra -pedantic -o out/a.out

./out/a.out > ./out/zero2.dat

python3 plot.py
