#!/usr/bin/env bash

clang sinxx.c -Wall -Wextra -pedantic -o out/a.out

echo "200" | ./out/a.out > ./out/sinxx.dat

python3 plot.py
