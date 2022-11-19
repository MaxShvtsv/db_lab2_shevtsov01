import psycopg2

username = 'postgres'
password = '133451' # root
database = 'mobiles'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT phone_id, label, int_memory
FROM phones
'''
query_2 = '''
SELECT customers.country, COUNT(*) AS phone_count
FROM customers, phones
WHERE customers.phone_id = phones.phone_id
GROUP BY customers.country
'''

query_3 = '''
SELECT phones.phone_id, phones.label, customers.cust_name
FROM phones, customers
WHERE customers.phone_id = phones.phone_id AND customers.age > 20
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
