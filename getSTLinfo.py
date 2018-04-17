import glob
import os

cwd = os.getcwd()
files = glob.glob(cwd + "\\*.*")

for i in range(len(files)):
	x = files[i].split("\\")
	print(x[len(x) - 1])




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
	
	def set_type(self, type):
		self.type = type
	
	def get_txn(self):
		self.txn = self.type + "," + self.dob + "," + self.date + "," + self.time + "," + self.emp + "," + self.table + "," + self.check + "," + self.amt + "," + self.bam + "," + self.tip + "," + self.card + "," + self.mask + "," + self.exp + "," + self.appr + "," + self.auth + "," + self.error + "," + self.filename + "," + self.filetype + "," + self.ref + ","



header = Trans("NUM", "TYPE", "DOB", "DATE", "TIME", "EMPLOYEE", "TABLE", "CHECK", "AUTHAMT", "BATCHAMT", "BATCHTIP", "CARDTYPE", "CARDMASK", "EXP", "APPROVED", "AUTH", "ERROR", "FILENAME", "FILETYPE", "REF", "", "", "")

header.get_txn()















