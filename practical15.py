import sqlite3
conn = sqlite3.connect('bank.db')
conn.execute('''CREATE TABLE IF NOT EXISTS Bank
 (AccountNo INT PRIMARY KEY NOT NULL,
CustomerName TEXT NOT NULL,
 Balance REAL NOT NULL,
 Phone TEXT,
 Address TEXT);''')
 
def insert_record(AccountNo, CustomerName, Balance, Phone, Address):
    conn.execute(f"INSERT INTO Bank (AccountNo, CustomerName, Balance, 
    Phone, Address) \
    VALUES ({AccountNo}, '{CustomerName}', {Balance}, 
    '{Phone}', '{Address}');")
    conn.commit()
def update_record(AccountNo, field, value):
    conn.execute(f"UPDATE Bank SET {field} = '{value}' WHERE AccountNo = 
    {AccountNo};")
    conn.commit()
def delete_record(AccountNo):
    conn.execute(f"DELETE FROM Bank WHERE AccountNo = {AccountNo};")
    conn.commit()
    insert_record(1001, 'Kumar', 15000.0, '190303105339', 'Vadodara')
    insert_record(1002, 'Deepak Kumar', 25000.0, '190303105591', 'Ahemdhabad')
    insert_record(1003, 'Vinu', 35000.0, '19030310539', 'Kakinada')
    update_record(1001, 'Balance', 20000.0)

    delete_record(1003)
    cursor = conn.execute('SELECT CustomerName, Balance FROM Bank 
    WHERE Balance > 20000')
    for row in cursor:
        print(f"{row[0]} has a balance of {row[1]}")
        conn.close()