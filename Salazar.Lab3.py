#Christopher Salazar
# Lab 3 starter code
# CSC 110

import math

def main():
    print("This program is to test functions")
    print()
    print('base1\t\tbase2\t\theight\t\tarea')
    areaTrapezoid(4,5,8)
    print()
    areaTrapezoid(2, 7, 9)
    
    print()
    print('Calculate the hypotneuse of a right triangle.' )
    print()
    opposite = int(input('What is the length of one side of the triangle? '))
    adjacent = int(input('What is the length of the other side of the triangle? ' ))
    print()
    areaTriangle(opposite, adjacent)
  
# This function calculates and returns the area of a trapezoid
# parameter: base1, the length of the top of the trapezoid
# parameter: base2, the length of the bottom
# parameter: height, the height of the trapezoid
# See this website for a picture  http://math.com/tables/geometry/areas.htm

def areaTrapezoid(base1, base2, height):
    
    area = height / 2.0 * (base1 + base2)
    print(base1,'\t\t', base2,'\t\t', height,'\t\t', area)

    return area

def areaTriangle(lega, legb):
    
    hypotneuse = math.sqrt(lega**2 + legb**2)
    print('LegA\t\tLegB\t\thypotneuse')
    print(lega,'\t\t', legb,'\t\t', format(hypotneuse, '.2f'))

    
main()

