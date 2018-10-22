#/usr/bin/python

import os

def parse_input(input_str):
    input_str = input_str.split(' ')
    
    if input_str[0] == 'turn':
        action = input_str[1]
        x1 = (input_str[2]).split(',')[0]
        y1 = (input_str[2]).split(',')[1]
        x2 = (input_str[4]).split(',')[0]
        y2 = (input_str[4]).split(',')[1]
    elif input_str[0] == 'toggle':
        action = input_str[0]
        x1 = (input_str[1]).split(',')[0]
        y1 = (input_str[1]).split(',')[1]
        x2 = (input_str[3]).split(',')[0]
        y2 = (input_str[3]).split(',')[1]
    else:
        print "Invalid input"
        return(None, None, None, None, None)

    return(action, x1, y1, x2, y2)
          
        
def take_action(action, x1, y1, x2, y2, lights_grid):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if action == 'on':
                lights_grid[x][y] = 1
            elif action == 'off':
                lights_grid[x][y] = 0
            elif action == 'toggle':
                if lights_grid[x][y] == 1:
                    lights_grid[x][y] = 0
                else:
                    lights_grid[x][y] = 1
           
def brighten_lights(action, x1, y1, x2, y2, lights_grid):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if action == 'on':
                lights_grid[x][y] += 1
            elif action == 'off':
                if lights_grid[x][y] > 0:
                    lights_grid[x][y] -= 1
            elif action == 'toggle':
                    lights_grid[x][y] += 2

 
def get_count_of_lights_lit(string_list):
    '''
    This function will return count of lights lit after executing all the actions in input file.
    There can be three types of actions
    1. turn on : Turn on lights 
    2. turn off: Turn off lights
    3. toggle: if light is turned on, turned off and vice versa
    The input is in the form "turn off 0,0 through 2,2" which means walk from (0,0) to (2,2) 
    and turn off all the lights in grid (i.e. 9 lights).

    Params: Input - List of input strings
            Return - Count of light lit. 
   
    '''
    lights_lit = 0
    lights_grid = [[0 for x in range(1000)] for y in range(1000)] 
    for input_str in string_list:
        action, x1, y1, x2, y2 = parse_input(input_str)  
        if(action and x1 and y1 and x2 and y2):
            take_action(action, int(x1), int(y1), int(x2), int(y2), lights_grid)

    for x in range(1000):
        for y in range(1000):
                lights_lit += lights_grid[x][y]

    print "\nNumber of lights lit by traversing all inputs:", lights_lit 


def get_total_brightness(string_list):
    '''
    This function will return total brightness of lights after executing all the actions in input file.
    There can be three types of actions
    1. turn on : Increase brightness by 1
    2. turn off: decrease brightness by 1 (minimum to 0)
    3. toggle: Increase brightness by 2
    The input is in the form "turn off 0,0 through 2,2" which means walk from (0,0) to (2,2)
    and increase brightness of all lights by 1.

    Params: Input - List of input strings
            Return - Total brightness of lights.

    '''
    brightness = 0
    lights_grid = [[0 for x in range(1000)] for y in range(1000)]
    for input_str in string_list:
        action, x1, y1, x2, y2 = parse_input(input_str)
        if(action and x1 and y1 and x2 and y2):
            brighten_lights(action, int(x1), int(y1), int(x2), int(y2), lights_grid)

    for x in range(1000):
        for y in range(1000):
                brightness += lights_grid[x][y]

    print "Total brightness by traversing all inputs:", brightness

def get_input_file_path():
    '''
    This function will return path of input file for puzzle.
    '''
    source_dir = os.path.dirname(__file__)
    input_filename = os.path.basename(__file__).replace('.py', '.txt')
    return os.path.abspath(os.path.join(source_dir, 'puzzle_inputs', input_filename))

if __name__ == '__main__':
    file_path = get_input_file_path()
    with open(file_path) as f:
        string_list = [string for string in f]
    get_count_of_lights_lit(string_list)
    get_total_brightness(string_list)
