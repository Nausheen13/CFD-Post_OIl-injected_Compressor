import xlrd
import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy
from matplotlib.ticker import FuncFormatter
from matplotlib.ticker import PercentFormatter

plt.rcParams.update({'font.size': 10})

df_male_3mm = pd.read_excel(r'excel file with temperature data and cell id location', sheet_name= 'male_3mm')
df_male_3mm.head()
df_female_3mm = pd.read_excel(r'excel file with temperature data and cell id location', sheet_name= 'female_3mm')
df_female_3mm.head()

df_male_4mm= pd.read_excel(r'excel file with temperature data and cell id location', sheet_name= 'male_4mm')
df_male_4mm.head()
df_female_4mm= pd.read_excel(r'excel file with temperature data and cell id location', sheet_name= 'female_4mm')
df_female_4mm.head()

df_male_5mm= pd.read_excel(r'excel file with temperature data and cell id location', sheet_name= 'male_5mm')
df_male_5mm.head()
df_female_5mm= pd.read_excel(r'excel file with temperature data and cell id location', sheet_name= 'female_5mm')
df_female_5mm.head()

df_male_8mm= pd.read_excel(r'excel file with temperature data and cell id location', sheet_name= 'male_8mm')
df_male_8mm.head()
df_female_8mm= pd.read_excel(r'excel file with temperature data and cell id location', sheet_name= 'female_8mm')
df_female_8mm.head()


Tempm_3mm= df_male_3mm['Temp']
Tempf_3mm= df_female_3mm['Temp']

Tempm_4mm= df_male_4mm['Temp']
try_4mm= Tempm_4mm[Tempm_4mm<462]
Tempf_4mm= df_female_4mm['Temp']

Tempm_5mm= df_male_5mm['Temp']
try_5mm= Tempm_5mm[Tempm_5mm<430]
Tempf_5mm= df_female_5mm['Temp']

Tempm_8mm= df_male_8mm['Temp']
Tempf_8mm= df_female_8mm['Temp']

#------Male Rotor-----

factor= 8.5e-07*(1e06)
#c,d,e = plt.hist([Tempm_3mm-273,Tempm_4mm-273,Tempm_5mm-273,Tempm_8mm-273], bins=[45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145,155, 165],color=['r','mediumslateblue','thistle','slategray'],histtype='stepfilled')
#plt.plot(c)
c,d,e = plt.hist([Tempm_3mm-273,Tempm_4mm-273,Tempm_5mm-273,Tempm_8mm-273], bins=[160,170,180,190,200,210,220], weights= [factor*numpy.ones_like(Tempm_3mm),factor*numpy.ones_like(Tempm_4mm),factor*numpy.ones_like(Tempm_5mm),factor*numpy.ones_like(Tempm_8mm)], color=['r','mediumslateblue','thistle','slategray'],histtype='stepfilled')

plt.setp(e[0], edgecolor='black', lw=2, fill= False, label= '3mm')
plt.setp(e[1], edgecolor='mediumslateblue', fill= False, lw=2, label= '4mm', hatch= "..")
plt.setp(e[2], edgecolor='firebrick', lw=2, label= '5mm', fill= False, hatch= "//")
plt.setp(e[3], edgecolor='slategray', lw=2, label= '8mm', alpha= 0.3)

plt.axvline((224), color= 'black', linestyle='--', linewidth=1)
plt.axvline((210), color='mediumslateblue', linestyle='--', linewidth=1)
plt.axvline((Tempm_5mm.max()-273), color= 'firebrick', linestyle='--', linewidth=1)
plt.axvline((Tempm_8mm.max()-273), color='slategray', linestyle='--', linewidth=1)

plt.legend()

plt.title('Male rotor surface temperature')
plt.xlabel('Surface Temperature (in C)')
plt.ylabel('No of Faces')
 
plt.xticks([30, 40,50, 60, 70, 80, 90, 100, 110, 120, 130, 140,150, 160, 170, 180, 190, 200, 210, 220, 230])
# Create names
plt.xlim(30, 230)
plt.ylim(0, 30000)

plt.savefig('./alltemp_Male_1.pdf',format='pdf')

#------Female Rotor-----

c,d,e = plt.hist([Tempf_3mm-273,Tempf_4mm-273,Tempf_5mm-273,Tempf_8mm-273], bins=[45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145,155, 165],color=['r','mediumslateblue','thistle','slategray'],histtype='stepfilled')
#plt.plot(c)
c,d,e = plt.hist([Tempf_3mm-273,Tempf_4mm-273,Tempf_5mm-273,Tempf_8mm-273], bins=[100, 110, 120, 130,140, 150,160,170,180,190,200,210,220],color=['r','mediumslateblue','thistle','slategray'],histtype='stepfilled')

plt.setp(e[0], edgecolor='black', lw=2, fill= False, label= '3mm')
plt.setp(e[1], edgecolor='mediumslateblue', fill= False, lw=2, label= '4mm', hatch= "..")
plt.setp(e[2], edgecolor='firebrick', lw=2, label= '5mm', fill= False, hatch= "//")
plt.setp(e[3], edgecolor='slategray', lw=2, label= '8mm', alpha= 0.3)

plt.axvline((Tempf_3mm.max()-273), color= 'black', linestyle='--', linewidth=1)
plt.axvline((Tempf_4mm.max()-273), color='mediumslateblue', linestyle='--', linewidth=1)
plt.axvline((Tempf_5mm.max()-273), color= 'firebrick', linestyle='--', linewidth=1)
plt.axvline((Tempf_8mm.max()-273), color='slategray', linestyle='--', linewidth=1)

