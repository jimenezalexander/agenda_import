#Import Agenda

import pandas as pd
import sys
from db_table import db_table

db_schema = {"id":"integer PRIMARY KEY", "date": "text NOT NULL", "start_time": "text NOT NULL", "end_time": "text NOT NULL", "session_type": "text NOT NULL", "title": "text NOT NULL", "location": "text", "description":"text", "speakers":"text"}
database = db_table("database", db_schema)

def open_xls(xls):
    df = pd.ExcelFile(xls)
    df = df.parse(names = ["Date","StartTime","EndTime","SessionType","SessionTitle","RoomLocation","Description","Speakers"], skiprows=14) #underscore indexes are invaled names for namedtuple
    df = df.fillna("")
    return df


def create_list(xls):
    rows = []
    for row in xls.itertuples():
        rows.append(row)
    return rows

def fill_database(rows):
    for row in rows:
        # database.insert({"date":row.Date, "start_time":row.StartTime, "end_time":row.EndTime, "session_type":row.SessionType, "session_title":row.SessionTitle, "room_location":row.RoomLocation, "description":row.Description})
        #had to replace apostrophes because they were causing problems in for sqlite execute function
        database.insert({"date":row.Date, "start_time":row.StartTime, "end_time":row.EndTime, "session_type":row.SessionType, "title":row.SessionTitle.replace("'"," "), "location":row.RoomLocation, "description":row.Description.replace("'", " "), "speakers":row.Speakers.replace("'", " ")})


def main(): #take arguments
    arg = sys.argv[1]
    xls = open_xls(arg)
    rows = create_list(xls)
    fill_database(rows)
    print("Database has now been created!")


if __name__ == '__main__':
    main()
