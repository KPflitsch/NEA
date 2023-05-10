def timingsinfo():
  loop1 = True

  while loop1:
    try:
      shiftstart = input("First Shift Start Time, in the form HHMM:\n")
      dateobject = datetime.strptime(shiftstart, "%H %M")
      loop1 = False
    except:
      print("Enter in Form HHMM")
    print(dateobject)


timingsinfo()