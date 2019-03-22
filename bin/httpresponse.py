#coding:utf8
import time

class HTTPResponse():
	
	def __init__(self):
		self.accept_ranges = 'bytes'
		self.protocol = 'HTTP/1.1'
		self.status = '200'
		self.mark = 'OK'
		self.server = 'server'
		self.date = ''
		self.content_type = 'text/html'
		self.content_charset = 'charset=UTF-8'
		self.connection = 'keep-alive'
		self.vary = 'Accept-Encoding'
		self.access_control_allow_origin = '*'
		self.access_control_allow_headers = 'X-Requested-with,access_token,access-token,content-type,multipart/form-data,application/json'
		self.access_control_allow_methods = 'GET,POST,OPTIONS'
		self.content_length = 0
		self.session_id = None
		self.content = ''
	
	def packageresponse(self):
		response = ''
		self.date = time.strftime('%a, %d %b %Y %H:%M:%S GMT',time.localtime())
		response = response + self.protocol + ' ' + self.status + ' ' + self.mark + '\r\n'
		response = response + 'Accept-Ranges: ' + self.accept_ranges + '\r\n'
		response = response + 'Server: ' + self.server + '\r\n'
		response = response + 'Date: ' + self.date + '\r\n'
		response = response + 'Content-Type: ' + self.content_type + ';' + self.content_charset + '\r\n'
		response = response + 'Connection: ' + self.connection + '\r\n'
		response = response + 'Vary: ' + self.vary + '\r\n'
		response = response + 'Access-Control-Allow-Origin: ' + self.access_control_allow_origin + '\r\n'
		response = response + 'Access-Control-Allow-Headers: ' + self.access_control_allow_headers + '\r\n'
		response = response + 'Access-Control-Allow-Methods: ' + self.access_control_allow_methods + '\r\n'
		content = self.analisysContent()
		self.content_length = len(content)
		response = response + 'Content-Length: ' + str(self.content_length) + '\r\n\r\n'
		return response + str(content)
	
	def analisysContent(self):
		content = ''
		if isinstance(self.content,dict):
			self.content_type = 'application/json'
			keys = self.content.keys()
			for key in keys:
				content = content + str(key) + '=' + str(self.content[key]) + '&'
			return content[:-1]
		return self.content
def getresponse(requestHead,requestdict):
	response = ''
	requestHead = 'HTTP/1.1 304 Not Modified'
	nowdate = time.strftime('%a, %d %b %Y %H:%M:%S GMT',time.localtime())
	requestdict.setdefault('Date',nowdate)
	requestdict.setdefault('Cache-Control','no-cache')
	requestdict.setdefault('Accept-Ranges','bytes')
	requestdict.setdefault('X-Powered-By','ASP.NET')
	response = response + requestHead + '\r\n'
	for key  in requestdict.keys():
		response = response + key +': ' + requestdict[key] + '\r\n'
	return bytes(response + '\r\n','utf-8')