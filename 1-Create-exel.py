#dnf install python3-pip
#yum install epel-release
#yum install python3-pip 
#pip3 install openpyxl

#import openpyxl
from openpyxl import Workbook

#Create Exel File
workbook = Workbook()
#workbook = openpyxl.workbook()

#Select First Sheet
sheet = workbook.active

#Change Name
sheet.title = "Server Info"

#Create Header
sheet.append(["Hostname", "OS", "CPU", "RAM (GB)", "Disk (GB)"])

#Append sampel Data
sheet.append(["server1", "Ubuntu 20", "Intel Xeon" ,8 , 500])
sheet.append(["server2", "Centos 7", "AMD EPYC" ,16 , 1000])

#Save Exel
workbook.save("server.xlsx")
print("Exel File created successfully")
