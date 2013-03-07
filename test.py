from bottle import *
import urllib2

@route('/set')
def set_get():
    i = request.params["i"]
    global variable
    variable = i

@route('/get')
def get_get():
    global variable
    yield variable

run(host="alpha", port=8081)
