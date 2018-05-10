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

class Settlement_File:
	#BOOLEAN Variables
	open_txn = False
	decl_txn = False

	#Temporary Variables
	auth = 0
	adjust = 0
	credit = 0
	void = 0
	declines = 0
	stl = 0

	#strings
	fullname = ""
	dob = ""
	ext = ""
	
	def __init__(self):
		#BOOLEAN Variables
		self.open_txn = False
		self.decl_txn = False

		#Temporary Variables
		self.auth = 0
		self.adjust = 0
		self.credit = 0
		self.void = 0
		self.declines = 0
		self.stl = 0

		#strings
		self.fullname = ""
		self.dob = ""
		self.ext = ""
	
#	def __del__(self):
#		self.init_trans_vars()
#		self.init_file_vars()
	
	def init_trans_vars(self):
		#BOOLEAN Variables
		open_txn = False
		decl_txn = False
		
	def init_file_vars(self):
		#Temporary Variables
		auth = 0
		adjust = 0
		credit = 0
		void = 0
		declines = 0
		stl = 0
		
		#strings
		fullname = ""
		dob = ""
		ext = ""

	def p_summary(self):
		print(self.fullname)
		print("Auths: " + str(self.auth))
		print("Adjusts: " + str(self.adjust))
		print("Credits: " + str(self.credit))
		print("Voids: " + str(self.void))
		print("Declines: " + str(self.declines))
		print("\n\n")


#Setup Trans Header for Files
header = Trans("NUM", "TYPE", "DOB", "DATE", "TIME", "EMPLOYEE", "TABLE", "CHECK", "AUTHAMT", "BATCHAMT", "BATCHTIP", "CARDTYPE", "CARDMASK", "EXP", "APPROVED", "AUTH", "ERROR", "FILENAME", "FILETYPE", "REF", "", "", "")
header.set_txn()

f = Settlement_File()


#Create and open generic reporting files
decTransFile = open(dirname + "\\DECLINES-all.csv", 'w')
stlTransFile = open(dirname + "\\SETTLEMENTS-all.csv", 'w')
allTransFile = open(dirname + "\\STL-DEC-all.csv", 'w')
perLineFile = open(dirname + "\\data-all.csv", 'w')
crunchAll = open(dirname + "\\cards-ALL.csv", 'w')
#add Headers to files
allTransFile.write(header.txn)
decTransFile.write(header.txn)
stlTransFile.write(header.txn)
perLineFile.write(header.txn)


#REGEXES
re_filename = re.compile('^((\d{8}\.*\d{0,3})\.(\w+))$', re.IGNORECASE)
re_auth = re.compile('\s*TYPE\s*AUTHORIZE', re.IGNORECASE)
re_adjust = re.compile('\s*TYPE\s*ADJUST', re.IGNORECASE)
re_credit = re.compile('\s*TYPE\s*CREDIT', re.IGNORECASE)
re_void = re.compile('\s*TYPE\s*VOID', re.IGNORECASE)
re_decline = re.compile('\s*APPROVED\s*NO', re.IGNORECASE)
re_type = re.compile('/^\s+TYPE\s+(.+)$//', re.IGNORECASE)
re_dob = re.compile('/^\s+DOB\s+(.+)$//', re.IGNORECASE)
re_date = re.compile('/^\s+DATE\s+(.+)$//', re.IGNORECASE)
re_time = re.compile('/^\s+TIME\s+(.+)$//', re.IGNORECASE)
re_emp = re.compile('/^\s+EMPLOYEE\s+(.+)$//', re.IGNORECASE)
re_table = re.compile('/^\s+TABLE\s+(.+)$//', re.IGNORECASE)
re_check = re.compile('/^\s+CHECK\s+(.+)$//', re.IGNORECASE)
re_amt = re.compile('/^\s+AUTHAMT\s+(.+)$//', re.IGNORECASE)
re_bat = re.compile('/^\s+BATCHAMT\s+(.+)$//', re.IGNORECASE)
re_tip = re.compile('/^\s+BATCHTIP\s+(.+)$//', re.IGNORECASE)
re_card = re.compile('/^\s+CARDTYPE\s+(.+)$//', re.IGNORECASE)
re_mask = re.compile('/^\s+CARDMASK\s+X+(.+)$//', re.IGNORECASE)
re_exp = re.compile('/^\s+EXP\s+(.+)$//', re.IGNORECASE)
re_ref = re.compile('/^\s+REF\s+(.+)$//', re.IGNORECASE)
re_authnum = re.compile('/^\s+AUTH\s+(.+)$//', re.IGNORECASE)
re_appr = re.compile('/^\s+APPROVED\s+(.+)$//', re.IGNORECASE)
re_error = re.compile('/^\s+ERROR\s+(.+)$//', re.IGNORECASE)
re_info = re.compile('/^\s+INFO\s+(.+)$//', re.IGNORECASE)

