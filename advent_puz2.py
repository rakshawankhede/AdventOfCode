#!/usr/bin/python

def find_1st_direction_for_basement(filename):
    
    ''' This function will find position of 1st input charecter which will lead Santa to basement.
    Opening brace ( indicates go one floor up and closing brace ) indicates go 1 floor down.
    :param: Path for file containing input string.
    :return: 
    '''

    pos = 0
    floor = 0
    with open(filename) as f:
        while True:
            c = f.read(1)
            pos +=1
            if not c:
                break
            if c == '(':
                floor +=1
            elif c == ')':
                floor -=1
            else:
                pass
            if floor == -1:
                print "First position for direction to reach basement is :{0}".format(pos)
                break


if __name__ == '__main__':
    input_file = "in1"
    find_1st_direction_for_basement(input_file)
