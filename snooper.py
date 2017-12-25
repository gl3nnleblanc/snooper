import fileinput, sqlite3

# set up table and cursor
db = 'example.db'
conn = sqlite3.connect(db)
c = conn.cursor()
try:
    c.execute("CREATE TABLE snoops (time, host, site)")
    print("Created new table snoops in", db)
except sqlite3.OperationalError:
    print("Table already exists; adding on.")

# read through text input and insert into table
for line in fileinput.input():
    try:
        # convert line into tuple for insertion into table
        line = tuple((line.split(',')))
        if len(line) != 3 or 'Request' in line[1] or 'Reply ' in line[1]:
            pass
        else:
            c.execute('INSERT INTO snoops VALUES (?,?,?);', line)
            conn.commit()
    except Exception as e:
        print(e)
        print('Error in input:')
        print(line)
