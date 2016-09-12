import operator
import argparse


def load_data(filepath):
    with open(filepath, 'r') as file:
    	return file.read()


def get_most_frequent_words(text):
    freq_dict = dict()
    splitted_text = text.split(' ')
    for word in splitted_text:
    	if word == '' or word == '--':
    		continue
    	word = word.translate({ord(c): None for c in '\n[('})
    	if word not in freq_dict:
    		freq_dict[word] = 1
    	else:
    		freq_dict[word] += 1
    return freq_dict


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-p', '--path', help='Path to file')
	args = parser.parse_args()
	if not args:
		print('You didn\'t pass \'path\' arguments')
	text = load_data(args.path)
	a = get_most_frequent_words(text)
	sorted_dict = sorted(a.items(), key=operator.itemgetter(1))
	print(sorted_dict[-1:-10:-1])
