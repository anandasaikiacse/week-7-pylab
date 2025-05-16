# Q)44) Create a dataframe using a list of elements.
# Aim: To work with Pandas data frames
# ALGORITHM  
# Step1: Start  
# Step2: import numpy and pandas module  
# Step3: Create a dataframe using the dictionary  
# Step4: Print the output  
# Step5: Stop


# Program:

import numpy as np  
import pandas as pd  
data = np.array([['','Col1','Col2'],  
['Row1',1,2],  
['Row2',3,4]])  
print(pd.DataFrame(data=data[1:,1:],  
index = data[1:,0],  
columns=data[0,1:]))  
# Take a 2D array as input to your DataFrame  
my_2darray = np.array([[1, 2, 3], [4, 5, 6]])  
print(pd.DataFrame(my_2darray))  
# Take a dictionary as input to your DataFrame  
my_dict = {1: ['1', '3'], 2: ['1', '2'], 3: ['2', '4']}  
print(pd.DataFrame(my_dict))  
# Take a DataFrame as input to your DataFrame  
my_df = pd.DataFrame(data=[4,5,6,7], index=range(0,4), columns=['A'])  
print(pd.DataFrame(my_df))  
# Take a Series as input to your DataFrame  
my_series = pd.Series({"United Kingdom":"London", "India":"New Delhi", "United States":"Washington", "Belgium":"Brussels"})  
print(pd.DataFrame(my_series))  
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]))  
# Use the `shape` property  
print(df.shape)  
# Or use the `len()` function with the `index` property  
print(len(df.index))


# Q)45) AIM: To Implement working with Pandas data frame using python code.
# ALGORITHM:
# Step 1: Start the program.  
# Step 3: Import pandas with an aliased name as pd.  
# Step 4: Create a given list and assign it to variable data.  
# Step 5: Call the data Frame function (data), and assign it to variable t.  
# Step 6: Call the Print function to print the Pandas data frame(t).  
# Step 7: Stop the program.


# Program:

import pandas as pd

data = {
    "Name": ["Ram", "Subash", "Raghul", "Arun", "Deepak"],
    "Age": [24, 25, 24, 26, 25],
    "CGPA": [9.5, 9.3, 9.0, 8.5, 8.8]
}

t = pd.DataFrame(data)
t.index += 1
print(t)