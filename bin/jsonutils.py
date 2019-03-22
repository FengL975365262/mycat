#encoding:utf8

def obj2json(obj):
	if not hasattr(obj,'__dict__'):
		return {}
	obj_json = obj.__dict__
	for key in obj_json.keys():
		if isinstance(obj_json[key],list):
			for index in range(len(obj_json[key])):
				if hasattr(obj_json[key][index],'__dict__'):
					obj_json[key][index] = obj2json(obj_json[key][index])
		elif hasattr(obj_json[key],'__dict__'):
			obj_json[key] = obj2json(obj_json[key])
	return obj_json

	
