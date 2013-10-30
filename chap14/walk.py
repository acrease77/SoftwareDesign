import os
cwd=os.getcwd()

def walk(direct):
	if os.path.exists(direct):
		for name in os.listdir(direct):
			filepath=os.path.join(dirname,name)
			if os.path.isdir(filepath):
				walk(filepath)
			else:
				print filepath
