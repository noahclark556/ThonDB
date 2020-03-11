import time
import os.path
from os import path

from pip._vendor.distlib.compat import raw_input
from ThonDB import Runner
from ThonDB import ReadReturn

import os


def writer(db):
    db = os.getcwd() + "\\ThonDB\\databases\\" + db
    with open(db, "a") as currentdb:
        currentdb.write("")
        currentdb.close()
    return "Database created: " + str(db)


clear = lambda: os.system('cls')


class Main:
    clear()
    while True:

        if __name__ == "__main__":

            print("Welcome to ThonDB query console:")

            reador = raw_input("Create new Database?(y/n)")

            if reador == "y":
                db = raw_input("Please enter name of database, do not include extensions:")
                print(writer(db + ".tdb"))
                print("please wait..")
                time.sleep(4)
            print("Ready to connect!")
            dbPath = raw_input("Enter name of database file in databases directory, do not include extensions: ")
            dbPath += ".tdb"
            dbPath = os.getcwd() + "\\ThonDB\\databases\\" + dbPath
            if path.exists(dbPath):
                dbTable = raw_input("Enter name of table (leave blank if none exist): ")

                try:

                    read = ReadReturn.ReadReturn(dbPath, dbTable)
                except:
                    print("Failure to communicate with db")
                    exit()

                while True:
                    Runner.runCommand(read)
            else:
                print("That database does not exist")
