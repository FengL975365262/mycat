#coding=utf8

def analysisHTTP(requestinfo):
	infos = requestinfo.split('\r\n')
	request_action = infos[0].split(' ')
	request_method = request_action[0]
	request_url = request_action[1]
	request_protocol = request_action[2]
	request = eval(request_method + 'Request()')
	setinfos = getattr(request,'setinfos')
	content = ''
	if request_method == 'GET':
		if '?' in request_url: 
			content = request_url[request_url.index('?')+1:]
			request_url = request_url[:request_url.index('?')]
	else:
		content = infos[-1]
	infodict = {'method': request_method,'url' : request_url,'protocol' :request_protocol,'content' : content}
	for info in infos[1:]:
		infolist = info.split(': ')
		if len(infolist) != 2: continue 
		infodict.setdefault(infolist[0],infolist[1])
	setinfos(infodict)
	print('\r\n收到' + request_method + '请求，请求内容如下：\r\n' + str(request.__dict__))
	return request

class HTTPRequest:
	
	def __init__(self):
		self.protocol = 'HTTP/1.1'
		self.method = ''
		self.url = ''
		self.host = ''
		self.connection = ''
		self.user_agent = ''
		self.upgrade_insecure_requests = 1
		self.accept = []
		self.accept_encoding = ''
		self.accept_language = ''
		self.referer = ''
		self.params = {}
	
	def setinfos(self,infodict):
		self.referer = infodict.get('Referer','')
		self.method = infodict.get('method','GET')
		self.url = infodict.get('url','/')
		self.host = infodict.get('Host')
		self.connection = infodict.get('Connection', '')
		self.user_agent = infodict.get('User-Agent','')
		self.upgrade_insecure_requests = int(infodict.get('Upgrade-Insecure-Requests','1'))
		self.accept = infodict.get('Accept','').split(',')
		self.accept_encoding = infodict.get('Accept-Encoding','')
		self.accept_language = infodict.get('Accept-Language','')
		self.params = self.analysisContent(infodict.get('content',''))
		
	def analysisContent(self,content):
		if len(content) < 1 : return {}
		paramslist = content.split('&')
		params = {}
		for param in paramslist:
			paramlist = param.split('=')
			if len(paramlist) != 2 : continue
			params.setdefault(paramlist[0],paramlist[1])
		return params	
		
class POSTRequest(HTTPRequest):

	def __init__(self):
		super(POSTRequest,self).__init__()
		self.referer = ''
		self.content_type = ''
		self.cache_control = {}
		self.origin = ''
		self.content_length = 0
		
	def setinfos(self,infodict):
		super().setinfos(infodict)
		self.content_type = infodict.get('Content-Type','')
		self.cache_control = super().analysisContent(infodict.get('Cache-Control',''))
		self.origin = infodict.get('Origin','')
		self.content_length = int(infodict.get('Content-Length','0'))
		
class GETRequest(HTTPRequest):

	def __init__(self):
		super(GETRequest,self).__init__()
		self.cookie = {}
	
	def setinfos(self,infodict):
		super().setinfos(infodict)
		self.cookie = super().analysisContent(infodict.get('Cookie',''))