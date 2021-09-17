def area_of_triangle(a, b, c):
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return area


print(area_of_triangle(32, 38, 44))
