#Lookup Agenda

import sys
import pandas as pd
from db_table import db_table
import sqlite3
from import_agenda import database

def nicely_print(rows):
    #rows is a list of dictionaries
    for item in rows:
        print(f'Date: {item["date"]} \t Start Time: {item["start_time"]} \t End Time: {item["end_time"]} \t Session or Subsession: {item["session_type"]} \t Session Title: {item["title"]} \t Room Location: {item["location"]} \t Description: {item["description"]} \t Speaker(s): {item["speakers"]}')
        print("\n")


def is_subsesion(db, id):
    row = db.select(where={"id":id}) #row in list form
    if row[0]["session_type"] == "Sub":
        return True


def lookup(db, col, val):
    speakers_dict = dict()
    correct_ids = []
    if col == "speakers":
        for name in db.select():
            if name["speakers"] != "":
                speakers_dict[name["id"]] = name["speakers"].split("; ")
            #if it is empty do nothing

        #now we have a list of everything that has speakers attached to their id
        for id, speakers in speakers_dict.items():
            next_id = id + 1
            #print("ID : ", id, "SPEakerS: ", speakers)
            if val in speakers:
                correct_ids.append(id)


    else: #not speakers
        id_list = db.select(columns = ["id"], where={col:val.replace("'", " ")})
        for item in id_list:
            correct_ids.append(item["id"])


    for id in correct_ids:
        current_row = db.select(where={"id":id})[0] #this gives the row of the id you are looking at in the form of a dictionary
        if current_row["session_type"] == "Session":
            next_id = id + 1
            while(is_subsesion(db, next_id)):
                correct_ids.append(next_id)
                next_id += 1

    correct_ids.sort()
    for id in correct_ids:
        nicely_print(db.select(columns = ["date", "start_time", "end_time", "session_type", "title", "location", "description", "speakers"], where={"id":id}))
    #return db.select(columns = ["date", "start_time", "end_time", "session_type", "title", "location", "description", "speakers"], where = {col:val})


def main():
    column, value_mult = sys.argv[1], sys.argv[2:]
    value = " ".join(value_mult)

    lookup(database, column, value)


if __name__ == '__main__':
    main()
