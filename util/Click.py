def get_center(locXY, x_add, y_add):
    x1 = locXY[0]
    y1 = locXY[1]
    x2 = locXY[2]
    y2 = locXY[3]
    return x1 + (x2 - x1) / 2+x_add, y1 + (y2 - y1) / 2+y_add
