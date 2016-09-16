from collections import Counter

import operator
import argparse


MOST_COMMON_NUMBER = 5


def load_data(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def get_most_frequent_words(text):
    splitted_text = text.split(' ')
    c = Counter()
    for word in splitted_text:
        if word == '' or word == '--':
            continue
        word = word.translate(
            {ord(c): None for c in '!@#$%^&*()[]{};:,./<>?\|`~-=_+\n'}
        )
        c[word.lower()] += 1
    return c


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='Path to file', required=True)
    args = parser.parse_args()
    if not args:
        print('You didn\'t pass \'path\' arguments')
    text = load_data(args.path)
    a = get_most_frequent_words(text)
    print(a.most_common(MOST_COMMON_NUMBER))
