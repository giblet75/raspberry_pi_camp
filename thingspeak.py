import httplib, urllib
params = urllib.urlencode({'field1':89, 'field2':"TheGiblet", 'key':'T0U6G8PQVFTIDWJI'})
headers = {"Content-type":"application/x-www-form-urlencoded", "Accept": "text/plain"}
conn = httplib.HTTPConnection("api.thingspeak.com:80")
conn.request("POST", "/update", params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
print data
conn.close()

