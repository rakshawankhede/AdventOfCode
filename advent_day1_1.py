#!/usr/bin/python

def deliver_present(filename):

    ''' This function will help santa to deliver present at correct floor.
    Opening brace ( indicates go one floor up and closing brace ) indicates go 1 floor down.
    :param: path for file containing input string.
    :return Floor number
    '''
    
    floor = 0
    with open(filename) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            if c == '(':
                floor +=1
            elif c == ')':
                floor -=1
            else:
                pass 
    print "Deliver present at Floor:", floor


if __name__ == '__main__':
    input_file = "in1"
    deliver_present(input_file)
