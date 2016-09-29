from collections import Counter

import operator
import argparse
import re


TOP_SIZE = 5


def load_data(filepath):
    with open(filepath, 'r') as txt_file:
        return txt_file.read()


def get_most_frequent_words(text):
    pattern = re.compile('[^\W\d_]+')
    parsed_text = pattern.findall(text)
    counter = Counter(parsed_text)
    return counter.most_common(TOP_SIZE)


def print_result(input_data):
    for item in input_data:
        print('Слово: "{}"'.format(item[0]), 'Кол-во употреблений:', item[1])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='Path to file', required=True)
    args = parser.parse_args()
    text = load_data(args.path)
    result = get_most_frequent_words(text)
    print_result(result)