plt.legend()

plt.title('Female rotor surface temperature')
plt.xlabel('Surface Temperature (in C)')
plt.ylabel('No of Faces')
 
plt.xticks([30,40,50, 60, 70, 80, 90, 100, 110, 120, 130, 140,150, 160, 170])
# Create names
plt.xlim(30, 170)
plt.ylim(0, 30000)

plt.savefig('./alltemp_Female.pdf',format='pdf')

#-------Subplot------------Male---------------------
c,d,e = plt.hist([Tempm_3mm-273,try_4mm-273,try_5mm-273,Tempm_8mm-273], bins=[100,110,120,130,140,150, 160,170,180,190,200,210,220], weights= [factor*numpy.ones_like(Tempm_3mm),factor*numpy.ones_like(try_4mm),factor*numpy.ones_like(try_5mm),factor*numpy.ones_like(Tempm_8mm)], color=['r','mediumslateblue','thistle','slategray'],histtype='stepfilled')

Tempm_3mm[np.abs(Tempm_3mm) >373].count()
Tempm_4mm[(np.abs(Tempm_4mm) >373) & (np.abs(Tempm_4mm) <462) ].count()
Tempm_5mm[np.abs(Tempm_5mm) >373].count()
Tempm_8mm[np.abs(Tempm_8mm) >373].count()

plt.setp(e[0], edgecolor='black', lw=2, fill= False, label= '3mm')
plt.setp(e[1], edgecolor='mediumslateblue', fill= False, lw=2, label= '4mm', hatch= "...")
plt.setp(e[2], edgecolor='firebrick', lw=2, label= '5mm', fill= False, hatch= "//")
plt.setp(e[3], edgecolor='slategray', lw=2, label= '8mm', alpha= 0.3)

plt.legend()

plt.title('Male rotor surface temperature>100 degC')
plt.xlabel('Surface Temperature (in C)')
plt.ylabel('Male Rotor Surface Area ($mm^2$)')
plt.yticks([0,250,500,750, 1000,1250,1500,1750,2000,2250])

plt.ylim(0, 2000)
plt.xlim(100, 225)

plt.savefig('./Subtemp_SA_Male_1.pdf',format='pdf')

#-------Subplot------------Female---------------------
c,d,e = plt.hist([Tempf_3mm-273,Tempf_4mm-273,Tempf_5mm-273,Tempf_8mm-273], bins=[100, 110, 120, 130,140, 150,160,170,180,190,200,210,220], weights= [factor*numpy.ones_like(Tempf_3mm),factor*numpy.ones_like(Tempf_4mm),factor*numpy.ones_like(Tempf_5mm),factor*numpy.ones_like(Tempf_8mm)], color=['r','mediumslateblue','thistle','slategray'],histtype='stepfilled')

Tempf_3mm[np.abs(Tempf_3mm) >373].count()
Tempf_4mm[np.abs(Tempf_4mm) >373].count()
Tempf_5mm[np.abs(Tempf_5mm) >373].count()
Tempf_8mm[np.abs(Tempf_8mm) >373].count()

plt.setp(e[0], edgecolor='black', lw=2, fill= False, label= '3mm')
plt.setp(e[1], edgecolor='mediumslateblue', fill= False, lw=2, label= '4mm', hatch= "...")
plt.setp(e[2], edgecolor='firebrick', lw=2, label= '5mm', fill= False, hatch= "//")
plt.setp(e[3], edgecolor='slategray', lw=2, label= '8mm', alpha= 0.3)

plt.legend()

plt.title('Female rotor surface temperature> 100 degC')
plt.xlabel('Surface Temperature (in C)')
plt.ylabel('Female Rotor Surface Area ($mm^2$)')
plt.yticks([0,250,500,750, 1000,1250,1500,1750,2000,2250])

plt.ylim(0, 2000)
plt.xlim(100, 225)

plt.savefig('./Subtemp_SA_Female.pdf',format='pdf')

#Temp>100 degC-------------------------------------


data_male= pd.Series([(Tempm_3mm[np.abs(Tempm_3mm) >373].count())*factor, (Tempm_4mm[np.abs(Tempm_4mm) >373].count())*factor, (Tempm_5mm[np.abs(Tempm_5mm) >373].count())*factor, (Tempm_8mm[np.abs(Tempm_8mm) >373].count())*factor])

data_female= pd.Series([(Tempf_3mm[np.abs(Tempf_3mm) >373].count())*factor, (Tempf_4mm[np.abs(Tempf_4mm) >373].count())*factor, (Tempf_5mm[np.abs(Tempf_5mm) >373].count())*factor, (Tempf_8mm[np.abs(Tempf_8mm) >373].count())*factor])

data_dia= pd.Series([3,4,5,8])

plt.plot(data_dia,data_male, label= 'Male',color='indigo', linewidth=2)
plt.plot(data_dia,data_female, label= 'Female', color='maroon', linewidth=2)

plt.title('Surface Temperature>100 degC')
plt.xlabel('$doil$ (mm)')
plt.ylabel('Rotor Surface Area ($mm^2$)')
 
#plt.xticks([40,50, 60, 70, 80, 90, 100, 110, 120, 130, 140,150, 160])
# Create names
plt.legend()

plt.xlim(3.0, 8.2)
plt.ylim(0, 7000)

plt.savefig('./AvgTemp_SA_Rotors.pdf',format='pdf')

