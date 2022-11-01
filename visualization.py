import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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
ORDER BY four_g DESC
'''

query_3 = '''
SELECT id, battery_power, clock_Speed
FROM features
WHERE battery_power > 1400
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:

    # Load data
    print ("Database opened successfully")
    cur = conn.cursor()
    print('1.  \n')

    cur.execute(query_1)
    df_1 = pd.DataFrame(cur.fetchall(), columns=['id', 'mobile_wt'])
    print(df_1)

    print('2.  \n')

    cur.execute(query_2)
    df_2 = pd.DataFrame(cur.fetchall(), columns=['id', 'four_g'])
    print(df_2)

    print('3.  \n')

    cur.execute(query_3)
    df_3 = pd.DataFrame(cur.fetchall(), columns=['id', 'battery_power', 'clock_Speed'])
    print(df_3)

    # Visualization
    fig, axs = plt.subplots(3, figsize=(10, 10))

    # Query 1 - Histogram
    axs[0].bar(df_1['id'], df_1['mobile_wt'])

    axs[0].set_xticks(list(range(df_1['id'].min(), df_1['id'].max() + 1)))
    axs[0].set_yticks(list(range(0, df_1['mobile_wt'].max() + 10, 5)))

    axs[0].set_ylim(df_1['mobile_wt'].min() - 10, df_1['mobile_wt'].max() + 10)

    axs[0].set_xlabel('id')
    axs[0].set_ylabel('Mobile Weight')
    axs[0].set_title('Query 1')

    axs[0].grid(axis='y')

    chartBox = axs[0].get_position()
    axs[0].set_position([chartBox.x0, chartBox.y0,
                         chartBox.width * 0.6,
                         chartBox.height])

    # Query 2 - Pie Diagram

    labels = ['Have 4G', 'Don\'t have 4G']
    sizes = df_2['four_g'].value_counts().values

    axs[1].pie(sizes, labels=labels, autopct='%1.1f%%')

    axs[1].set_title('Query 2')

    chartBox = axs[1].get_position()
    axs[1].set_position([chartBox.x0 + 0.2, chartBox.y0,
                         chartBox.width * 2,
                         chartBox.height * 2])

    # Query 3 - Scatter

    axs[2].scatter(df_3['battery_power'], df_3['clock_Speed'])

    def my_range(x, y, jump):
        while x < y:
            yield x
            x += jump

    axs[2].set_yticks(list(my_range(int(df_3['clock_Speed'].min()), int(df_3['clock_Speed'].max() + 2), 0.5)))

    axs[2].set_xlabel('Battery Power')
    axs[2].set_ylabel('Clock Speed')
    axs[2].set_title('Query 3')

    axs[2].grid()

    chartBox = axs[2].get_position()
    axs[2].set_position([chartBox.x0, chartBox.y0 + 0.15,
                         chartBox.width * 0.6,
                         chartBox.height])

    plt.show()

