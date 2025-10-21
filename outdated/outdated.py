month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
months = ["01", "02", '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
day = ["01", "02", "03", "04", '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
       '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
done = False
while done != True:
    try:
        date = input("Enter a date: ")
        # If the user inputs the date like 9/8/2023
        if "/" in date:
            date = date.strip()
            mm, dd, yyyy = date.split("/")
            if int(dd) > 31:
                raise ValueError
            if int(mm) < 10:
                mm = ("0" + str(mm))
            if int(mm) < 13 and int(dd) < 31:
                if int(dd) < 10:
                    dd = day[int(dd) - 1]
                print(f"{yyyy}-{mm}-{(dd)}")
                done = True
                exit()
                break
            else:
                raise ValueError
        elif "," in date:
            # If the user types the date like September 8, 2024
            mmdd, yyyy = date.split(", ")
            mm, dd = mmdd.split(" ")
            if int(dd) > 31:
                raise ValueError

            if mm in month:
                if str(mm) == "January":
                    mm = "01"
                if str(mm) == "February":
                    mm = "02"
                if str(mm) == "March":
                    mm = "03"
                if str(mm) == "April":
                    mm = "04"
                if str(mm) == "May":
                    mm == "05"
                if str(mm) == "June":
                    mm == "06"
                if str(mm) == "July":
                    mm == "07"
                if str(mm) == "August":
                    mm == "08"
                if str(mm)== "September":
                    mm = "09"
                if str(mm) == "October":
                    mm = "10"
                if str(mm) == "November":
                    mm = "11"
                if str(mm) == "December":
                    mm = "12"
            if int(mm) < 10:
                if int(dd) < 10:
                    dd = day[int(dd) -1]
            print(f"{yyyy}-{mm}-{day[int(dd) -1]}")
            done = True
            exit()
            break

    except ValueError:
        pass
