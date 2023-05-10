import sqlite3
from datetime import datetime

def staffmembersinfo():
  name = ""
  hourlyratewhile = 0  
  day = ""
  
  while namewhile == 0:
    name = input("Name: ")
    if name != "":
      namewhile = 1  
  while hourlyratewhile == 0:
    hourlyrate = int(input("Hourly Rate: "))
    while hourlyrate != "" and hourlyratewhile != 1:
      hourlyratewhile = 1
  contdaysoffwhile = "y"
  while contdaysoffwhile == "y":
    contdaysoffwhile = input("Continued days off (y/n): ")
    if contdaysoffwhile == "Y" or contdaysoffwhile == "y":
      end = 0
      while end != 1:
        day = ""
        day = input("Day off (press enter to cancel): ")
        if day == "":
          end = 1
          contdaysoffwhile = "n"
        else:
          for x in range(7):
            if day == "":
                end = 1
                contdaysoffwhile = "n"
            if day != "":
              day = input("Day off (press enter to cancel): ")
  return name, hourlyrate, day

def newStaffMemberInfo():
  full = False

  




def rotainfo():
  loop1 = True
  loop2 = True
  
  while loop1:
    try:
      minlen = int(input("Minimum shift length:\n"))
      loop1 = False
    except:
      print("Minimum shift length must be a whole number")
  while loop2:
    try:
      maxlen = int(input("Maximum shift length:\n"))
      loop2 = False
    except:
      print("Maximmum shift length must be a whole number")
    

def inserttimes():
  loop1 = True
  dateobject = 0
  while loop1:
    try:
      shiftstart = input(current, "in the form HHMM:\n")
      dateobject = datetime.strptime(shiftstart, "%H%M").time()
      loop1 = False
    except:
      print("Enter in Form HHMM")
    print(dateobject)
    return(dateobject)


def timingsinfo():
  current = "First Shift Start Time"
  sqlcurrent = "shiftstart"
  inserttimes(current)
  crs.execute("""INSERT INTO timingsinfo""", current, """VALUES (?)""", dateobject)

  

connection = sqlite3.connect('database.db')
crs = connection.cursor()







###--creating blank tables start--###

## def make a funciton here create manager info (def manInfoCreate)
crs.execute("DROP TABLE IF EXISTS managerinfo")
sql = """CREATE TABLE managerinfo(
        name VARCHAR(225) NOT NULL,
        hourlyrate DECIMAL(2,3) DEFAULT(00.000) NOT NULL,
        contdaysoff VARCHAR(225) DEFAULT NULL
      );"""
crs.execute(sql)
## Function (def manInfoCreate) ends here


## def make a function here create supervisor info (def supInfoCreate)
crs.execute("DROP TABLE IF EXISTS supervisorinfo")
sql = """CREATE TABLE supervisorinfo(
        name VARCHAR(225) NOT NULL,
        hourlyrate DECIMAL(2,3) DEFAULT(00.000),
        contdaysoff VARCHAR(225) DEFAULT NULL
      );"""
crs.execute(sql)
## (def supInfoCreate) ends her

##########################
####make all of these#####
####silly SQL things######
####its own function######
##########################

crs.execute("DROP TABLE IF EXISTS fulltimeinfo")
sql = """CREATE TABLE fulltimeinfo(
        name VARCHAR(225) NOT NULL,
        hourlyrate DECIMAL(2,3) DEFAULT(00.000),
        contdaysoff VARCHAR(225) DEFAULT NULL
      );"""
crs.execute(sql)

crs.execute("DROP TABLE IF EXISTS parttimeinfo")
sql = """CREATE TABLE parttimeinfo(
        name VARCHAR(225) NOT NULL,
        hourlyrate DECIMAL(2,3) DEFAULT(00.000),
        contdaysoff VARCHAR(225) DEFAULT NULL
      );"""
crs.execute(sql)

crs.execute("DROP TABLE IF EXISTS rotainfo")
sql = """CREATE TABLE rotainfo(
        minshiftlen INTEGER,
        maxshiftlen INTEGER,
      );"""
crs.execute(sql)

crs.execute("DROP TABLE IF EXISTS timingsinfo")
sql = """CREATE TABLE timingsinfo(
   openshift TIME NOT NULL,
   businessopen TIME NOT NULL,
   peaktimestart TIME NOT NULL,
   peaktimeend TIME NOT NULL,
   businessclose TIME NOT NULL,
   closeshiftend NOT NULL
   );"""
crs.execute(sql)

crs.execute("DROP TABLE IF EXISTS staffing")
sql = """create table staffing (
   staffforopen INTEGER NOT NULL,
   stafffromopen INTEGER NOT NULL,
   staffatpeak INTEGER NOT NULL,
   staffuntilclose INTEGER NOT NULL,
   staffforclose INTEGER NOT NULL
   );"""
crs.execute(sql)

connection.commit()


#crs.execute("SELECT * FROM managerinfo")
#print(crs.fetchall())
###--creating blank tables end--####

print("New Manager")
staffmembersinfo()
crs.execute("""INSERT INTO managerinfo ("name", hourlyrate, contdaysoff) VALUES (?, ?, ?)""", (name, hourlyrate, day))
crs.execute("SELECT * FROM managerinfo")
print(crs.fetchall())

fulltime = "filler"
while fulltime != "":
  print("New Full Time Staff Member")
  staffmembersinfo()
  crs.execute("""INSERT INTO fulltimeinfo ("name", hourlyrate, contdaysoff) VALUES (?, ?, ?)""", (name, hourlyrate, day))
  crs.execute("SELECT * FROM fulltimeinfo")
  print(crs.fetchall())
  print("New Full Time Staff Member (Press Enter to Cancel)\n")
  fulltime = input

parttime = "filler"
while parttime != "":
  print("New Part Time Staff Member")
  staffmembersinfo()
  crs.execute("""INSERT INTO parttimeinfo ("name", hourlyrate, contdaysoff) VALUES (?, ?, ?)""", (name, hourlyrate, day))
  crs.execute("SELECT * FROM parttimeinfo")
  print(crs.fetchall())
  print("New Part Time Staff Member (Press Enter to Cancel)\n")
  parttime = input

print("Extra information")
rotainfo()
crs.execute("""INSERT INTO rotainfo (minshiftlen, maxshiftlen) values (?, ?""", (minlen, maxlen))

print ()
inserttimes()


connection.close()
