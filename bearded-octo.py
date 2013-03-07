import urllib2
from bottle import *

@post('/<port:int>/<scheme>/<website>/<path:path>') #for non-http port
@post('/<scheme>/<website>/<path:path>') #for everything else
def post_get(website,port=80,scheme="http",path=None):
	try:
		params = request.query
		yield str(params)
		get = ""
		for p in params:
			get += str(str(p)+"="+str(params[p])+"&")
		get=get[:-1]
		yield str(get)
		req = urllib2.urlopen(str(scheme)+"://"+str(website)+":"+str(port)+"/"+str(path)+"?"+str(get))
		yield "OK"
	except Exception,e: yield str(e)

@route('/')
def index():yield ""

run(host="",port=80)