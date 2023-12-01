import sys
import time
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
    #   print(result)   
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
        ls = [l for l in line if l.isdigit()]
        #print(ls)
        results.append(str(ls[0])+str(ls[-1]))
        continue

    return [int(r) for r in results]

def part2(filename):
    results = []

    lines = read_file(filename)
    for count, line in enumerate(lines):
        line = re.sub("(one)", "on1e", line)
        line = re.sub("(two)", "t2wo", line)
        line = re.sub("(three)", "th3ree", line)
        line = re.sub("(four)", "fo4ur", line)
        line = re.sub("(five)", "fi5ve", line)
        line = re.sub("(six)", "si6x", line)
        line = re.sub("(seven)", "sev7en", line)
        line = re.sub("(eight)", "eig8ht", line)
        line = re.sub("(nine)", "ni9ne", line)
        
        ls = [l for l in line if l.isdigit()]
        #print(ls)
        results.append(str(ls[0])+str(ls[-1]))
        continue

    return [int(r) for r in results]

if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1: 
        if sys.argv[1] == "0":
            filename = "example_input.txt"
        else:
            filename = f"example_input{sys.argv[1]}.txt"
    #filename = 
    main(filename)