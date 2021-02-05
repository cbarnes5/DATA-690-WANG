#Create a blank list
int_list = []
#Create a for loop to iterate through integer user request
for i in range(1,11):
    while True:
        try:
            integer=int(input("input an integer:"))
            print(f"You have entered #{i}", integer)
            int_list.append(integer)
        except ValueError: 
            print("Only integers are allowed")
            continue
        break
print("Overall, you have entered:", int_list)
# Set the first number in the list to the maximum
maxnum=int_list[0]
# Create a for loop to test each number in the list against the reigning maximum
for i in range(0, len(int_list)):
    # If the tested number succeds, set it as the new maximum
    if int_list[i]>maxnum:
        maxnum=int_list[i]
print("The Maximum is:", maxnum)
# Set the first number in the list to the minimum
minnum=int_list[0]
# Create a for loop to test each number in the list against the reigning minimum
for i in range(0, len(int_list)):
    # If the tested number succeds, set it as the new minimum
    if int_list[i]<minnum:
        minnum=int_list[i]
print("The Minimum is:", minnum)
# Range = List Max - List Min
rng=maxnum-minnum
print("The Range is:", rng)
# Mean = Sum of list / length of list
mean=sum(int_list)/len(int_list)
print("The Mean is:", mean)
# Variance = The average of the squared difference from the mean
# Create a new list for the squared differences
dif_sqr_list=[] 
# Calculate the difference from the mean of each value, and square it  
for i in range(0, len(int_list)):
    difference=mean-int_list[i]
    dif_sqr=difference ** 2
    dif_sqr_list.append(dif_sqr)
# Average out the list of squared difference
var=sum(dif_sqr_list)/len(dif_sqr_list)
print("The Varience is:", round(var, 2))
# Standard Deviation = Square Root of Variance
StrDev=var ** (1/2)
print("The Standard Deviation is:", round(StrDev, 2))