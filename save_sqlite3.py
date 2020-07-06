import sqlite3

conn = sqlite3.connect('top_cities.db')

c = conn.cursor()

c.execute('DROP TABLE IF EXISTS cities')
c.execute('''
    CREATE TABLE cities(
        rank integer,
        city text,
        poplation integer
    )
    ''')

c.executemany('INSERT INTO cities VALUES(:rank,:cities,:poplation)',{
    'rank3':3,'cities':'Beigin','population':123456
})

conn.commit()
c.execute('SELECT * FROM cities')
for row in c.fethall():
    print(row)

conn.close()