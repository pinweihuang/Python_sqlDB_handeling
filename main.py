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
                          'BL5         real,' +
                          '[M1-thk]    real,' +
                          '[M2-thk]    real,' +
                          '[M3-thk]    real,' +
                          '[M4-thk]    real,' +
                          '[M5-thk]    real,' +
                          '[M6-thk]    real,' +
                          '[M1-Ms]     real,' +
                          '[M2-Ms]     real,' +
                          '[M3-Ms]     real,' +
                          '[M4-Ms]     real,' +
                          '[M5-Ms]     real,' +
                          '[M6-Ms]     real,' +
                          '[M1-Hex]    real,' +
                          '[M2-Hex]    real,' +
                          '[M3-Hex]    real,' +
                          '[M4-Hex]    real,' +
                          '[M5-Hex]    real,' +
                          '[M6-Hex]    real,' +
                          '[M1-Hk]     real,' +
                          '[M2-Hk]     real,' +
                          '[M3-Hk]     real,' +
                          '[M4-Hk]     real,' +
                          '[M5-Hk]     real,' +
                          '[M6-Hk]     real,' +
                          '[M1-sigHk]  real,' +
                          '[M2-sigHk]  real,' +
                          '[M3-sigHk]  real,' +
                          '[M4-sigHk]  real,' +
                          '[M5-sigHk]  real,' +
                          '[M6-sigHk]  real,' +
                          '[M1-Ha-magn] real,' +
                          '[M2-Ha-magn] real,' +
                          '[M3-Ha-magn] real,' +
                          '[M4-Ha-magn] real,' +
                          '[M5-Ha-magn] real,' +
                          '[M6-Ha-magn] real,' +
                          '[M1-Ha-theta] real,' +
                          '[M2-Ha-theta] real,' +
                          '[M3-Ha-theta] real,' +
                          '[M4-Ha-theta] real,' +
                          '[M5-Ha-theta] real,' +
                          '[M6-Ha-theta] real,' +
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
BL5   =  []
mNz1  =  []
mNz12 =  []
mNz2  =  []
mNz23 =  []
mNz3  =  []
mNz34 =  []
mNz4  =  []
mNz45 =  []
mNz5  =  []
mNz56 =  []
mNz6  =  []
M1_Ms =  []
M2_Ms =  []
M3_Ms =  []
M4_Ms =  []
M5_Ms =  []
M6_Ms =  []
M1_Hex =  []
M2_Hex =  []
M3_Hex =  []
M4_Hex =  []
M5_Hex = []
M6_Hex = []
M1_Hk =     []
M1_sigHk =  []
M2_Hk =     []
M2_sigHk =  []
M3_Hk =     []
M3_sigHk =  []
M4_Hk =     []
M4_sigHk =  []
M5_Hk =    []
M5_sigHk = []
M6_Hk =    []
M6_sigHk = []
M1_Ha_magn = []
M2_Ha_magn = []
M3_Ha_magn = []
M4_Ha_magn = []
M5_Ha_magn = []
M6_Ha_magn = []
M1_Ha_theta = []
M2_Ha_theta = []
M3_Ha_theta = []
M4_Ha_theta = []
M5_Ha_theta = []
M6_Ha_theta = []

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

    BL1.append( float(lines[80][0:5]) )
    BL2.append( float(lines[91][0:5]) )
    BL3.append( float(lines[102][0:5]) )
    BL4.append( float(lines[113][0:5]) )
    BL5.append( float(lines[124][0:5]) )

    mNz1.append( int(lines[176][0:2]))
    mNz12.append(int(lines[177][0:2]))
    mNz2.append( int(lines[178][0:2]))
    mNz23.append(int(lines[179][0:2]))
    mNz3.append( int(lines[180][0:2]))
    mNz34.append(int(lines[181][0:2]))
    mNz4.append( int(lines[182][0:2]))
    mNz45.append(int(lines[183][0:2]))
    mNz5.append( int(lines[184][0:2]))
    mNz56.append(int(lines[185][0:2]))
    mNz6.append( int(lines[186][0:2]))
    
    M1_Ms.append( float(lines[74][0:5]) )
    M2_Ms.append( float(lines[85][0:5]) )
    M3_Ms.append( float(lines[96][0:5]) )
    M4_Ms.append( float(lines[107][0:5]) )
    M5_Ms.append( float(lines[118][0:5]) )
    M6_Ms.append( float(lines[129][0:5]) )
    
    M1_Hex.append( float(lines[77][0:5]) )
    M2_Hex.append( float(lines[88][0:5]) )
    M3_Hex.append( float(lines[99][0:5]) )
    M4_Hex.append( float(lines[110][0:5]) )
    M5_Hex.append( float(lines[121][0:5]) )
    M6_Hex.append( float(lines[132][0:5]) )
    
    M1_Hk.append( float(lines[189][0:10]) )
    M2_Hk.append( float(lines[190][0:10]) )
    M3_Hk.append( float(lines[191][0:10]) )
    M4_Hk.append( float(lines[192][0:10]) )
    M5_Hk.append( float(lines[193][0:10]) )
    M6_Hk.append( float(lines[194][0:10]) )
    
    M1_sigHk.append( float(lines[78][0:5]) )
    M2_sigHk.append( float(lines[89][0:5]) )
    M3_sigHk.append( float(lines[100][0:5]) )
    M4_sigHk.append( float(lines[111][0:5]) )
    M5_sigHk.append( float(lines[122][0:5]) )
    M6_sigHk.append( float(lines[133][0:5]) )
    
    M1_Ha_magn.append( float(lines[50][0:5]) )
    M2_Ha_magn.append( float(lines[54][0:5]) )
    M3_Ha_magn.append( float(lines[58][0:5]) )
    M4_Ha_magn.append( float(lines[62][0:5]) )
    M5_Ha_magn.append( float(lines[66][0:5]) )
    M6_Ha_magn.append( float(lines[70][0:5]) )
    
    M1_Ha_theta.append( float(lines[51][0:5]) )
    M2_Ha_theta.append( float(lines[55][0:5]) )
    M3_Ha_theta.append( float(lines[59][0:5]) )
    M4_Ha_theta.append( float(lines[63][0:5]) )
    M5_Ha_theta.append( float(lines[67][0:5]) )
    M6_Ha_theta.append( float(lines[71][0:5]) )
    f_ptr0.close()

    f_ptr1 = open("output.out")
    lines1 = f_ptr1.readlines()
    Hc.append(float(lines1[4][11:20]))
    SFD_perc.append(float(lines1[3][8:15]))
    clustSz.append(float(lines1[7][16:23]))
    f_ptr1.close()

    os.chdir("..")

