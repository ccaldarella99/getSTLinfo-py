#! python3
# getSTLinfo.py - parse STL files and generate CSV files from them

import glob
import os
import re

#List Files in this folder
cwd = os.getcwd()
file_names = []
files = glob.glob(cwd + "\\*.*")
for i in range(len(files)):
	x = files[i].split("\\")
	file_names.append(x[len(x) - 1])

#Print List of File Names
#for file in file_names:
#	print(file)

#create Directories for CSV files
dirname = "stl-csv"
if not os.path.isdir(dirname):
	os.makedirs(dirname)
declines_name = dirname + "\\DECLINES"
if not os.path.isdir(declines_name):
	os.makedirs(declines_name)
stl_name = dirname + "\\SETTLEMENTS"
if not os.path.isdir(stl_name):
	os.makedirs(stl_name)





class Trans:
	num = ""
	type = ""
	dob = ""
	date = ""
	time = ""
	emp = ""
	table = ""
	check = ""
	amt = ""
	bam = ""
	tip = ""
	card = ""
	mask = ""
	exp = ""
	appr = ""
	auth = ""
	error = ""
	filename = ""
	filetype = ""
	ref = ""
	txn = ""
	info = ""
	auth_num = ""

	def __init__(self, num, *args):
		list_of_args = []
		for x in range(0, len(args)):
			list_of_args.append(args[x])
		self.num = num
		self.type = list_of_args[0]
		self.dob = list_of_args[1]
		self.date = list_of_args[2]
		self.time = list_of_args[3]
		self.emp = list_of_args[4]
		self.table = list_of_args[5]
		self.check = list_of_args[6]
		self.amt = list_of_args[7]
		self.bam = list_of_args[8]
		self.tip = list_of_args[9]
		self.card = list_of_args[10]
		self.mask = list_of_args[11]
		self.exp = list_of_args[12]
		self.appr = list_of_args[13]
		self.auth = list_of_args[14]
		self.error = list_of_args[15]
		self.filename = list_of_args[16]
		self.filetype = list_of_args[17]
		self.ref = list_of_args[18]
		self.txn = list_of_args[19]
		self.info = list_of_args[20]
		self.auth_num = list_of_args[21]
	
	def set_txn(self):
		self.txn = self.type + "," + self.dob + "," + self.date + "," + self.time + "," + self.emp + "," + self.table + "," + self.check + "," + self.amt + "," + self.bam + "," + self.tip + "," + self.card + "," + self.mask + "," + self.exp + "," + self.appr + "," + self.auth + "," + self.error + "," + self.filename + "," + self.filetype + "," + self.ref + ","


#Setup Header for Files
header = Trans("NUM", "TYPE", "DOB", "DATE", "TIME", "EMPLOYEE", "TABLE", "CHECK", "AUTHAMT", "BATCHAMT", "BATCHTIP", "CARDTYPE", "CARDMASK", "EXP", "APPROVED", "AUTH", "ERROR", "FILENAME", "FILETYPE", "REF", "", "", "")
header.set_txn()
#print(header.txn)


#Create generic reporting files and add Header
decTransFile = open(dirname + "\\DECLINES-all.csv", 'w')
stlTransFile = open(dirname + "\\SETTLEMENTS-all.csv", 'w')
allTransFile = open(dirname + "\\STL-DEC-all.csv", 'w')
perLineFile = open(dirname + "\\data-all.csv", 'w')
crunchAll = open(dirname + "\\cards-ALL.csv", 'w')
allTransFile.write(header.txn)
decTransFile.write(header.txn)
stlTransFile.write(header.txn)
perLineFile.write(header.txn)


#Temporary Variables
auth = 0
adjust = 0
credit = 0
void = 0
declines = 0


#REGEX
re_filename = re.compile('^((\d{8}\.*\d{0,3})\.(\w+))$', re.IGNORECASE)

#Go through list of Files
for file in file_names:
	#Parse Settlement files
	if os.path.exists(file):
		is_stl = re.match(re_filename, file)
		if(is_stl):
			fullname = is_stl.group(1)
			dob = is_stl.group(2)
			ext = is_stl.group(3)
			
			list = open(file, 'r')
			for line in list:
				
				if("AUTHORIZE" in line):
					auth += 1
				elif("ADJUST" in line):
					adjust += 1
				elif("CREDIT" in line):
					credit += 1
				elif("DELETE" in line):
					void += 1
				elif("APPROVED\s+NO" in line):
					declines += 1
#					print("DECLINE: " + line)
				
			list.close()














#Close Files
decTransFile.close()
stlTransFile.close()
allTransFile.close()
perLineFile.close()
crunchAll.close()


