bearded-octo
============

Bottlepy Server to change post requests to get requests & vise versa.


# API:
/PORT(optional)/SCHEME(http/s)/website(www.example.com)/the rest goes here?query data will be passed also

# Example:
http://localhost/8080/http/localhost/set?i=1 [get]
sends a post request to:
http://localhost:8080/set?i=1 [post]

OR

http://localhost/http/localhost/account/something?password=pass [post]
sends a get request to:
http://localhost/account/something?password=pass [get]

# Run with:

## Linux/Unix/Mac
- nohup python bearded-octo.py &

## Windows (untested)
- python bearded-octo.py