import httplib, urllib, sys
if len(sys.argv) == 1:
    print 'Usage: %s <name> [<value>]' % sys.argv[0]
    quit()

value = "OFF"
if len(sys.argv) > 2:
    value = sys.argv[2]

params = urllib.urlencode({'command_string':value, 'key':'4M3RR9JJ6TNGJBHZ'})
headers = {"Content-type":"application/x-www-form-urlencoded", "Accept": "text/plain"}
conn = httplib.HTTPConnection("api.thingspeak.com:80")
conn.request("POST", "/talkbacks/%s/commands" % sys.argv[1], params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
print data
conn.close()

