#!/usr/bin/env python3

def fibonacci_sequence(n):
    if n <= 0:
        return []

    sequence = [0, 1]
    if n == 1:
        return sequence[:1]

    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence
