import glob
import os

cwd = os.getcwd()
files = glob.glob(cwd + "\\*.*")

for i in range(len(files)):
	x = files[i].split("\\")
	print(x[len(x) - 1])


