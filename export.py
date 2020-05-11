import csv
import cx_Oracle

username = 'Maya'
password = 'Maya'
databaseName = 'localhost/xe'

connection = cx_Oracle.connect(username,password,databaseName)
cursor = connection.cursor()

tables = ['Game', 'Genre', 'Publisher', 'Region','Sales']

for table in tables:
    with open(table + '.csv', 'w', newline='') as csv_file:
        query = 'SELECT * FROM ' + table
        cursor.execute(query)
        row = cursor.fetchone()

        title = tuple(map(lambda x: x[0], cursor.description))
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(title)


        while row:
            csv_writer.writerow(row)
            row = cursor.fetchone()

cursor.close()
connection.close()