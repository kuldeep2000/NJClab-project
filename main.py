import sqlite3

conn = sqlite3.connect('Movies.db')
print("Database opened successfully")

conn.execute('''CREATE TABLE Movies
         (Lead_actor    TEXT    NOT NULL,
         Lead_actress   TEXT    NOT NULL,
         yor            INT     NOT NULL,
         Director_name  TEXT    NOT NULL);''')
print("Table created successfully")

conn.execute("INSERT INTO Movies (Lead_actor,Lead_actress,yor,Director_name) \
      VALUES ('RajKumar','Bhumi',2022, 'Harshwardhan')")

conn.execute("INSERT INTO Movies (Lead_actor,Lead_actress,yor,Director_name) \
      VALUES ('Ayushmann','yami',2012, 'Soorjit Sircar')")

conn.execute("INSERT INTO Movies (Lead_actor,Lead_actress,yor,Director_name) \
      VALUES ('Nawazuddin Siddiqui','Richa',2012, 'Anurag Kashyap')")

conn.execute("INSERT INTO Movies (Lead_actor,Lead_actress,yor,Director_name) \
      VALUES ('Pankaj Tripathi','Monal Gajjar',2021, 'Satish Kaushik')")

conn.execute("INSERT INTO Movies (Lead_actor,Lead_actress,yor,Director_name) \
      VALUES ('Shahrukh khan','Katrina kaif',2019, 'Anand L rai')")

conn.commit()
print("Records stored successfully")

cursor = conn.execute("SELECT Lead_actor,Lead_actress,yor,Director_name from Movies")
for row in cursor:
   print ("Lead_actor = ", row[0])
   print("Lead_actress = ", row[1])
   print("yor = ", row[2])
   print("Director_name = ", row[3], "\n")

print("Displayed successfully")

conn.close()