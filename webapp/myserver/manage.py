#encoding:utf-8

import urls,controllers,controlutils

def manage(urlstr,request,response):
	return url(urlstr,request,response)

def url(urlstr,request,response):
	controllerstr = urls.urls.get(urlstr,'null')
	print('\r\n请求方法路径：' + urlstr + '   ' +'请求方法为：' + controllerstr + '\r\n')
	if not controllerstr : 
		response.status = '500'
		response.mark = 'ERROR'
	try:
		controller = getattr(controllers,controllerstr)
		return controller(request,response)
	except Exception as exception:
		print('\r\n没有找到指定方法' + controllerstr +'\r\n')
		response.status = '404'
		response.mark = 'NOTFOUND'