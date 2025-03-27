#######################################################################################################################################################
# 
# Name: Amir Suhail
# SID: 750018850
# Exam Date: 3/27/2025
# Module: BEMM458 Programming for Business Analytics
# Github link for this assignment: https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-hadeshades00 
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

Answer 1: 
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""
# SID first and last digits
sid = "750018850"
digit1 = int(sid[0])
digit2 = int(sid[-1])

#Trying to get only the relevant keywords
alloc_keywords = [key_comments[digit1], key_comments[digit2]]

# Now we will initialize the list to hold the start and end positions respectively
my_list = []

#Now we will loop through the 'allocated keywords' and find their positions
for word in alloc_keywords:
    start = customer_feedback.find(word)  #Starting index
    if start != -1:  
        end = start + len(word)  # if word is found, calculate end index
        my_list.append((start, end))  # Appending to  the list
# Output 
print("Printing the start and end positions respectively:", my_list)

### Output Printing the start and end positions respectively: [(129, 136), (38, 50)]
###

##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here: 75
# Insert last two digits of ID number here: 50

# Write your code for Operating Profit Margin
# Operating Profit Margin
def opm(profit, revenue):
    return ((profit / revenue) * 100)

# Write your code for Revenue per Customer
def rpc(revenue, customers):
    return (revenue / customers)

# Write your code for Customer Churn Rate
def ccr(lost, start):
    return ((lost / start) * 100)

# Write your code for Average Order Value
def aov(revenue, orders):
    return (revenue / orders)

# Sample input assignments
p = sid_1      # Operatingprofit
r = sid_2       # Total revenue
c = sid_2      # Customers
o = sid_2          # Orders
s = sid_1       # Starting customers
l = sid_2           # Customers lost

# Call your designed functions here

print("Operating Profit Margin:", opm(p, r), "%")
print("Revenue per Customer:", rpc(r, c))
print("Customer Churn Rate:", ccr(l, s), "%")
print("Average Order Value:", aov(r, o))


###Output: Operating Profit Margin: 150.0 %
Revenue per Customer: 1.0
Customer Churn Rate: 66.66666666666666 %
Average Order Value: 1.0 ###


##########################################################################################################################################################



# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here

#Importing relevant libraries

import pandas as pd
from sklearn.linear_model import LinearRegression

# simple data from the shop: price vs. how many people bought
d = {
    "p": [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],  # price (£)
    "q": [300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85]  # demand (units)
}

# turning it into a table
df = pd.DataFrame(d)

# reshaping price for the model (needs to be 2D)
X = df[["p"]]
y = df["q"]

# let's train the model
m = LinearRegression()
m.fit(X, y)

# now let's predict what the model thinks demand would be
df["pred_q"] = m.predict(X)

# rlet evenue is price * predicted demand
df["rev"] = df["p"] * df["pred_q"]

# lets find the row where revenue is highest
best_row = df.loc[df["rev"].idxmax()]
best_p = best_row["p"]
best_rev = best_row["rev"]

# let's find the demand st 52 pounds
d52 = m.predict([[52]])[0]

# show results
print("Best price to make max money: £", round(best_p, 2))
print("Expected max revenue: £", round(best_rev, 2))
print("Expected demand at £52: ", round(d52, 2), "units")


###Output: Best price to make max money: £ 45.0
Expected max revenue: £ 8529.55
Expected demand at £52:  158.17 units###

##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
max-value = integer(input("Enter your Student ID: ")) 
random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='O', markercolor='green', markeredgcolor='red', linestyle='--', lable='Random Numbers', color='blue');
plt.title(Line Chart of 100 Random Numbers)
plt.xlabel="Index"
plt.ylabel="Random Number"
plt.legend('---')
plt.grid(True)
plt.show()


Fixes to be done:
•	max-value → sid (can’t use hyphen in variable name, has to be underscore)
•	integer() → int() wront syntax
•	lable → should be label (wrong spelling)
•	plt.title() needs quotation mark for the string
•	marker='O' → lowercase 'o' ( is the valid marker)
•	markercolor → should be markerfacecolor instead
•	markeredgcolor → should be markeredgecolor
•	plt.xlabel = → should be plt.xlabel()




