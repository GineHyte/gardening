from pymysql import connect, cursors

from app.core.utils import Singleton
from app.core.config import settings

class DBConnection(metaclass=Singleton):
    """
    Manages a singleton database connection using pymysql.

    This class ensures that only one database connection is active at any given time.
    It provides methods for reading and writing data to the database.
    """
    instance: "DBConnection" = None
    connection: connect = None

    def __init__(self):
        """Initializes a new database connection using pymysql.

        The connection parameters are retrieved from the application's configuration.
        These parameters include the database host, port, username, password, and database name.
        """
        self.connection = connect(
            host=settings.DB_HOST,
            user=settings.DB_USER,
            password=settings.DB_PASS,
            database=settings.DB_DATABASE,
            cursorclass=cursors.DictCursor
        )
        self.cursor = self.connection.cursor()

    def read_once(self, query: str, params: tuple = ()): 
        """
        Executes a given SQL query and returns a single row from the result set.

        Args:
            query: The SQL query string to execute.
            params: A tuple of parameters to substitute into the query.
        Returns:
            A single row from the query result, or None if no rows are found.
        """
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def read_all(self, query: str, params: tuple = ()): 
        """
        Executes a given SQL query and returns all rows from the result set.

        Args:
            query: The SQL query string to execute.
            params: A tuple of parameters to substitute into the query.
        Returns:
            A list of all rows from the query result.
        """
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def write_query(self, query: str, params: tuple = ()): 
        """
        Executes a given SQL query that modifies the database (e.g., INSERT, UPDATE, DELETE).
        Commits the transaction after execution.

        Args:
            query: The SQL query string to execute.
            params: A tuple of parameters to substitute into the query.
        """
        self.cursor.execute(query, params)
        self.connection.commit()

    def test(self):
        """
        Tests the database connection by executing a simple query.
        Returns:
            The result of the test query.
        """
        self.cursor.execute("SELECT 1")
        return self.cursor.fetchone()

    def close(self):
        """
        Closes the database connection and cursor.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            self.connection = None
            self.cursor = None
            DBConnection.instance = None