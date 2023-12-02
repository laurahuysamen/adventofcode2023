import sys
import time

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
    for result in pt1results:
        print(result)   
    print (sum(pt1results))

    print ("PART 2 RESULTS:")
    for result in pt2results:
        print(result)   
    print (sum(pt2results)) 
    
    print(f"Part 1 Time: {str(middle-start)}")
    print(f"Part 2 Time: {str(end-middle)}")
    print(f"Total Time: {str(end-start)}")
    
    
def part1(filename):     
    results = []

    lines = read_file(filename)
    for count, line in enumerate(lines):
        game = line.split(":")

        maxr = 0
        maxg = 0
        maxb = 0
        rounds = game[1].split(";")
        for round in rounds: 
            moves = round.split(",")
            for cubes in moves:
                descriptor = cubes.strip().split(" ")
                print(descriptor)
                if descriptor[1] == "red":
                    numr = int(descriptor[0])
                    maxr = max(maxr, numr)
                if descriptor[1] == "green":
                    numg = int(descriptor[0])
                    maxg = max(maxg, numg)
                if descriptor[1] == "blue":
                    numb = int(descriptor[0])
                    maxb = max(maxb, numb)            

        thresholdr = 12
        thresholdg = 13
        thresholdb = 14
        if maxr <= thresholdr and maxg <= thresholdg and maxb <= thresholdb :
            results.append(int(game[0][5:]))
        continue

    return results

def part2(filename):
    results = []

    lines = read_file(filename)
    for count, line in enumerate(lines):
        game = line.split(":")

        maxr = 0
        maxg = 0
        maxb = 0
        rounds = game[1].split(";")
        for round in rounds: 
            moves = round.split(",")
            for cubes in moves:
                descriptor = cubes.strip().split(" ")
                print(descriptor)
                if descriptor[1] == "red":
                    numr = int(descriptor[0])
                    maxr = max(maxr, numr)
                if descriptor[1] == "green":
                    numg = int(descriptor[0])
                    maxg = max(maxg, numg)
                if descriptor[1] == "blue":
                    numb = int(descriptor[0])
                    maxb = max(maxb, numb)            

        
        results.append(maxr * maxg * maxb)
        continue

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