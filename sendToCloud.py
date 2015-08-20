import httplib, urllib, sys
if len(sys.argv) == 1:
    print 'Usage: %s <name> [<value>]' % sys.argv[0]
    quit()

value = "None"
if len(sys.argv) > 2:
    value = sys.argv[2]

params = urllib.urlencode({'field1':sys.argv[1], 'field2':value, 'key':'T0U6G8PQVFTIDWJI'})
headers = {"Content-type":"application/x-www-form-urlencoded", "Accept": "text/plain"}
conn = httplib.HTTPConnection("api.thingspeak.com:80")
conn.request("POST", "/update", params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
print data
conn.close()

