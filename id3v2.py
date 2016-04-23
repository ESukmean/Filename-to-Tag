import os

TITLE = 'TIT2'

class ID3v2:
	file = False
	bit = []
	ver = 0
	
	
	def __init__(self, path = False, file = False):
		if file != False:
			self.file = file
		else:
			self.file = open(path, 'r+b')
		
		self.file.seek(5)
		bit = self.file.read(1)[0]
		self.bit = [True if bit & 1 << b else False for b in range(8)]
		
		ver = self.ID3v2Version()
			
	def checkID3v2(self):
		if self.file.read(3) != b'ID3':
			return False
			
		return True
		
	def ID3v2Version(self):
		self.file.seek(3, 0)
		
		ver = self.file.read(2)
		return [v for v in ver]
			
	def Read(self, tag = ''):
		pass
		
	def Write(self, tag = ''):
		pass