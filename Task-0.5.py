def area_of_triangle(side_1, side_2, side_3):
    sides = (side_1 + side_2 + side_3) / 2
    area = (sides*(sides-side_1)*(sides-side_2)*(sides-side_3)) ** 0.5
    return area


print(area_of_triangle(32, 38, 44))
