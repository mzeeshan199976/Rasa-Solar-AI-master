# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import FollowupAction
from rasa_sdk.events import BotUttered
import sqlite3
from sqlite3 import Error

# change this to the location of your SQLite file
path_to_db = "database.db"

class ActionProductSearch(Action):
    def name(self) -> Text:
        return "action_get_user_data"
    def main():
        database = r"C:\sqlite\db\pythonsqlite.db"

        # create a database connection
        conn = create_connection(database)
        with conn:
            print("1. Query task by priority:")
            select_task_by_priority(conn, 1)

            print("2. Query all tasks")
            select_all_tasks(conn)

    def create_connection(db_file):
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
            """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn


