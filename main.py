import cx_Oracle
import chart_studio.plotly as py
import plotly.graph_objs as go


username = 'Maya'
password = 'Maya'
databaseName = 'localhost/xe'

connection = cx_Oracle.connect(username, password, databaseName)
cursor = connection.cursor()


#Запит 1 - вивести топ-15 ігор та суму їх продажів

query = '''
SELECT *
FROM(
SELECT
    game_name,
    SUM(to_number(sales, '9999.99')) AS suma
FROM
    sales_game
GROUP BY
    game_name
ORDER BY suma DESC)
WHERE ROWNUM<=15'''

cursor.execute(query)
game_name = []
suma = []

row = cursor.fetchone()
while row:
    game_name.append(row[0])
    suma.append(row[1])
    row = cursor.fetchone()

bar = [go.Bar(
    x=game_name,
    y=suma
)]
layout = go.Layout(
    xaxis={
        'title': "Game's name"
    },
    yaxis={
        'title': 'Global sales'
    }
)

fig = go.Figure(data=bar, layout=layout)

fig_1 = py.plot(fig, filename='Global sales')



#Запит 2 - Вивести жанр та % його популярності у порівнянні з іншими

query = '''
SELECT
    genre_name,
    ROUND((SUM(to_number(sales, '9999.99')))*100/(SELECT SUM(to_number(sales, '9999.99')) FROM sales),2) AS percent
FROM
    (SELECT *
        FROM sales_game)
GROUP BY
    genre_name
'''

cursor.execute(query)
genre_name = []
percent = []

row = cursor.fetchone()
while row:
    genre_name.append(row[0])
    percent.append(row[1])
    row = cursor.fetchone()

pie = go.Pie(labels=genre_name, values=percent)
fig_2 = py.plot([pie], filename="Genre's percent")



#Запит 3 - вивести динаміку продажів ігор кожною компанією

query = '''
SELECT
    publisher_name,
    SUM(to_number(sales, '9999.99')) AS suma
FROM
    (SELECT *
     FROM sales_game)
GROUP BY
    publisher_name
'''

cursor.execute(query)
publisher_name = []
suma = []

row = cursor.fetchone()
while row:
    publisher_name.append(row[0])
    suma.append(row[1])
    row = cursor.fetchone()

scatter = go.Scatter(
    x=publisher_name,
    y=suma,
    mode='lines+markers')

fig_3 = py.plot([scatter], filename="Publisher's sales")


connection.close()