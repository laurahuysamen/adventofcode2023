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


def isSymbol(str):
    symbols = ["*","$","%","@","+","/","#","-","&","="]
    return str in symbols 

def getPartNumber(above, current, below, index):
    fullnumberIndexes = []
    for i in range(0,3): #all part numbers are shorter than 3 digits
        if index + i < len(current) and current[index+i].isdigit():
            fullnumberIndexes.append(index+i)
        else:
            break
    fullNumber = ""
    for j in fullnumberIndexes:
        fullNumber = fullNumber + current[j]
    #print(fullNumber)
    #we now have the full part-num. 

    
    for k in range(fullnumberIndexes[0]-1, fullnumberIndexes[-1]+2):
        if isSymbol(above[k]) or isSymbol(current[k]) or isSymbol(below[k]):   
            # it's a part number!         
            #print(above[fullnumberIndexes[0]-1:fullnumberIndexes[-1]+2])
            #print(current[fullnumberIndexes[0]-1:fullnumberIndexes[-1]+2])
            #print(below[fullnumberIndexes[0]-1:fullnumberIndexes[-1]+2])
            #print("----------")
            return (int(fullNumber), len(fullnumberIndexes))
    return (0, 1)

def isGearSymbol(str):
    symbols = ["*"]
    return str in symbols 

def getPartNumberAndGear(above, current, below, index):
    fullnumberIndexes = []
    for i in range(0,3): #all part numbers are shorter than 3 digits
        if index + i < len(current) and current[index+i].isdigit():
            fullnumberIndexes.append(index+i)
        else:
            break
    fullNumber = ""
    for j in fullnumberIndexes:
        fullNumber = fullNumber + current[j]
    #print(fullNumber)
    #we now have the full part-num. 
    
    for k in range(fullnumberIndexes[0]-1, fullnumberIndexes[-1]+2):
        if isGearSymbol(above[k]):
            return (int(fullNumber), len(fullnumberIndexes), (k, -1))
        elif isGearSymbol(current[k]):
            return (int(fullNumber), len(fullnumberIndexes), (k, 0))            
        elif isGearSymbol(below[k]):               
            return (int(fullNumber), len(fullnumberIndexes), (k, 1))
        
    return (0, 1, (0,0))
    
def part1(filename):     
    results = []

    lines = read_file(filename) 
    start = 0
    end = len(lines) - 1
    for count, line in enumerate(lines):
        if count == start or count == end: 
            continue # input has been modified to have a row of ... around the entire space :D 

        i = 0
        while i < len(line):
            if line[i].isdigit():
                (partnum, spaces) = getPartNumber(lines[count-1], line, lines[count+1], i)
                results.append(partnum)
                i = i + spaces
            else:
                i = i + 1

    return results

def part2(filename):
    results = []

    lines = read_file(filename) 
    start = 0
    end = len(lines) - 1
    interimResults = defaultdict(list)
    for count, line in enumerate(lines):
        if count == start or count == end: 
            continue # input has been modified to have a row of ... around the entire space :D 

        i = 0
        while i < len(line):
            if line[i].isdigit():
                (partnum, spaces, (gearx, geary)) = getPartNumberAndGear(lines[count-1], line, lines[count+1], i)
                gearstring = f"{gearx},{count+geary}"
                interimResults[gearstring].append(partnum)
                i = i + spaces
            else:
                i = i + 1

    for gear in interimResults.keys():
        items = interimResults[gear]
        if len(items) == 2:
            results.append(items[0]*items[1])

    return results

if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1: 
        if sys.argv[1] == "0":
            filename = "example_input.txt"
        else:
            filename = f"example_input{sys.argv[1]}.txt"
    #filename = 
    main(filename)