#Need to import mean function from library, which is listed at the top of the page.
from statistics import mean

Set1 = float(input("Input total number of samples Set1 "))
Set2 = float(input("Input total number of samples Set2 "))
Set3 = float(input("Input total number of samples Set3 "))
Set4 = float(input("Input total number of samples Set4 "))
Set5 = float(input("Input total number of samples Set5 "))
Set6 = float(input("Input total number of samples Set6 "))
Set7 = float(input("Input total number of samples Set7 "))
Set8 = float(input("Input total number of samples Set8 "))
Set9 = float(input("Input total number of samples Set9 "))
Set10 = float(input("Input total number of samples Set10 "))

#Make sure to include both ([]), because the brackets make it a list.
average = mean([Set1, Set2, Set3, Set4, Set5, Set6, Set7, Set8, Set9, Set10])
print("Average is: ", average)
