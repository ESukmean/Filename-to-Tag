import sys
import os, os.path

def check_mp3ver(path):
	pass

def set_id3v1(path, title):
	pass

def set_id3v2(path, title):
	pass

def proc(path):
	if path[-4:] != '.mp3':
		print(path, 'is not MP3 file. skip')
	
	ver = check_mp3ver(path)
	if ver == 31:
		pass
	elif ver == 32:
		pass
	
	pass


for path in sys.argv[1:]:
	if os.path.isfile(path):
		proc(path)
	
	elif os.path.isdir(path):
		for fpath in os.walk(path):
			for fname in fpath:
				proc(fname)
	else:
		print('<', path, '> not Exists')