import urllib2;from bottle import *

@post('/<port:int>/<scheme>/<website>/<path:path>') #for non-http port
@post('/<scheme>/<website>/<path:path>') #for everything else
def post_get(website,port=80,scheme="http",path=""):
	try:
		params = request.query
		#yield str(params)
		get = ""
		for p in params:
			get += str(str(p)+"="+str(params[p])+"&")
		get=get[:-1]
		#yield str(get)
		req = urllib2.urlopen(str(scheme)+"://"+str(website)+":"+str(port)+"/"+str(path)+"?"+str(get))
		return "OK"
	except Exception,e: print str(e)

@get('/<port:int>/<scheme>/<website>/<path:path>')
@get('/<scheme>/<website>/<path:path>')
def get_post(website,port=80,scheme="http",path=""):
	try:
		params = request.query
		#yield str(params)
		get = ""
		for p in params:
			get += str(str(p)+"="+str(params[p])+"&")
		get=get[:-1]
		#yield str(get)
		req = urllib2.urlopen(str(scheme)+"://"+str(website)+":"+str(port)+"/"+str(path)+"?"+str(get),"")
		return "OK"
	except Exception,e: print str(e)

@route('/')
def index():yield ""

if __name__ == '__main__':
	run(host="",port=80)