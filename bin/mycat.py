#coding=utf8

from socket import * 
import threading
import time
import httprequest,httpresponse,controlutils,dispatcher

class tcpSocketSvr:
	
	def __init__(self,port=8080):
		self.socketSvr = socket(AF_INET,SOCK_STREAM)
		ADDR = ('',port)
		self.socketSvr.bind(ADDR)
		self.socketSvr.listen(1)
	
	def start(self):
		while True:
			print('wait for connected......')
			cliSocket,addr = self.socketSvr.accept()
			try:
				pubInfo(cliSocket)
			except Exception as err:
				pass
	
def pubInfo(cliSocket):
	data = cliSocket.recv(1024)
	reqmsg = data.decode('utf-8')
	print('\r\n请求原文为：\r\n' + reqmsg + '\r\n')
	#if not reqmsg: pubInfo(cliSocket)
	res = httpresponse.HTTPResponse()
	request = httprequest.analysisHTTP(reqmsg);
	dispatcher.dispatcher(request,res)
	res.content_type = request.accept[0]
	''' 返回图片流尝试
	if request.url.endswith('.jpg'):
		resdict = {'Server': 'myserver'}
		response = httpresponse.getresponse('',resdict) + res.content
		cliSocket.send(response)
		cliSocket.close()
		return
	else:
	'''
	response = res.packageresponse()
	print('\r\n回复请求的内容为：\r\n' + response + '\r\n')
	cliSocket.send(bytes(response , 'utf-8'))
	cliSocket.close()

if __name__ == '__main__':
	tcpSvrSock = tcpSocketSvr(8080)
	tcpSvrSock.start()