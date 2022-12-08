# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

import sqlite3
from sqlite3 import Error
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "get_user_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn= create_connection("database.db")
        name=tracker.get_slot("name")
        number=tracker.get_slot("number")
        email=tracker.get_slot("email")
        if name is not None:
            if number is not None:
                if email is not None:
                    cur = conn.cursor()
                    cur.execute(f"""INSERT INTO Customer(Name,Contact,Email) VALUES(?,?,?);""",(name,number,email))
                    conn.commit()
                    #select_all_tasks(conn,name,number,email)
        return []

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

# def select_all_tasks(conn,name,number,email):

#     cur = conn.cursor()
#     cur.execute("""INSERT INTO Customer (Name,Contact,Email) VALUES(name,number,email);""")

#     conn.commit()
#     rows = cur.fetchall()

#     for row in rows:
#         print(row)



