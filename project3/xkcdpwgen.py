#!/usr/bin/env python3

import argparse
import random
import string

def generate_password(w, c, n, s):
    with open('words.txt', 'r') as f:
        words = [line.strip() for line in f]
    password_words = random.sample(words, w)
    
    if c:
        password_words = [word.capitalize() if random.choice([True, False]) else word for word in password_words]
    if n:
        for i in range(len(password_words)-1):
            if random.choice([True, False]):
                password_words.insert(i*2+1, str(random.randint(0, 9)))
    if s:
        symbols = string.punctuation
        for i in range(len(password_words)-1):
            if random.choice([True, False]):
                password_words.insert(i*2+1, random.choice(symbols))
    return "".join(password_words)


def main():


    parser = argparse.ArgumentParser(description='Generate an XKCD-style password.')
    parser.add_argument('-w', type=int, default=4)
    parser.add_argument('-c', action='store_true')
    parser.add_argument('-n', action='store_true')
    parser.add_argument('-s', action='store_true')

    args = parser.parse_args()

    print(generate_password(args.w, args.c, args.n, args.s))

main()
