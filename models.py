import sqlite3
import logging


class Schema:
    '''
    This class holds the database connections and methods
    '''
    def __init__(self):
        '''
        This method initializes the database and creates the tables if they don't already exist
        '''
        try: 
            self.conn = sqlite3.connect('syllabus_project.db')
        except sqlite3.Error as e:
            logging.ERROR(e)


    def create_login_table():
        '''
        This method will create the table of login information if it does not already exist
        '''
        pass


    def create_syllabus_files_table():
        '''
        This method will create the table of the uploaded syllabus files if it does not already exist
        '''
        pass

    def create_downloadable_calendar_table():
        '''
        This method will create the table of downloadable calendar files if it does not already exist
        '''
        pass
    

