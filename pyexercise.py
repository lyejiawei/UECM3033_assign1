import sympy as sy
import numpy as np

def fun_1( my_id ):
    ans = hex(my_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate(sy.exp(-x)*(sy.sqrt(x)), (x,0, sy.oo))
    return ans

def my_solution():
    A = np.array( [[3,1,6,0,4,3,2,8,9,5], [1,2,7,0,8,4,2,9,4,1], [3,6,5,5,6,8,0,2,9,1], [4,5,7,8,3,2,1,0,5,8], [1,2,0,4,3,5,6,7,8,3], [5,3,3,6,7,9,2,1,3,0], [1,2,3,8,6,3,4,5,0,9], [2,2,5,8,7,4,4,0,9,1], [2,3,7,8,4,5,3,6,0,1], [5,6,7,8,3,2,1,4,5,3]] )
    b = np.array([9,8,3,2,1,0,4,6,5,2])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    my_id = 1403855
    print('Hexadecimal representation of %d is %s'%( my_id, fun_1( my_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())