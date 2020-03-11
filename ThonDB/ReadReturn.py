import os

if __name__ == "__main__":
    print("Run file main.py, not this one")


class ReadReturn:

    def isEmptyDb(self):
        if os.stat(self.db).st_size == 0:
            return True
        else:
            return False

    def reload(self, db, table="none"):
        self.db = db
        # print(self.db)
        self.table = table
        self.dataList = []
        self.dataDict = {}
        with open(self.db, "r") as currentdb:
            currentdb.seek(0)
            for line in currentdb:

                if (line.split("|")[0]) == self.table + "GUID-199876" or (line.split("|")[0]) == self.table:
                    datastring = line.split("|")[1:]
                    count = 0
                    for item in datastring:
                        self.dataDict[item.split(":")[0]] = item.split(":")[1].rstrip(
                            "\n")  # cast into readable dictionary
                    self.dataList.append(self.dataDict.copy())
            currentdb.close()

    def delete(self, col, val):
        with open(self.db, "r") as f:
            lines = f.readlines()
            f.close()
        with open(self.db, "w") as f:
            for line in lines:
                checkstr = col + ":" + val
                curline = line.strip("\n")
                if checkstr in curline and str(self.table) in curline:
                    pass
                else:
                    f.write(line)
            f.close()
        self.reload(self.db, self.table)

    def deletePlaceholder(self):
        with open(self.db, "r") as f:
            f.seek(0)
            lines = f.readlines()
            f.close()
        with open(self.db, "w") as f:
            f.seek(0)
            for line in lines:
                checkstr = "GUID-199876"
                curline = line.strip("\n")
                if checkstr in curline and str(self.table) in curline:
                    pass
                else:
                    f.write(line)
            f.close()
        self.reload(self.db, self.table)

    def insertRow(self, queryString):
        try:
            with open(self.db, "a") as writingDb:
                writingDb.seek(0)
                writingDb.write(queryString + "\n")
                writingDb.close()

        except Exception as e:
            print(e)
        self.reload(self.db, self.getTable())


    def __init__(self, db, table):
        self.db = db
        # print(self.db)
        self.table = table
        self.dataList = []
        self.dataDict = {}
        if self.table != "":
            self.reload(self.db, self.table)
        else:
            print("Please select a Table or insert a new one (type help)")

    def selectTable(self, tbName):
        self.table = tbName
        self.reload(self.db, self.table)

    def refresh(self):
        self.reload(self.db, self.table)

    def getSpecific(self, column, row=0):
        try:
            print("\n")
            return self.dataList[row].get(column)
        except:
            print("Column or row does not exist in the table")
            return

    def getRawRow(self, format="raw"):
        count = 1
        try:
            if format == "raw":
                for item in self.dataList:
                    print("\n")
                    print("   ROW: " + str(count))
                    count += 1
                    yield item
            if format == "pairs":
                for item in self.dataList:
                    print("\n")
                    print("   ROW: " + str(count))
                    count += 1
                    for key in item:
                        yield key, '->', item[key]
            if format == "keys":
                for item in self.dataList:
                    print("\n")
                    for key in item:
                        yield key
                    return
        except Exception as e:
            print(e)
            print("Failed to execute query")
        finally:
            return

    def getTable(self):
        return str(self.table)

    def getSize(self):
        print("\n")
        return str(len(self.dataList)) + " rows in table " + self.table
