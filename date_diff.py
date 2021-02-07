import json
import datetime as dt

days_in_year = 365.2425 # To take into account leap years

def import_data():
    data = []
    with open("datafile.py", "r") as f:
        for line in f:
            # Assume that data validation may be skipped in this task
            (name, birthdate) = line.split("=")
            name = name.strip()
            birthdate = birthdate.split('"')[1]
            (byear, bmonth, bday) = map(int, birthdate.split("-"))
            age = int((dt.date.today() - dt.date(byear, bmonth, bday)).days / days_in_year)
#            data = data + [(name, byear, bmonth, bday, age)]
            data.append((name, byear, bmonth, bday, age))
    data.sort(key=lambda e: f"{e[1]}{e[2]}{e[3]}")
    return data

def prepare_json(data):
    data_json = {}
    (name, byear, bmonth, bday, age) = data[-1]  # the Youngest
    youngest_bdate = dt.date(byear, bmonth, bday)
    today_date = dt.date.today()
    for name, byear, bmonth, bday, age in data:
        emp_bdate = dt.date(byear, bmonth, bday)
        emp_days = (today_date - emp_bdate).days
        age_since_youngest = int((youngest_bdate - emp_bdate).days / days_in_year)
        #print(f"{name:25} {emp_days:6} {age_since_youngest:3}")
        data_json[name] = {"Age in days":emp_days, "Age since youngest":age_since_youngest}
    return data_json

def main():
    data = import_data()
    print(f"{'Age'}  {'Name':25} Birthday")
    for name, byear, bmonth, bday, age in data:
        print(f"{age:3}  {name:25} {bday:02}.{bmonth:02}.{byear}")
        
    data_json = prepare_json(data)
    with open('datafile.json', 'w') as write_file:
        json.dump(data_json, write_file, ensure_ascii=False, indent=4)
        write_file.write('\n')

if __name__ == "__main__":
    # execute only if run as a script
    #print(dt.datetime.now().strftime("%Y-%m-%d"))
    main()
