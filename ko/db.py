from typing import List

import oracledb

from ko.config import CONFIG
from ko.model import User

def get_connection() -> oracledb.Connection:
    user = CONFIG.DB_USER
    pwd = CONFIG.DB_PASSWORD
    host = CONFIG.DB_HOST
    print(user, pwd, host)
    return oracledb.connect(user=user, password=pwd, host=host, port=1521, service_name="XEPDB1")

def insert_user(user: User):
    sql = 'insert into ross.users(user_name) values(:user_name)'

    try:
        with get_connection() as con:
            with con.cursor() as cursor:
                cursor.execute(sql, user_name=user.user_name)
                con.commit()
    except oracledb.Error as error:
        print("Oracle error:")
        print(error)

def get_users():
    sql = 'select * from ross.users'
    try:
        with get_connection() as con:
            with con.cursor() as cursor:
                users = [row for row in cursor.execute(sql)]
                return users
    except oracledb.Error as error:
        print("Oracle error:")
        print(error)

def clear_users():
    sql = 'delete from ross.users'
    try:
        with get_connection() as con:
            with con.cursor() as cursor:
                cursor.execute(sql)
                con.commit()
    except oracledb.Error as error:
        print("Oracle error:")
        print(error)