import psycopg2

username = 'postgres'
password = '133451' # root
database = 'mobiles'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT id, mobile_wt
FROM dimensions
WHERE mobile_wt > 150;
'''
query_2 = '''
SELECT id, four_g
FROM connections
WHERE four_g IS TRUE
'''

query_3 = '''
SELECT id, battery_power, clock_Speed
FROM features
WHERE battery_power > 1400
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:

    print ("Database opened successfully")
    cur = conn.cursor()
    print('1.  \n')

    cur.execute(query_1)

    for row in cur:
        print(row)

    print('2.  \n')

    cur.execute(query_2)

    for row in cur:
        print(row)

    print('3.  \n')

    cur.execute(query_3)

    for row in cur:
        print(row)
