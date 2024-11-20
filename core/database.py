import os
import sqlite3

class DatabaseManager:
    """
    Manages interactions with the SQLite database for emergency contacts.
    """
    def __init__(self, db_path="assets/data/contacts.db"):
        self.db_path = db_path
        self.connection = None
        self.ensure_directory_exists()
        self.initialize_database()

    def ensure_directory_exists(self):
        """
        Ensures that the directory for the database file exists.
        """
        directory = os.path.dirname(self.db_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

    def connect(self):
        """
        Establishes a connection to the database.
        """
        if not self.connection:
            self.connection = sqlite3.connect(self.db_path)

    def close(self):
        """
        Closes the connection to the database.
        """
        if self.connection:
            self.connection.close()
            self.connection = None

    def initialize_database(self):
        """
        Creates the contacts table if it does not exist.
        """
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            country TEXT NOT NULL,
            police TEXT,
            fire TEXT,
            ambulance TEXT
        )
        """)
        self.connection.commit()
        self.close()

    def fetch_contacts(self, country=None):
        """
        Fetches emergency contacts, filtered by country if specified.

        :param country: Country name to filter contacts.
        :return: List of tuples containing contact details.
        """
        self.connect()
        cursor = self.connection.cursor()
        if country:
            cursor.execute("SELECT * FROM contacts WHERE country = ?", (country,))
        else:
            cursor.execute("SELECT * FROM contacts")
        results = cursor.fetchall()
        self.close()
        return results

    def add_contact(self, country, police, fire, ambulance):
        """
        Adds a new contact record to the database.

        :param country: Name of the country.
        :param police: Police contact number.
        :param fire: Fire contact number.
        :param ambulance: Ambulance contact number.
        """
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("""
        INSERT INTO contacts (country, police, fire, ambulance)
        VALUES (?, ?, ?, ?)
        """, (country, police, fire, ambulance))
        self.connection.commit()
        self.close()