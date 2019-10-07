from __future__ import unicode_literals, print_function, division
from io import open
from glob import glob
import os 

def find_files(path):
    return glob(path)

print(find_files(os.path.join('data', 'names', '*.txt')))

import unicodedata
import string 

all_letters = string.ascii_letters + "'.,;'"
n_letters = len(all_letters)

def unicode_to_ascii(s):
    result = ''.join(c for c in unicodedata.normalize('NFD', s)
                if unicodedata.category(c) != 'Mn'
                and c in all_letters)
    return result

print(unicode_to_ascii('afwe#ae£3d.'))

# Build the category_lines dictionary, a list of names per language
category_lines = {}
all_categories = []

def read_lines(filename):
    """
    Reads a file and splits into lines
    """
    lines = open(filename, encoding='utf-8').read().strip().split('\n')
    result = [unicode_to_ascii(line) for line in lines]
    return result 

# test_file = read_lines(find_files(os.path.join('data', 'names', 'english.txt'))[0])
# print(test_file)

for file_name in find_files('data/names/*.txt'):
    category = os.path.splitext(os.path.basename(file_name))[0]
    all_categories.append(category)
    lines = read_lines(file_name)
    category_lines[category] = lines

n_categories = len(all_categories)

print(category_lines['Italian'][:5])

import torch 

def letter_to_index(letter):
    '''
    Find letter index from all_letters (e.g. 'a'=0) 
    '''
    return all_letters.find(letter)

def letter_to_tensor(letter):
    '''
    Just for demonstration, turn a letter into a <1 x n_letters> tensor
    '''
    tensor = torch.zeros(1, n_letters)
    tensor[0][letter_to_index(letter)] = 1
    return tensor

def line_to_tensor(line):
    tensor = torch.zeros(len(line), 1, n_letters)
    for li, letter in enumerate(line):
        tensor[li][0][letter_to_index(letter)] = 1
    return tensor 

print(letter_to_tensor('a'))
print(line_to_tensor('jbkad').size())