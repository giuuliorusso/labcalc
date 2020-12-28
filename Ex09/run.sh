#!/usr/bin/env bash

clang hitmiss.c -Wall -Wextra -pedantic

echo "100000" | ./a.out

python3 ellisse.py
