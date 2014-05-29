#!/usr/bin/env python

import sys
import re
import random


def load_film_database(min_length=10):
    choices = set()

    for l in open('us-uk-films.txt'):
        mo = re.match(r'([A-Za-z]{3,}? [A-Za-z]{3,}?)\s+\(\d{4}\)\s*(US|UK)$', l)
        if mo:
            title = mo.group(1)
            if len(title) < min_length:
                continue
            if title in choices:
                continue
            choices.add(title)
    return choices


def generate_password(choices):
    selection = list(choices)
    num = random.randint(100, 999)

    film = random.choice(selection)
    passwd = film.replace(' ', str(num))

    choices.remove(film)
    return passwd

def main():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-l', '--min-length', type='int', help="Minimum length of film title", default=10)
    parser.add_option('-n', '--number', type='int', help="Number of passwords to generate", default=1)
    parser.add_option('-s', '--db-size', action="store_true", help="Print size of candidate database")

    options, args = parser.parse_args()

    db = load_film_database(options.min_length)
    if not db:
        parser.error("The minimum length is too long; no films match.")

    if options.db_size:
        print len(db)
        sys.exit(0)
    
    for i in range(options.number):
        print generate_password(db)

if __name__ == '__main__':
    main()

