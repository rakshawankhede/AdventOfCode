#/usr/bin/python

import os

xd = {'>':1, '<' : -1}
yd = {'^': 1, 'v': -1}

def get_house_cnt_with_santa(file_path):

    '''
    This function will count number of houses that will receive at least one present.
    directions for Santa: '^' = Go North
                          'v' = Go South
                          '>' = Go East
                          '<' = Go West

    Input: file containing puzzle input
    Returns: Count for no of houses that will get atleast one present from Santa.

    '''
 
    # List containing house position 
    house_positions = [(0,0)]
    x = 0
    y = 0
    with open(file_path) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            else:
                x += xd.get(c, 0)
                y += yd.get(c, 0)
                house_positions.append((x,y))
    print "\nWhen only Santa was delivering presents..."
    print "Number of houses that will get atleast one present: ",len(set(house_positions))


def get_house_cnt_with_santa_and_robo(file_path):
    '''
    This function will count number of houses that will receive at least one present.
    directions for Santa and Robo: '^' = Go North
                                   'v' = Go South
                                   '>' = Go East
                                   '<' = Go West

    Input: file containing puzzle input
    Returns: Count for no of houses that will get atleast one present from Santa and Robo.

    '''

    # List containing house position
    house_positions = [(0,0)]
    xs = xb = 0
    ys = yb = 0
    flag = 0
    with open(file_path) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            if flag == 0:
                xs += xd.get(c, 0)
                ys += yd.get(c, 0)
                house_positions.append((xs,ys))
                flag = 1
            else:
                xb += xd.get(c, 0)
                yb += yd.get(c, 0)
                house_positions.append((xb,yb))
                flag = 0
    print "\nWhen Santa and Robot were delivering presents..."
    print "Number of houses that will get atleast one present: ",len(set(house_positions)) 

def get_input_file_path():
    '''
    This function will return path of input file for puzzle.
    '''
    source_dir = os.path.dirname(__file__)
    input_filename = os.path.basename(__file__).replace('.py', '.txt')
    return os.path.abspath(os.path.join(source_dir, 'puzzle_inputs', input_filename))

if __name__ == '__main__':
    file_path = get_input_file_path()
    get_house_cnt_with_santa(file_path)
    get_house_cnt_with_santa_and_robo(file_path)
