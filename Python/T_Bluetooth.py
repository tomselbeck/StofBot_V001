#!/usr/bin/python

# Requirements:
# sudo aptitude install python-bluetooth

# Information Sources: 
# http://code.google.com/p/pybluez/source/browse/trunk/examples/simple/rfc...
# http://people.csail.mit.edu/albert/bluez-intro/x290.html#py-rfcomm-clien...

# import bluetooth
# import sys
# import threading

# uuid = "fa87c0d0-afac-11de-8a39-0800200c9a66"
# addr = '60:E7:01:8B:F8:AA'

from bluetooth import *
import sys
if sys.version < '3':
    input = raw_input

addr = '60:E7:01:8B:F8:AA'


if len(sys.argv) < 2:
    print("no device specified.  Searching all nearby bluetooth devices for")
    print("the SampleServer service")
else:
    addr = sys.argv[1]
    print("Searching for SampleServer on %s" % addr)

# search for the SampleServer service
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
service_matches = find_service( uuid = uuid, address = addr )

if len(service_matches) == 0:
    print("couldn't find the SampleServer service =(")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("connecting to \"%s\" on %s" % (name, host))

# Create the client socket
sock=BluetoothSocket( RFCOMM )
sock.connect((host, port))

print("connected.  type stuff")
while True:
    data = input()
    if len(data) == 0: break
    sock.send(data)

sock.close()