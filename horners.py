from fractions import Fraction

def horners(poly, n, x):
    result = poly[0]

    for i in range(1, n):
        result = result*x + poly[i]

    return result


poly = [1,0,0,-9]
x = 2.078125
n = len(poly)

if __name__ == '__main__':
    print("Value of the polynomial is " , horners(poly,n,x))
