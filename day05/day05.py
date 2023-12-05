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
    for result in pt1results:
        print(result)   
    print (min(pt1results))

    print ("PART 2 RESULTS:")
    #for result in pt2results:
    #    print(result)   
    print (min(pt2results)) 
    
    print(f"Part 1 Time: {str(middle-start)}")
    print(f"Part 2 Time: {str(end-middle)}")
    print(f"Total Time: {str(end-start)}")

class Map:
    def __init__(self, destination, source, maprange):
        self.source_begin = source
        self.destination_begin = destination
        self.source_end = source + maprange - 1
        self.destination_end = destination + maprange - 1
        self.maprange = maprange

    def __str__(self):
        return f"{self.source_begin}-{self.source_end} {self.destination_begin}-{self.destination_end}  {self.maprange}"
    def __lt__(self, other):
        return self.destination_begin < other.destination_begin
    
    def findMap(self, source_input):
        if self.source_begin <= source_input <= self.source_end:
            delta = source_input - self.source_begin
            return self.destination_begin + delta
        else:
            return -1
        
    def findBackMap(self, destination_input):
        if self.destination_begin <= destination_input <= self.destination_end:
            delta = destination_input - self.destination_begin
            return self.source_begin + delta
        else:
            return -1
    
    
def part1(filename):     
    results = []
    seeds = [] 
    maps = []

    lines = read_file(filename) #modified to have extra newline at the end

    seeds = [int(i) for i in lines[0].split(':')[1].split(' ') if i ]
    map = []
    for count, line in enumerate(lines[1:]):
        if line == "":
            maps.append(map)
            map = []
            continue
        if line[0].isalpha():
            continue
        splitline = line.split(' ')
        map_obj = Map(int(splitline[0]), int(splitline[1]), int(splitline[2]))
        map.append(map_obj)
      
    seed_soil_maps = maps[1]
    soil_fertilizer_maps = maps[2]
    fertilizer_water_maps = maps[3]    
    water_light_maps = maps[4]
    light_temperature_maps = maps[5]
    temperature_humidity_maps = maps[6]
    humidity_location_maps = maps[7]

    for seed in seeds: 
        soil = -1
        for map in seed_soil_maps:            
            soil = map.findMap(seed)
            if soil != -1:
                break
        if soil == -1:
            soil = seed
        
        fertilizer = -1
        for map in soil_fertilizer_maps:
            fertilizer = map.findMap(soil)
            if fertilizer != -1:
                break
        if fertilizer == -1:
            fertilizer = soil
    
        water = -1
        for map in fertilizer_water_maps:
            water = map.findMap(fertilizer)
            if water != -1:
                break
        if water == -1:
            water = fertilizer

        light = -1
        for map in water_light_maps:
            light = map.findMap(water)
            if light != -1:
                break
        if light == -1:
            light = water
        
        temperature = -1
        for map in light_temperature_maps:
            temperature = map.findMap(light)
            if temperature != -1:
                break
        if temperature == -1:
            temperature = light
            
        humidity = -1
        for map in temperature_humidity_maps:
            humidity = map.findMap(temperature)
            if humidity != -1:
                break
        if humidity == -1:
            humidity = temperature
            
        location = -1
        for map in humidity_location_maps:
            location = map.findMap(humidity)
            if location != -1:
                break
        if location == -1:
            location = humidity    
        
        result = (seed, soil, fertilizer, water, light, temperature, humidity, location)
        #print(result)

        results.append(location)

    return results

def part2(filename):
    results = []

    lines = read_file(filename)
    for count, line in enumerate(lines):
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