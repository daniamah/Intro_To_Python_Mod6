############################################################################################################
# Title: Assignment 06
# Description: Working with Functions
#              to display user a menu of options to choose from. Their choices are
#              Reading a file, writing to a file, removing from file,
#              saving to file and lastly exit the program.
#
# ChangeLog (Who,When,What)
#           DaniaM,02.22.2021,Started editing assignment 5 script, defined the ModifyData class to write functions
#           DaniaM,02.23.2021,Executed the save and remove functions and tested the script
#############################################################################################################
# Declare variables
dicRow = {}     # Dictionary definition
strTaskRm = ""  # Enter to be removed
strUsrOpt = ""  # To store option from the menu picked by user
lstRow = []     # List of items in a row from file
lst = []        # List of task and priorities
strMenu = "Menu of Options" "\n" "1) Display current data" "\n" "2) Add Data to List" "\n" "3) Remove an item" "\n" "4) " \
          "Save data to file" "\n" "5) Exit Program "

class ModifyData:
    @staticmethod
    def read_file_to_list():
        objFile = open("ToDo.txt", "r")
        for row in objFile:
            lstRow = row.split(",")
            dicRow = {"Task": lstRow[0], "Priority": lstRow[1]}
            lst.append(dicRow)
        objFile.close()
        return lst

    @staticmethod
    def write_data_from_list_to_file(lst):
        status = False
        objFile = open("ToDo.txt", "w")
        for dicRow in lst:
            objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        objFile.close()
        #print("Your data has been saved!")
        status = True
        return status

    @staticmethod
    def add_data_to_list(lst):
        strTask = input("Enter the task: ")
        strPri = input("Enter task priority: ")
        lstRow = {"Task": strTask, "Priority": strPri}
        lst.append(lstRow)

    @staticmethod
    def remove_data_from_list(lst):
        status = False
        strTaskRm = str(input("Enter task name you want to remove? "))
        lst_len = len(lst)

        i = 0
        found = False
        while (i < lst_len):
            if strTaskRm in lst[i].values():
                del lst[i]
                print(strTaskRm + " has been removed!")
                found = True
                break
            i = i + 1

        if found == False:
            print("Task not found!")

        return True

    @staticmethod
    def display_current_data(lst):
        for row in lst:
            print(row["Task"] + "," + row["Priority"])

# Execute script depending on user input
while (True):
 print(strMenu)
 strUsrOpt = int(input("Which option would you like to perform? [1 to 5] "))
 if strUsrOpt == 1:
     ModifyData.display_current_data(lst)

 elif strUsrOpt == 2:
     ModifyData.add_data_to_list(lst)

 elif strUsrOpt == 3:
     ModifyData.remove_data_from_list(lst)

 elif strUsrOpt == 4:
     ModifyData.write_data_from_list_to_file(lst)

 elif strUsrOpt == 5:
     exit()