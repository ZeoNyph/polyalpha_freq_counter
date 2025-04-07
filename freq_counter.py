""" File: freq_counter.py
    Created by: Mithun Sivanesan (c3403606)
    Description: A Python program that takes in a text file and performs frequency analysis for a given period length. 
    To be used with ciphertexts from ciphers such as Beaufort's and Vigenere's ciphers.
    Dependencies: matplotlib; install via running 'pip install matplotlib'
"""

import sys
import os
from copy import deepcopy
import matplotlib.pyplot as plt

 # Initialize dictionaries
letter_count = { #created for convenience; copied in count
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0
}
count = {}

def main():
    """
    Frequency analysis to be used with polyalphabetic frequency analysis
    """
    # Check if the correct number of arguments is provided
    if len(sys.argv) <= 3:
        print("Usage: python freq_counter.py <filename> <length> <args>")
        print ("-p : print to console")
        print ("-g : generate graph")
        sys.exit(1)

    if not sys.argv[2].isdigit():
        print('Length is not a number')
    else:
        for i in range(1,int(sys.argv[2])+1):
            count.update({str(i): deepcopy(letter_count)})

    parse_file(sys.argv[1])

    for i in range(3, len(sys.argv)):
        if sys.argv[i] == "-p":
            print_console()
        elif sys.argv[i] == "-g":
            save_graph()
        else:
            print(f"Error: Unknown argument '{sys.argv[i]}'.")
            sys.exit(1)

def parse_file(filename: str):
    """Parses the given file and measures the frequency of the letters at a given index"""
# Check if the file exists
    if not os.path.isfile(filename):
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)    
    #read file
    with open(filename, encoding="utf-8") as file:
        content = file.read().strip().replace(' ', '').replace('\n','')
    for i in range(0,len(content)):
        count[str((i % int(sys.argv[2]))+1)][content[i]] += 1

def print_console():
    """Output the frequency to console as text"""
# print out count
    for position, letters in count.items():
        print(f"Frequency of letters in {position}")
        for letter, value in letters.items():
            print(f"{letter}: {value}")

def save_graph():
    """Outputs the frequency into charts, then saves them as .png files"""
    positions = list(count.keys())
    letters = list(letter_count.keys())

    # Create a bar chart for each position
    for position in positions:
        print(f"Generating graph for position {position}")
        frequencies = [count[position][letter] for letter in letters]
        plt.figure(figsize=(10, 6))
        plt.bar(letters, frequencies, color='skyblue')
        plt.title(f"Letter Frequency for Position {position}")
        plt.xlabel("Letters")
        plt.ylabel("Frequency")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.savefig(f"letter_frequency_position_{position}.png")

if __name__ == "__main__":
    main()