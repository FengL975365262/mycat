#coding:utf-8

import os,sys,controlutils

homepath = os.getcwd()[:os.getcwd().index('mycat')+5]

def dispatcher(request,response):
	url = request.url
	print('\r\n当前url请求为： ' + url + '\r\n')
	if url == '/':
		print('\r\n访问主页面： index.html  \r\n')
		response.content = controlutils.readhtml(homepath+'\\bin\\index.html')
		return
	urlinfolist = url.split('/')
	if len(urlinfolist) > 1:
		response.server = urlinfolist[1]
		serverpath = homepath +'\\webapp\\'+response.server
		if url.endswith('css') | url.endswith('js') | url.endswith('jpg') | url.endswith('png'):
			sourcepath = url[len(response.server)+1:].replace('/','\\')
			print('\r\n下载静态文件路径：' + serverpath+'\\templates'+sourcepath + '\r\n')
			response.content = controlutils.readhtml(serverpath+'\\templates'+sourcepath)
			return
		if os.path.exists(serverpath):
			sys.path.append(serverpath)
			print('\r\n跳转到服务位置： ' + serverpath + '\r\n')
			manage = __import__('manage')
			result = manage.manage(url[url.index(response.server)+len(response.server):],request,response)
			if isinstance(result,str) & result.endswith('.html'):
				response.content = controlutils.readhtml(serverpath+'\\templates\\'+result)
		else:
			response.status = '404'
			response.mark = 'NOTFOUND'
			
def findstaticfile(request,response):
	pass
	
def findcontroller(url):
	pass
def nofind():
	pass