#!/usr/bin/python

import os

def get_input_file_path():
    '''
    This function will return path of input file for puzzle.
    '''
    source_dir = os.path.dirname(__file__)
    input_filename = os.path.basename(__file__).replace('.py', '.txt')
    return os.path.abspath(os.path.join(source_dir, 'puzzle_inputs', input_filename))

def get_nice_string_count(string_list):

    '''
    This function will return count for nice strings in input file
    A string should satisfy following conditions to be nice string:
    1. It should contains at least three vowels (aeiou only), like aei, xazegov, 
       or aeiouaeiouaeiou.
    2. It should contains at least one letter that appears twice in a row,
       like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    3. It should not contain the strings ab, cd, pq, or xy, 
       even if they are part of one of the other requirements.

    Param: Input- List of strings
           Output - Count for nice strings
    '''

    vowels = {'a':1, 'e': 1, 'i':1, 'o' : 1, 'u' : 1}
    nice_string = 0
    for input_str in string_list:
        vcount = 0
        con1 = con2 = False
        con3 = True

        for char in ['ab', 'cd', 'pq', 'xy']:
            if char in input_str:
                con3 = False
                break
        for i in range(len(input_str)):
            if (i < len(input_str)-1):
                if input_str[i] == input_str[i+1]:
                    con2 = True
            vcount += vowels.get(input_str[i], 0)
        if(vcount >= 3):
            con1 = True
        if(con1 and con2 and con3):
            nice_string += 1
            
    print "Nice string count::", nice_string


def get_nice_string_count_algo2(string_list):
 
    '''
    This function will return count for nice strings in input file
    A string should satisfy following conditions to be nice string:
    1. It should contains a pair of any two letters that appears at least twice in the string without overlapping, 
       like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    2. It should contains at least one letter which repeats with exactly one letter between them, 
       like xyx, abcdefeghi (efe), or even aaa.

    Param: Input- List of strings
           Output - Count for nice strings
    '''

    nice_string = 0
    match_str = None
    for input_str in string_list:
        con1 = con2 = False
        for i in range(len(input_str)):
            if(i < len(input_str)-4):
                match_str = input_str[i:i+2]
                if match_str in input_str[i+2:]:
                    con1 = True
                    break
        for i in range(len(input_str)):
            if(i< len(input_str)-3):
                if(input_str[i] == input_str[i+2]):
                    con2 = True
                    break

        if (con1 and con2):
           nice_string += 1
                    
    print "Nice string count::", nice_string
                               

if __name__ == '__main__':
    file_path = get_input_file_path()
    with open(file_path) as f:
        string_list = [string for string in f]
    get_nice_string_count(string_list)    
    get_nice_string_count_algo2(string_list)    
