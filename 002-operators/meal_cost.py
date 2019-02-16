#!/bin/python3


# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent / 100)
    tax = meal_cost * (tax_percent / 100)
    return meal_cost + tax + tip

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    total_cost = solve(meal_cost, tip_percent, tax_percent)
    print(round(total_cost))
