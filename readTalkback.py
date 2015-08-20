import httplib, urllib, sys, time
#import pibrella

if len(sys.argv) == 1:
    print 'Usage: %s <talkback_id>' % sys.argv[0]
    quit()
running = True

while running:
    time.sleep(1)
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    conn.request("GET", "/talkbacks/%s/commands/execute?api_key=4M3RR9JJ6TNGJBHZ" % sys.argv[1])
    response = conn.getresponse()
    if response.status == 200:
        command = response.read()
        if command == "quit":
            running = False
        else:
            exec command
    else:
        print response.status, response.reason
        running = False

conn.close()

