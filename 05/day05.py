import numpy as np

"""Day 05"""
def count_vents(world):
    """counts the numbers greater than 1 and returns the solution"""
    danger = (world > 1).sum() # counts true values in boolean mask
    return danger

def draw_1(vents):
    """draws vent lines into array but only horizontally and vertically"""
    world = create_world(vents)
    for couple in vents:
        (x0, y0),(x1, y1) = couple
        if x0 == x1 or y0 == y1:
            # _s for sorted x0 and x1
            x0_s, x1_s = min(x0,x1), max(x0,x1)
            y0_s, y1_s = min(y0,y1), max(y0,y1)           
            world[y0_s:y1_s+1,x0_s:x1_s+1] +=1
    return world

def draw_2(vents):
    """draws vent lines horizontally, vertically and diagonally"""
    world = create_world(vents)
    for couple in vents:
        (x0, y0),(x1, y1) = couple
        # _s for sorted x0 and x1
        x0_s, x1_s = min(x0,x1), max(x0,x1)
        y0_s, y1_s = min(y0,y1), max(y0,y1) 
        if x0 == x1 or y0 == y1:
            #for horizontal and vertical lines
            world[y0_s:y1_s+1,x0_s:x1_s+1] +=1
        else:
            # y for diagonal lines
            steps = x1_s-x0_s+1
            # get direction of line for x and y
            if x1-x0 >= 0:
                x_dir = 1
            else:
                x_dir = -1
            if y1-y0 >= 0:
                y_dir = 1
            else:
                y_dir = -1
            for i in range(steps):
                world[y0+i*y_dir, x0+i*x_dir] += 1
    return world

def create_world(data):
    """creates np-array in shape of the max x and y values"""
    x_max = 0
    y_max = 0
    for couple in data:
        for value in couple:
            if value[0] >= x_max:
                x_max = value[0]
            if value[1] >= y_max:
                y_max = value[1]
    return np.zeros((x_max+1,y_max+1))

def main():
    # change path for testvalues
    path = '05\\input.txt'
    # path = '05\\testvalues.txt'

    # input vectors:
    vents = []
    with open(path, 'r') as inp_txt:
        for l in inp_txt:
            line = l.split(" -> ")
            l0 = tuple(map(int,line[0].split(","))) #x0,y0
            l1 = tuple(map(int,line[1].split(","))) #x1,y1
            vents.append((l0,l1))

    world1 = draw_1(vents)
    world2 = draw_2(vents)

    print(f"Part One: {count_vents(world1)}")
    print(f"Part Two: {count_vents(world2)}")


if __name__ == "__main__":
    main()