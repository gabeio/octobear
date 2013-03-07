import octobear

assert octobear.post_get("255.255.255.255") == "OK"
assert octobear.get_post("255.255.255.255") == "OK"

