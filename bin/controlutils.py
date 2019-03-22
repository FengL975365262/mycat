#encoding=utf8

def readhtml(path):
	with open(path,'rb') as htmlfile:
		htmlbytes = htmlfile.read()
		if path.endswith('jpg'):
			return htmlbytes
		htmlstr = htmlbytes.decode('utf-8')
		return htmlstr