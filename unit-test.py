import octobear

assert octobear.post_get("beta.shov.me",80,"http","passer") == "OK"
assert octobear.get_post("beta.shov.me",80,"http","passer") == "OK"
