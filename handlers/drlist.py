def return_list():
    drs_str = "Ваши др в формате 'Name' 'date'"
    drs = []
    dr_str =""
    x = drs_str.split("\n")
    for strok in x:
        dictionary = {
        "name":str,
        "date":str
        }
        stroka = strok.split(" ")
        data = stroka[1][0:5]
        dictionary["name"] = stroka[0]
        dictionary["date"] =  data
        print(dictionary)
        drs.append(dictionary)
    return drs
