#!/usr/bin/python

get_list = lambda input_str:[x for x in input_str.split('\n') if x!='']

def get_total_paper_and_ribbon_required(dimentions_list):

    '''
    This function will calculate total paper required to wrap boxes and total ribbon required.
    Paper rquired to wrap one box = surface area of box + area of the smallest side
    Ribbon required = smallest perimeter of any one face + volume of box (to tie a bow)
    param: dimention_list - List containing dimention for each box (length*width*height)
    return: 1. Total paper required to wrap boxes
            2. Total ribbon required
    '''

    total_area = 0
    total_ribbon_required = 0
    fail = 0
    for d in dimentions_list:
        try:
            l = int(d.split('x')[0])
            w = int(d.split('x')[1])
            h = int(d.split('x')[2])
        except Exception:
            print "Invalid input!"
            fail = 1
            break

        area = (2*l*w) + (2*w*h) + (2*l*h) + min(l*w, w*h, l*h)
        total_area = total_area + area
        ribbon_required_for_box = min((2*l+2*w), (2*w+2*h), (2*l+2*h)) + (l*w*h)
        total_ribbon_required += ribbon_required_for_box  
       
    if not fail: 
        print "Total Paper required:", total_area
        print "Total ribbon required:", total_ribbon_required


if __name__ == '__main__':
    fd = open("in2", "r")
    input_str = fd.read()
    dimentions_list = get_list(input_str)
    get_total_paper_and_ribbon_required(dimentions_list)
    fd.close()


