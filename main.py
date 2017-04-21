#!/usr/bin/python

import sqlite3
import os
import glob
import shutil
import numpy


# Print current directory
print("The staring directory is...", os.getcwd())

# Change directory to where the data locates
os.chdir('/Users/PWH-Mac/Seagate/work/data/')
print("The current directory is changed to...", os.getcwd())



## Connect to a database and create a table
database = "FRC_media_DB.db"
conn = sqlite3.connect('%s' % database)
print("Opened database successfully")

# Create a table in the database
table = 'PSG_4BL_20170420'
conn.execute('create table if not exists ' + table + '(' +
                '[media id] char(50) primary key not null,' +
                'BL1         real,' +
                'BL2         real,' +
                'BL3         real,' +
                'BL4         real,' +
                '[M1-Hk]     real,' +
                '[M5-Hk]     real,' +
                '[M5-Hex]    real,' +
                'Hc        real,' +
                '[SFD%]    real,' +
                'ClusterSz real);')

print("Table created successfully")
conn.close()



## Loop over folders and record data
os.chdir('20170420_PMR_4BL')
print("The current directory is changed to...", os.getcwd())

folders_iter = glob.glob("_*")
count = 0

# Input fields
BL1   =  []
BL2   =  []
BL3   =  []
BL4   =  []
M1_Hk =  []
M5_Hk =  []
M5_Hex = []

# Output fields
Hc =       []
SFD_perc = []
clustSz =  []

for folder in folders_iter:
    count += 1
    os.chdir(os.path.join(os.getcwd(), folder))
    print(os.getcwd(), "....", count, "th folder")
    f_ptr0 = open("Config.dat")
    lines = f_ptr0.readlines()
    BL1.append(float(lines[80][0:5]))
    BL2.append(float(lines[91][0:5]))
    BL3.append(float(lines[102][0:5]))
    BL4.append(float(lines[113][0:5]))
    M1_Hk.append(float(lines[189][0:10]))
    M5_Hk.append(float(lines[193][0:10]))
    M5_Hex.append( float(lines[121][0:5]) )
    f_ptr0.close()

    f_ptr1 = open("output.out")
    lines1 = f_ptr1.readlines()
    Hc.append(float(lines1[4][11:20]))
    SFD_perc.append(float(lines1[3][8:15]))
    clustSz.append(float(lines1[7][16:23]))
    f_ptr1.close()

    os.chdir("..")

print("Looped for", count, "folders!")

print("The current directory is...", os.getcwd())


## Connect to a database and inserts fields into a table
os.chdir("..")
print("The directory is changed to...", os.getcwd())
conn = sqlite3.connect('%s' % database)
print("Opened database successfully")
table = 'PSG_4BL_20170420'

str_tmp = ""
for i in range(0, len(BL1)):

    print(i)
    if i < 10:
        id_record = (str_tmp+'000000'+str(i))
    elif (i>=10 and i<100):
        id_record = (str_tmp+'00000'+str(i))
    elif (i>=100 and i<1000):
        id_record = (str_tmp+'0000'+str(i))
    elif (i>=1000 and i<10000):
        id_record = (str_tmp+'000'+str(i))
    elif (i>=10000 and i<100000):
        id_record = (str_tmp+'00'+str(i))
    elif (i>=100000 and i<1000000):
        id_record = (str_tmp+'0'+str(i))
    elif (i>=1000000 and i<10000000):
        id_record = (str_tmp+str(i))
    else:
        print("Exceed maximum table size")

    conn.execute("insert into %s \
                    values (?,  \
                    ?, ?, ?, ?, \
                    ?, ?,        \
                    ?,            \
                    ?, ?, ?)" % table,
                    (id_record,
                     BL1[i], BL2[i], BL3[i], BL4[i],
                     M1_Hk[i], M5_Hk[i],
                     M5_Hex[i],
                     Hc[i], SFD_perc[i], clustSz[i]))

print("Records created successfully in table " + table)

conn.commit()

conn.close()