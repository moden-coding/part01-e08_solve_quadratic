#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    determinant = float(b*b - 4*a*c)
    determinant = math.sqrt(determinant)
    answer_one = (-b + determinant)/(2*a)
    answer_two = (-b - determinant)/(2*a)


    return (answer_one,answer_two)


def main():
    print(solve_quadratic(1,-1,-5))

if __name__ == "__main__":
    main()
