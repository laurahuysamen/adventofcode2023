import sys
import time
import numpy as np
from collections import Counter, defaultdict
import itertools
from functools import reduce
import copy
import math
import uuid
import networkx as nx
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import re


def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [str(l.strip()) for l in lines]
    return lines

def main(filename):
    print("PART 1")
    start = time.time()
    pt1results = part1(filename)
    middle = time.time()
    print("PART 2")
    pt2results = part2(filename)
    end = time.time() 

    print ("PART 1 RESULTS:")
    #for result in pt1results:
    #    print(result)   
    print (sum(pt1results))

    print ("PART 2 RESULTS:")
    #for result in pt2results:
    #    print(result)   
    print (sum(pt2results)) 
    
    print(f"Part 1 Time: {str(middle-start)}")
    print(f"Part 2 Time: {str(end-middle)}")
    print(f"Total Time: {str(end-start)}")
    
    
def part1(filename):     
    results = []

    lines = read_file(filename)
    for count, line in enumerate(lines):
        splitline = line.split(':')[1].split('|')
        winning_numbers = [int(i) for i in splitline[0].split(' ') if i]
        scratchcard_numbers = [int(i) for i in splitline[1].split(' ') if i]
        cardvalue = 0
        for win_num in winning_numbers:
            if win_num in scratchcard_numbers:
                cardvalue = cardvalue + 1

        if cardvalue > 0:
            results.append(2**(cardvalue-1))

    return results

def part2(filename):
    results = []

    scratchcards = []
    countOfCards = []

    lines = read_file(filename)
    for count, line in enumerate(lines):

        splitline = line.split(':')[1].split('|')
        winning_numbers = [int(i) for i in splitline[0].split(' ') if i]
        scratchcard_numbers = [int(i) for i in splitline[1].split(' ') if i]
        cardvalue = 0
        for win_num in winning_numbers:
            if win_num in scratchcard_numbers:
                cardvalue = cardvalue + 1
        scratchcards.append(cardvalue)
        countOfCards.append(1)
    
    #print(scratchcards)
    #print(countOfCards)
        
    for count, card in enumerate(scratchcards):
        if card > 0:
            for i in range(1, card+1):
                countOfCards[count+i] = countOfCards[count+i] + countOfCards[count]*1
    #print (countOfCards)
    return countOfCards

if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1: 
        if sys.argv[1] == "0":
            filename = "example_input.txt"
        else:
            filename = f"example_input{sys.argv[1]}.txt"
    #filename = 
    main(filename)