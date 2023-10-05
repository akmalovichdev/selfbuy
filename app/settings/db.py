import datetime
import mysql.connector
from aiogram.types import User
import requests
import configs

def connect():
    try:
        conn = mysql.connector.connect(
            host=configs.mysqlHost,
            user=configs.mysqlUser,
            password=configs.mysqlPassword,
            database=configs.mysqlDatabase
        )
        return conn
    except Exception as error:
        print("Ошибка подключения к базе данных: {}".format(error))
        return None

#########################################################################################################################################################################

def getNowDate():
    date = datetime.datetime.today().strftime("%Y-%m-%d")
    return date

def getNowDateTime():
    date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    return date

def getUsersExist(user_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f"SELECT userId FROM users WHERE userId = '{user_id}'")
    if cursor.fetchone() is None:
        return False
    else:
        return True

def getAllUsers():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f"""SELECT userId FROM users""")
    row = cursor.fetchall()
    return row
    
#########################################################################################################################################################################

def addUser(user_id, userName):
    conn = connect()
    cursor = conn.cursor(buffered=True)

    user = [user_id, userName, getNowDate()]
    cursor.execute(f'''INSERT INTO users(userId, userName, joinDate) VALUES(%s,%s,%s)''', user)
    conn.commit()

def addPurchase(message, data, type):
    conn = connect()
    cursor = conn.cursor(buffered=True)

    if type == 'questions':
        user = [message.from_user.id, data['productLink'], data['purchaseCount'], data['purchasePurpose'], data['isProductRetrievalPlanned'], data['cityForPurchase'], data['purchaseAlgorithm'], data['isBuyerRetrievalNeeded'], data['isReviewNeeded'], getNowDate()]
        cursor.execute(f'''INSERT INTO `purchases`(`userId`, `productLink`, `purchaseCount`, `purchasePurpose`, `isProductRetrievalPlanned`, `cityForPurchase`, `purchaseAlgorithm`, `isBuyerRetrievalNeeded`, `isReviewNeeded`, `createDate`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', user)
        id_of_new_row = cursor.lastrowid
    elif type == 'distribution':
        user = [message.from_user.id, data['productLink'], data['cashback'], data['algoritm'], data['cashbackDay'], getNowDate()]
        cursor.execute(f'''INSERT INTO `distribution`(`userId`, `productLink`, `cashback`, `algoritm`, `cashbackDay`, `createDate`) VALUES(%s,%s,%s,%s,%s,%s)''', user)
        id_of_new_row = cursor.lastrowid

    conn.commit()

    return id_of_new_row

#########################################################################################################################################################################

def select(fields, fields2, table, select):
    conn = connect()
    try:
        cursor = conn.cursor(buffered=True)
        cursor.execute(f"""SELECT {select} FROM {table} WHERE {fields} = '{fields2}'""")
        result = cursor.fetchone()
        row = str(result[0])
        return row
    except:
        return False
    
def selectConf(conf):
    conn = connect()
    cursor = conn.cursor(buffered=True)

    cursor.execute(f"""SELECT meaning FROM config WHERE name = '{conf}'""")
    result = cursor.fetchone()
    row = str(result[0])
    return row

#########################################################################################################################################################################

def updatepurchase(id, type):
    conn = connect()
    cursor = conn.cursor()
    if type == 'questions':
        cursor.execute(f'''UPDATE purchases SET isActive = True WHERE id = {id}''')
    elif type == 'distribution':
        cursor.execute(f'''UPDATE distribution SET isActive = True WHERE id = {id}''')

    conn.commit()
    