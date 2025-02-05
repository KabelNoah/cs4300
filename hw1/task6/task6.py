# task6.py

import os

def count_words_in_file(filename):
    """
    Reads a file and returns the number of words in it.
    
    :param filename: The name of the file to read.
    :return: The word count as an integer.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None

if __name__ == "__main__":
    file_name = "task6_read_me.txt"
    word_count = count_words_in_file(file_name)
    print(f"Word count in '{file_name}': {word_count}")
