import sys
import os

# Input file mat.csv :

# a,b,c,d
# e,f,g,h
# i,j,k,l

def MAP(key, value):
    value = value.rstrip()      # Remove spaces and returns
    elems = value.split(',')    # Creates list from string (',' delimiter)    
    
    lst = []
    for i, tup in enumerate(elems):
        # index of the element is the row, key provided is the line
        # the new key becomes [line, row]
        lst.append([[key, i], tup]) 

    return lst

def REDUCE(key, value):
    # We invert coordinates
    return [[key[1], key[0]], value]


with open('mat.csv') as f:
    # List equivalent to the context of map 
    mapped = []
    
    for index, line in enumerate(f):
        mapped.extend(MAP(index, line))
        
    print "Map : "
    print mapped
    
    # Output :
    
    # Map :
    # [[[0, 0], 'a'], [[0, 1], 'b'], [[0, 2], 'c'], [[0, 3], 'd'], [[1, 0], 'e'], [[1, 1], 'f'], [[1, 2], 'g'], [[1, 3], 'h'], [[2, 0], 'i'], [[2, 1], 'j'], [[2, 2], 'k'], [[2, 3], 'l']]

    
    # Since our keys after mapping are coordinates, their are unique, so we can directly feed it to 
    # the reducer as if we had done a shuffle and sort before that. 

    # List equivalent to the context of reduce
    reduced=[]
    for elem in mapped:
        reduced.append(REDUCE(elem[0], elem[1]))

    print "Reduce : " 
    print reduced

    # Output :
    
    # Reduce : 
    # Reduce : [[[0, 0], 'a'], [[1, 0], 'b'], [[2, 0], 'c'], [[3, 0], 'd'], [[0, 1], 'e'], [[1, 1], 'f'], [[2, 1], 'g'], [[3, 1], 'h'], [[0, 2], 'i'], [[1, 2], 'j'], [[2, 2], 'k'], [[3, 2], 'l']]

