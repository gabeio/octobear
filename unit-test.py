import octobear

def post_get():
	z = ""
	x = octobear.post_get("beta.shov.me",80,"http","passer")
	for y in x:
		z+=y
	return z

def get_post():
	z = ""
	x = octobear.get_post("beta.shov.me",80,"http","passer")
	for y in x:
		z+=y
	return z

assert post_get() == "OK"
assert get_post() == "OK"