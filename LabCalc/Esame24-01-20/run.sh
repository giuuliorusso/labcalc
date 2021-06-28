#!/usr/bin/env bash

clang main.c -Wall -Wextra -pedantic

echo "10000" | ./a.out

python3 plot.py