#Go through list of Files
for file in file_names:
	#Parse Settlement files
	if os.path.exists(file):
		is_stl = re.match(re_filename, file)
		if(is_stl):
			f.fullname = is_stl.group(1)
			f.dob = is_stl.group(2)
			f.ext = is_stl.group(3)
			
			list = open(file, 'r')
			for line in list:
				
				if(re.match(re_auth, line)):
					f.auth += 1
				elif(re.match(re_adjust, line)):
					f.adjust += 1
				elif(re.match(re_credit, line)):
					f.credit += 1
				elif(re.match(re_void, line)):
					f.void += 1
				elif(re.match(re_decline, line)):
					f.declines += 1
#					print("DECLINE: " + line)
			
				if("BEGIN" in line):
					f.open_txn = True
				elif("APPROVED" in line):
					f.decl_txn = True
				elif("END" in line):
					f.init_trans_vars()
#					print("add to Queue and reset Vars")
			
				if(f.open_txn == True):
					m_type = re.match(re_type, line)
					m_dob = re.match(re_dob, line)
					m_date = re.match(re_date, line)
					m_time = re.match(re_time, line)
					m_emp = re.match(re_emp, line)
					m_table = re.match(re_table, line)
					m_check = re.match(re_check, line)
					m_amt = re.match(re_amt, line)
					m_bat = re.match(re_bat, line)
					m_tip = re.match(re_tip, line)
					m_card = re.match(re_card, line)
					m_mask = re.match(re_mask, line)
					m_exp = re.match(re_exp, line)
					m_ref = re.match(re_ref, line)
					m_authnum = re.match(re_authnum, line)
					m_appr = re.match(re_appr, line)
					m_error = re.match(re_error, line)
					m_info = re.match(re_info, line)
					
					if(m_type):
						tran = m_type.group(1)
					elif(m_dob):
						dobT = m_dob.group(1)
					elif(m_date):
						dateT = m_date.group(1)
					elif(m_time):
						time = m_time.group(1)
					elif(m_emp):
						emp = m_emp.group(1)
					elif(m_table):
						table = m_table.group(1)
						#if(table.include? ','):
						#	table.sub!(',','')
					elif(m_check):
						check = m_check.group(1)
					elif(m_amt):
						amt = m_amt.group(1)
					elif(m_bat):
						bam = m_bat.group(1)
					elif(m_tip):
						tip = m_tip.group(1)
					elif(m_card):
						card = m_card.group(1)
					elif(m_mask):
						mask = m_mask.group(1)
					elif(m_exp):
						exp = m_exp.group(1)
					elif(m_ref):
						ref = m_ref.group(1)
					elif(m_authnum):
						authorize = m_authnum.group(1)
					elif(m_appr):
						appr = m_appr.group(1)
					elif(m_error):
						error = m_error.group(1)
					elif(m_info):
						info = m_info.group(1)
			
			list.close()
			f.p_summary()
			f = Settlement_File()










#Close Files
decTransFile.close()
stlTransFile.close()
allTransFile.close()
perLineFile.close()
crunchAll.close()


os.system("pause")
