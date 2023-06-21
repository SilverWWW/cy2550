#!/usr/bin/env python3

import argparse
import random
import string

def generate_password(num_words, capitalize, add_numbers, add_symbols):
    with open('words.txt', 'r') as f:
        words = [line.strip() for line in f]

    password_parts = random.sample(words, num_words)

    if capitalize:
        password_parts = [word.capitalize() if random.choice([True, False]) else word for word in password_parts]
    
    if add_numbers:
        for i in range(len(password_parts)-1):
            if random.choice([True, False]):
                password_parts.insert(i*2+1, str(random.randint(0, 9)))
    
    if add_symbols:
        symbols = string.punctuation
        for i in range(len(password_parts)-1):
            if random.choice([True, False]):
                password_parts.insert(i*2+1, random.choice(symbols))

    return "".join(password_parts)

def main():
    parser = argparse.ArgumentParser(description='Generate an XKCD-style password.')
    parser.add_argument('-w', type=int, default=4, help='Number of words in the password')
    parser.add_argument('-c', action='store_true', help='Capitalize the start of random words')
    parser.add_argument('-n', action='store_true', help='Insert numbers randomly between words')
    parser.add_argument('-s', action='store_true', help='Insert symbols randomly between words')

    args = parser.parse_args()

    print(generate_password(args.w, args.c, args.n, args.s))

if __name__ == "__main__":
    main()
