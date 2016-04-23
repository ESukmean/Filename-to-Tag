import sys
import os, os.path

ENCODING = 'utf-8'

def check_mp3ver(file):
	to_return = 1;
	
	if file.read(3) == b'ID3':
		to_return = to_return * 32
	
	file.seek(-128, 2)
	if file.read(3) == b'TAG':
		to_return = to_return * 31
	
	return to_return
	
def set_id3v1(file, title):

	file.seek(-125, 2)
	
	to_write = bytes(title, ENCODING)
	to_write += bytes((0 for x in range(30 - len(to_write))))
	
	file.write(to_write)

def set_id3v2(file, title):
	return False

def proc(path):
	if path[-4:] != '.mp3':
	
	title = os.path.basename(path)[:-4]
	file = open(path, 'r+b')
	ver = check_mp3ver(file)

        
	if ver == -1:
		return False
	
	if ver % 31 == 0:
		set_id3v1(file, title)
	
	elif ver % 32 == 0:
		set_id3v2(file, title)		
		
	return False

for path in sys.argv[1:]:
	if os.path.isfile(path):
	
	elif os.path.isdir(path):
		for fpath in os.walk(path):
			for fname in fpath:
				proc(fname)
	else:
		
