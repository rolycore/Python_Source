# http://code.activestate.com/recipes/117211-simple-very-sntp-client/
import socket
import struct
import sys
import time

def gettime_ntp(addr='time.nist.gov'):
    
       TIME1970 = 2208988800      # Thanks to F.Lundh
       client = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
       data = '\x1b' + 47 * '\0'
       client.sendto( data, (addr, 123))
       data, address = client.recvfrom( 1024 )

       if data:
            t = struct.unpack( '!12I', data )[10]
            t -= TIME1970

       return time.ctime(t),t
