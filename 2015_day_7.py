#!/usr/bin/python

import os

circuit_dict = dict()

def get_input_file_path():
    '''
    This function will return path of input file for puzzle.
    '''
    source_dir = os.path.dirname(__file__)
    input_filename = os.path.basename(__file__).replace('.py', '.txt')
    return os.path.abspath(os.path.join(source_dir, 'puzzle_inputs', input_filename))

def num(s):
    try:
        return int(s)
    except ValueError:
        return -1

def parse_input(in_list):
    '''
    This function will convert instruction input list to a dictionary.
    Instruction can be of form : x AND y -> z
    For above example dictionary key will be 'z' and value will be 'x AND y'
    Params:
          Input: list containing instructions
          Output: Dictinary
    '''
    out_dict = {}
    for instr in in_list:
        in_arr = instr.split(' ')
        if(len(in_arr) == 5):
            out_dict[in_arr[-1]] = [in_arr[1],in_arr[0],in_arr[2]]
        if(len(in_arr) == 4):
            out_dict[in_arr[-1]] = [in_arr[0],in_arr[1]]
        if(len(in_arr) == 3):
            i = num(in_arr[0])
            if i != -1:
                out_dict[in_arr[-1]] = i
            else:
                out_dict[in_arr[-1]] = in_arr[0]
    return out_dict


def get_circuit_val(char_key):
    '''
    This function will calculate value of a circuit recursively.
    A signal is provided to each wire by a gate, another wire, or some specific value.
    Input file contains list of instructions to assemble circuit.
    Possible gates used in instructions are AND, OR, NOT and some bitwise operations like 
    RSHIFT and LSHIFT.

    Params:
          Input: char_key - char_key can be an expression, a wire name or an integer value
          Output: Value of key
    '''
   
    j = num(char_key)
    if j != -1:
        return j
    if(type(char_key) == int):
        return char_key
    if(type(circuit_dict[char_key]) == int):
        return circuit_dict[char_key]
    if(type(circuit_dict[char_key]) == str):
        x = get_circuit_val(circuit_dict[char_key])
        return x
    if(len(circuit_dict[char_key]) == 2):
        x = ~get_circuit_val(circuit_dict[char_key][1])
        circuit_dict[char_key] = x
        return x
    elif(len(circuit_dict[char_key]) == 3):
        if circuit_dict[char_key][0] == 'AND':
            x = get_circuit_val(circuit_dict[char_key][1])&get_circuit_val(circuit_dict[char_key][2])
            circuit_dict[char_key] = x
            return x
        if circuit_dict[char_key][0] == 'OR':
            x = get_circuit_val(circuit_dict[char_key][1])|get_circuit_val(circuit_dict[char_key][2])
            circuit_dict[char_key] = x
            return x
        if circuit_dict[char_key][0] == 'RSHIFT':
            x = get_circuit_val(circuit_dict[char_key][1])>>get_circuit_val(circuit_dict[char_key][2])
            circuit_dict[char_key] = x
            return x
        if circuit_dict[char_key][0] == 'LSHIFT':
            x = get_circuit_val(circuit_dict[char_key][1])<<get_circuit_val(circuit_dict[char_key][2])
            circuit_dict[char_key] = x
            return x
    
if __name__ == '__main__':
    file_path = get_input_file_path()
    with open(file_path) as f:
        string_list = [string.strip() for string in f]
   
    circuit_dict = parse_input(string_list)
    a_circuit_val = get_circuit_val('a')
    print("a = {}".format(a_circuit_val)) 
    new_b_circuit_val = a_circuit_val

    circuit_dict = parse_input(string_list)
    circuit_dict['b'] = new_b_circuit_val
    a_circuit_val = get_circuit_val('a')
    print("a = {}".format(a_circuit_val))

    
