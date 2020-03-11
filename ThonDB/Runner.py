if __name__ == "__main__":
    print("Run file main.py, not this one")

from pip._vendor.distlib.compat import raw_input

import os

def clear():
    os.system('cls')

def runCommand(read):
    command = raw_input("Enter a query command: ")
    listcom = command.split(".")

    try:
        if listcom[0] == "getRawRows":
            if read.getTable() == "none" or read.getTable() == "":
                print("Please select a Table or insert a new one (type help)")
            else:
                for item in read.getRawRow(listcom[1]):
                    print(item)
        elif listcom[0] == "getSpecific":
            if (read.getTable() == "none" or read.getTable() == ""):
                print("Please select a Table or insert a new one (type help)")
            else:
                print(read.getSpecific(str(listcom[1]), int(listcom[2])))
                print("\n")
        elif listcom[0] == "deleteRow":
            if (read.getTable() == "none" or read.getTable() == ""):
                print("Please select a Table or insert a new one (type help)")
            else:
                read.delete(listcom[1], listcom[2])
                print("Deleted row where column = " + listcom[1] + " and value = " + listcom[2])
                print("\n")
        elif listcom[0] == "getSize":
            if(read.getTable() == "none" or read.getTable() == ""):
                print("Please select a Table or insert a new one (type help)")
            else:
                print(read.getSize())
                print("\n")
        elif listcom[0] == "selectTable":
            read.selectTable(listcom[1])
            print("Table " + listcom[1] + " is selected")
            read.refresh()
            print("\n")
        elif listcom[0] == "help":
            print("\n")
            print("________________________________________HELP MENU__________________________________________________")
            print("QUERY COMMANDS -- CURRENTLY CaSe SeNsAtIvE --- DO NOT INCLUDE {} IN QUERY")
            print("NOTE: TO BREAK ANY QUERY, TYPE 'STOP()'")
            print("_____________________________________RETRIEVE COMMANDS_____________________________________________")
            print("getRawRows.{FORMAT} -- FORMAT is either raw or pairs -- Returns full table data")
            print("getSpecific.{COLUMN}.{ROW} -- COLUMN is column name, ROW is row number -- returns specific of data "
                  "pointed to")
            print("getSize -- Returns size of currently selected table")
            print("selectTable.{TABLE_NAME} -- Used when switching between tables in a query console")
            print("______________________________________UPDATE COMMANDS______________________________________________")
            print("deleteRow.{COLUMN}.{VALUE} -- Delete row from selected table where column={COLUMN} and value={"
                  "VALUE}")
            print("insert -- Allows insertion into existing table")
            print("newTable -- Allows creation of new table")
            print("___________________________________________________________________________________________________")
            print("\n")
        elif listcom[0] == "newTable":
            tbName = raw_input("Enter Table Name:")
            queryString = tbName + "GUID-199876"
            print("type stop() to break")
            print("Setting up table " + tbName)
            counter = 0
            while True:
                col = raw_input("Enter name of column " + str(counter) + ": ")
                if col == "stop()":
                    break
                queryString += "|" + col + ":PLACEHOLDER_ROW"
                counter+=1
            read.selectTable(tbName)
            read.insertRow(queryString)

            print("Selected table is now " + tbName)

            read.refresh()
        elif listcom[0] == "insert":
            if read.getTable() == "none" or read.getTable() == "":
                print("No table selected...")
                print("Please select a table with selectTable.{TABLE_NAME} or create a new one with newTable")
            else:
                print("Type stop() to quit")

                print("inserting into table " + read.getTable())

                go = True
                while (True):
                    qstring = read.getTable()
                    for item in read.getRawRow("keys"):
                        input = raw_input("insert " + item + ":")
                        if input == "stop()":
                            read.deletePlaceholder()
                            go = False
                            break
                        qstring += "|" + item + ":" + input
                    if go == True:
                        read.insertRow(qstring)
                    else:
                        break



                print("Make sure to use command selectTable.{TABLE_NAME} to select new table")
            print("\n")
        elif listcom[0] == "clear":
            clear()
        elif listcom[0] == "exit":

            exit()
        elif listcom[0] == "refresh":
            read.refresh()
        else:
            print("Invalid Query Command")
    except Exception as e:
        # print("Please input valid query commands (type: help)")
        print(e)
    finally:
        return
