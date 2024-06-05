from DBUtils.PooledDB import PooledDB
import pymysql

class ConnectionManager:
    def __init__(self, host, database, user, password, pool_size=10):
        self.pool = PooledDB(
            creator=pymysql,
            maxconnections=pool_size,
            blocking=True,
            host=host,
            database=database,
            user=user,
            password=password,
            cursorclass=pymysql.cursors.DictCursor  # Set cursor class to DictCursor
        )

    def get_connection(self):
        return self.pool.connection()

    def execute_query(self, connection, query, params=None):
        cursor = connection.cursor()
        try:
            cursor.execute(query, params)
            connection.commit()
        except pymysql.MySQLError as e:
            connection.rollback()
            raise e
        finally:
            cursor.close()

    def fetch_one(self, connection, query, params=None):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query, params)
            result = cursor.fetchone()
        except pymysql.MySQLError as e:
            raise e
        finally:
            cursor.close()
        return result

    def fetch_all(self, connection, query, params=None):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query, params)
            result = cursor.fetchall()
        except pymysql.MySQLError as e:
            raise e
        finally:
            cursor.close()
        return result

    def fetch_many(self, connection, query, size, params=None):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query, params)
            result = cursor.fetchmany(size)
        except pymysql.MySQLError as e:
            raise e
        finally:
            cursor.close()
        return result

    def execute_many(self, connection, query, param_list):
        cursor = connection.cursor()
        try:
            cursor.executemany(query, param_list)
            connection.commit()
        except pymysql.MySQLError as e:
            connection.rollback()
            raise e
        finally:
            cursor.close()
