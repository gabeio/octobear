import urllib2
from bottle import *

@post('/<port:int>/<scheme>/<website>/<path:path>') #for non-http port
@post('/<scheme>/<website>/<path:path>') #for everything else
def post_get(website,port=80,scheme="http",path=None):
    params = request.query
    get = ""
    for p in params:
        get += (p+"="+params[p]+"&")
    get=get[:-1]
    req = urllib2.urlopen(scheme+"://"+website+":"+port+"/"+path+"?"+get)
    yield "OK"

@route('/')
def index():yield ""

run()
