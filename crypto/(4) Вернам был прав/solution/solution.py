#!/usr/bin/python3

key = "flag{ASCII_b3sT_1n_Th3_W0rLd3}"
cipher = [0, 0, 0, 0, 0, 23, 96, 49, 39, 120, 50, 61, 103, 64, 59, 45, 2, 26, 110, 63, 55, 96, 43, 37, 0, 28, 122, 40, 74, 0]
for i, g in zip(cipher, key):
 print(chr(i^ord(g)), end = "")
