def switch_case (arguement):
    switcher ={
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
    }
    return switcher.get(arguement, "invalid days")

    Day = 3
    print (switch_case, {Day})