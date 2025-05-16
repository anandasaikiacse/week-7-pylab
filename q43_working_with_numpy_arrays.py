# Q)43) AIM : Working with Numpy arrays  
# ALGORITHM  
# Step1: Start  
# Step2: Import numpy module  
# Step3: Print the basic characteristics and operactions of array  
# Step4: Stop

# A) Program:
    
import numpy as np  
# Creating array object  
arr = np.array( [[ 1, 2, 3],  
[ 4, 2, 5]] )  
# Printing type of arr object  
print("Array is of type: ", type(arr))  
# Printing array dimensions (axes)  
print("No. of dimensions: ", arr.ndim)  
# Printing shape of array  
print("Shape of array: ", arr.shape)  
# Printing size (total number of elements) of array  
print("Size of array: ", arr.size)  
# Printing type of elements in array  
print("Array stores elements of type: ", arr.dtype)


# B) NUMPY OPERATIONS WITH ARRAYS

import numpy as np

a = np.array([[1, 2], [4, 5]])
b = np.array([[1, 2], [4, 5]])

while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Dot product")
    print("6. Exponentiation")
    print("7. Logarithm (base e)")
    print("8. Logarithm (base 10)")
    print("9. Exit")

    n = int(input("Enter the option number: "))

    if n == 1:
        c = np.add(a, b)
        print("Sum:\n", c)
    elif n == 2:
        d = np.subtract(a, b)
        print("Difference:\n", d)
    elif n == 3:
        e = np.multiply(a, b)
        print("Product:\n", e)
    elif n == 4:
        f = np.divide(a, b)
        print("Quotient:\n", f)
    elif n == 5:
        g = np.dot(a, b)
        print("Dot Product:\n", g)
    elif n == 6:
        h = np.exp(a)
        i = np.exp(b)
        print("Exponentiation for array a:\n", h)
        print("Exponentiation for array b:\n", i)
    elif n == 7:
        l = np.log(a)
        m = np.log(b)
        print("Natural Logarithm (base e) for array a:\n", l)
        print("Natural Logarithm (base e) for array b:\n", m)
    elif n == 8:
        x = np.log10(a)
        y = np.log10(b)
        print("Logarithm (base 10) for array a:\n", x)
        print("Logarithm (base 10) for array b:\n", y)
    elif n == 9:
        print("Exiting program.")
        break
    else:
        print("No such option exists, please enter a valid option.")



# C) Program to Perform Array Slicing.

a = np.array([[1,2,3],[3,4,5],[4,5,6]])  
print(a)  
print("After slicing")  
print(a[1:])


# D) Program to Perform Array Slicing.

# array to begin with  
import numpy as np  
a = np.array([[1,2,3],[3,4,5],[4,5,6]])  
print('Our array is:' )  
print(a)

# this returns array of items in the second column  
print('The items in the second column are:' )  
print(a[...,1])  
print('\n' )

# Now we will slice all items from the second row
print ('The items in the second row are:' )  
print(a[1,...])
print('\n' )

# Now we will slice all items from column 1 onwards  
print('The items column 1 onwards are:' )  
print(a[...,1:])