mNz1 = mNz1
mNz2 = (numpy.subtract(mNz2, mNz12))
mNz3 = (numpy.subtract(mNz3, mNz23))
mNz4 = (numpy.subtract(mNz4, mNz34))
mNz5 = (numpy.subtract(mNz5, mNz45))
mNz6 = (numpy.subtract(mNz6, mNz56))

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
                    values (?, \
                            ?, ?, ?, ?, ?, \
                            ?, ?, ?, ?, ?, ?, \
                            ?, ?, ?, ?, ?, ?, \
                            ?, ?, ?, ?, ?, ?, \
                            ?, ?, ?, ?, ?, ?, \
                            ?, ?, ?, ?, ?, ?, \
                            ?, ?, ?, ?, ?, ?, \
                            ?, ?, ?, ?, ?, ?, \
                            ?, ?, ?)" % table,
                    (id_record,
                     BL1[i],         BL2[i],         BL3[i],         BL4[i],        BL5[i],
                     mNz1[i],        mNz2[i],        mNz3[i],        mNz4[i],        mNz5[i],        mNz6[i],
                     M1_Ms[i],       M2_Ms[i],       M3_Ms[i],       M4_Ms[i],       M5_Ms[i],       M6_Ms[i],
                     M1_Hex[i],      M2_Hex[i],      M3_Hex[i],      M4_Hex[i],      M5_Hex[i],      M6_Hex[i],
                     M1_Hk[i],       M2_Hk[i],       M3_Hk[i],       M4_Hk[i],       M5_Hk[i],       M6_Hk[i],
                     M1_sigHk[i],    M2_sigHk[i],    M3_sigHk[i],    M4_sigHk[i],    M5_sigHk[i],    M6_sigHk[i],
                     M1_Ha_magn[i],  M2_Ha_magn[i],  M3_Ha_magn[i],  M4_Ha_magn[i],  M5_Ha_magn[i],  M6_Ha_magn[i],
                     M1_Ha_theta[i], M2_Ha_theta[i], M3_Ha_theta[i], M4_Ha_theta[i], M5_Ha_theta[i], M6_Ha_theta[i],
                     Hc[i],          SFD_perc[i],    clustSz[i]))

print("Records created successfully in table " + table)

conn.commit()

conn.close()