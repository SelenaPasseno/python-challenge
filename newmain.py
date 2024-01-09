#Dataset contains two columns: "Date" and "Profit/Loss" 


#Items asked for:

# Objective 1 - Total number of months in dataset.  
#Total # of months in the dataset >> column A = "Date" >> Use count to determine months
#The net total amount of "Profit/Losses" over the entire period >> column B = "Profit/Loss"

#months = "count"
#num_months = len(date)


#Your task is to create a Python script that analyzes the records to calculate each of the following values:

# Objective A: The total number of months included in the dataset  
#The net total amount of "Profit/Losses" over the entire period
    #
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period


#1 import os and csv modules

import os
import csv

#2 set the pathway for the file to be read

budget_data_csv_path = os.path.join(r"c:\\Users\\slpas\\PythonClass\\python-challenge\\PyBank\\Resources\\budget_data.csv")

#3 set and initialize the variables to use with dataset

months = []
profit_loss_changes = []

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

#4 read in the csv file for manipulation of data and solving the problem set up a delimintated file
with open(budget_data_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")

    #5 read header row to remove from calculations
    header = next(csv_reader)

    #6 Loop through each row of data after skipping header rwo
    for row in csv_reader:

        #7 count number of months
        count_months += 1

        #8 total up the net amount of profit/losses over period
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        #9 set up if statement to count months and make value of previous month equal to current month
        if (count_months == 1):
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:            
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss  #determine change in profit/loss
           
            #10 Add append statement to append each month to current months[]
            months.append(row[0])

            #11 Add append to each profit_loss_change to the profit_loss_changes []
            profit_loss_changes.append(profit_loss_change)

            #12 make current month loss into the previous month profit loss to set up next loop
            previous_month_profit_loss = current_month_profit_loss
    
#Objective B asum up the profit_loss and average the profit_loss over the period
    sum_profit_loss = sum(profit_loss_changes)

#Objective C average changes in profit_losses 
    average_profit_loss = round(sum_profit_loss/(count_months -1), 2)

#objective D and E greatest change in profits dollar amounts
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

#Objective D ad E locate the highest and lowest profit and loss over period and assign it to an index so that it can be called out 
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    #Assigning highest and lowest by best and worse months
    greatest_increase_month = months[highest_month_index]
    greatest_decrease_month = months[lowest_month_index]

#Objective F - Print the results to the terminal 
print("Financial Analysis of PyBank")
print("________________________________")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  S{average_profit_loss}")
print(f"Greatest Increase in Profits:  {greatest_increase_month} ($ {highest_change})")
print(f"Greatest Decrease in Losses:  {greatest_decrease_month} ($ {lowest_change})")

#Objective G - Print results to text_file ls
budget_file = os.path.join("Analysis", "budget_data.txt")
with open(budget_file, "w") as text_file:
    text_file.write("Financial Analysis \n")
    text_file.write("____________________________\n")
    text_file.write(f"Total Months:  {count_months}\n")
    text_file.write(f"Total: $ {net_profit_loss}\n")
    text_file.write(f"Average Change: ${average_profit_loss}\n")
    text_file.write(f"Greatest Increase in Profits: {greatest_increase_month} ($ {highest_change})\n")
    text_file.write(f"Greatest Decrease in Losses:  {greatest_decrease_month} (${lowest_change})\n")


   
           
           
           
           
           
          







