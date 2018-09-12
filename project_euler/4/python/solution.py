#!/usr/bin/env python3.7


def is_number_palindrome(
    number: int
) -> bool:
    number = str(number)
    if number == number[::-1]:
        return True
    return False


def largest_palindromic_product_of_two_n_digit_multiplicands(
    n: int
) -> int:
    max_multiplicand = int('9' * n)

    largest_palindrome = 9
    x = max_multiplicand
    while len(str(x)) == n:
        y = max_multiplicand
        while len(str(y)) == n:
            product = x * y
            if product <= largest_palindrome:
                break
            if is_number_palindrome(product) and product > largest_palindrome:
                print(x, y, product)
                largest_palindrome = product
            y -= 1
        x -= 1

    return largest_palindrome


if __name__ == '__main__':
    print(
        largest_palindromic_product_of_two_n_digit_multiplicands(
            n=3
        )
    )
