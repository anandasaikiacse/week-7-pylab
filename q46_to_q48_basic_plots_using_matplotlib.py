# Q)46) Aim: To draw basic plots in Python program using Matplotlib

# ALGORITHM
# Step1: Start  
# Step2: import Matplotlib module  
# Step3: Create a Basic plots using Matplotlib  
# Step4: Print the output  
# Step5: Stop


# A) Program: 

# importing the required module  
import matplotlib.pyplot as plt  
# x axis values  
x = [1,2,3]  
# corresponding y axis values  
y = [2,4,1]  
# plotting the points  
plt.plot(x, y)  
# naming the x axis  
plt.xlabel('x - axis')  
# naming the y axis  
plt.ylabel('y - axis')  
# giving a title to my graph  
plt.title('My first graph!')  
# function to show the plot  
plt.show()


# B) Program:

import matplotlib.pyplot as plt 
a = [1, 2, 3, 4, 5] 
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21] 
plt.plot(a) 
# o is for circles and r is 
# for red 
plt.plot(b, "or") 
plt.plot(list(range(0, 22, 3))) 
# naming the x-axis 
plt.xlabel('Day ->') 
# naming the y-axis 
plt.ylabel('Temp ->') 
c = [4, 2, 6, 8, 3, 20, 13, 15] 
plt.plot(c, label = '4th Rep') 
# get current axes command 
ax = plt.gca() 
# get command over the individual 
# boundary line of the graph body 
ax.spines['right'].set_visible(False) 
ax.spines['top'].set_visible(False) 
# set the range or the bounds of  
# the left boundary line to fixed range  
ax.spines['left'].set_bounds(-3, 40)  
# set the interval by which  
# the x-axis set the marks  
plt.xticks(list(range(-3, 10)))  
# set the intervals by which y-axis  
# set the marks  
plt.yticks(list(range(-3, 20, 3)))  
# legend denotes that what color  
# signifies what  
ax.legend(['1st Rep', '2nd Rep', '3rd Rep', '4th Rep'])  
# annotate command helps to write  
# ON THE GRAPH any text xy denotes  
# the position on the graph  
plt.annotate('Temperature V / s Days', xy = (1.01, -2.15))  
# gives a title to the Graph  
plt.title('All Features Discussed')  
plt.show()


# C) Program:

import matplotlib.pyplot as plt  
a = [1, 2, 3, 4, 5]  
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21]  
c = [4, 2, 6, 8, 3, 20, 13, 15] 

fig = plt.figure(figsize =(10, 10))  
# creating multiple plots in a  
# single plot  
sub1 = plt.subplot(2, 2, 1)  
sub2 = plt.subplot(2, 2, 2)  
sub3 = plt.subplot(2, 2, 3)  
sub4 = plt.subplot(2, 2, 4)  
sub1.plot(a, 'sb')  
# sets how the display subplot  
# x axis values advances by 1  
# within the specified range  
sub1.set_xticks(list(range(0, 10, 1)))  
sub1.set_title('1st Rep')  
sub2.plot(b, 'or')  
# sets how the display subplot x axis  
# values advances by 2 within the  
# specified range  
sub2.set_xticks(list(range(0, 10, 2)))  
sub2.set_title('2nd Rep')  
# can directly pass a list in the plot  
# function instead adding the reference  
sub3.plot(list(range(0, 22, 3)), 'vg')  
sub3.set_xticks(list(range(0, 10, 1)))  
sub3.set_title('3rd Rep')
sub4.plot(c, 'Dm')  
# similarly we can set the ticks for  
# the y-axis range(start(inclusive),  
# end(exclusive), step)  
sub4.set_yticks(list(range(0, 24, 2)))  
sub4.set_title('4th Rep')  
# without writing plt.show() no plot  
# will be visible  
plt.show()


# Q)47) AIM: To Implement Plotting the points for line graph using Matplotlib using python code.

# ALGORITHM:  
# Step 1: Store in x1=[1,4,6,8]  
# Step 2: Store in y1=[2,5,8,9]  
# Step 3:Using plot() We can set the label as lineA and color of the line as red with x1 and y1 as co-ordinates.  
# Step 4: Store in x2=[3,6,8,10]  
# Step 5: Store in y2=[2,4,8,9]  
# Step 6:Using plot() We can set the label as line B and color of the line as green with x2 and y2 as co-ordinates.  
# Step 7: Using xlim() and ylim() we can set the points as 0 to 12 on x-axis and y- axis .  
# Step 8: show the x-axis and y-axis of the plot, show the title as Graph. 


# Program:

import matplotlib.pyplot as mpl

# Data for Line A
x1 = [1, 4, 6, 8]  
y1 = [2, 5, 8, 9]  
mpl.plot(x1, y1, label="Line A", color="r")

# Data for Line B
x2 = [3, 6, 8, 10]  
y2 = [2, 4, 8, 9]  
mpl.plot(x2, y2, label="Line B", color="g")

# Set axis limits
mpl.xlim(0, 12)  
mpl.ylim(0, 12)

# Add labels and title
mpl.xlabel("X-axis")  
mpl.ylabel("Y-axis")  
mpl.title("Graph")

# Show legend and plot
mpl.legend()  
mpl.show()


# Q)48) AIM: To Implement a bar chart using Matplotlib using python code.

# ALGORITHM:  
# Step 1: Store in x=[1,2,3,4,5]  
# Step 2: Store in y=[50,65,85,87,98]  
# Step 3: Store in text=["IBM","Amazon","Facebook","Microsoft","Google"] Step4: Store in colors=["red","orange","yellow","blue","green"]  
# Step 5: Using xlim() and ylim() we can set the points as 0 to 6 on x-axis and 0 to 100 on y- axis respectively.  
# Step 6: Using bar() we can create a bar graph with x,y with label as text and color=colors and line width of the graph as 0.5.  
# Step 6: show the x-axis and y-axis of the plot as ‘Company' and 'Percentage', show the title as Percentage Graph.


# Program: 

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [50, 65, 85, 87, 98]
text = ["IBM", "Amazon", "Facebook", "Microsoft", "Google"]
colors = ["red", "orange", "yellow", "blue", "green"]
plt.xlim(0, 6)
plt.ylim(0, 100)
plt.bar(x, y, tick_label=text, color=colors, linewidth=0.5)
plt.xlabel("Company")
plt.ylabel("Percentage")
plt.title("Percentage Graph")
plt.show()