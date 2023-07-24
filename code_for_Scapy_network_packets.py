
# python3                
Python 3.11.4 (main, Jun  7 2023, 10:13:09) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from scapy.all import *


>>> file = rdpcap('/home/kali/Testing/dns.pcapng')
>>> file
<dns.pcapng: TCP:0 UDP:244 ICMP:0 Other:14>
>>> file.show
<bound method _PacketList.show of <dns.pcapng: TCP:0 UDP:244 ICMP:0 Other:14>>
>>> file.show()

0000 Ether / IP / UDP 192.168.86.1:2008 > 192.168.86.255:2008 / Raw
0001 Ether / IP / UDP 192.168.86.1:2008 > 192.168.86.255:2008 / Raw
0002 Ether / IP / UDP 192.168.86.1:2008 > 192.168.86.255:2008 / Raw
0003 Ether / IP / UDP 192.168.86.1:2008 > 192.168.86.255:2008 / Raw


>>> f = file[0]
>>> f
<Ether  dst=ff:ff:ff:ff:ff:ff src=00:50:56:c0:00:08 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=48 id=23708 flags= frag=0 ttl=128 proto=udp chksum=0xafcf src=192.168.86.1 dst=192.168.86.255 |<UDP  sport=2008 dport=2008 len=28 chksum=0x62e3 |<Raw  load='BC 15DESKTOP-V5O50OK' |>>>>
>>> f.show()
###[ Ethernet ]### 
  dst       = ff:ff:ff:ff:ff:ff
  src       = 00:50:56:c0:00:08
  type      = IPv4
###[ IP ]### 
     version   = 4
     ihl       = 5
     tos       = 0x0
     len       = 48
     id        = 23708
     flags     = 
     frag      = 0
     ttl       = 128
     proto     = udp
     chksum    = 0xafcf
     src       = 192.168.86.1
     dst       = 192.168.86.255
     \options   \
###[ UDP ]### 
        sport     = 2008
        dport     = 2008
        len       = 28
        chksum    = 0x62e3
###[ Raw ]### 
           load      = 'BC 15DESKTOP-V5O50OK'



>>> f[UDP].sport
2008
>>> f[UDP].sport = 3002
>>> f[UDP].sport
3002
>>> f.show()
###[ Ethernet ]### 
  dst       = ff:ff:ff:ff:ff:ff
  src       = 00:50:56:c0:00:08
  type      = IPv4
###[ IP ]### 
     version   = 4
     ihl       = 5
     tos       = 0x0
     len       = 48
     id        = 23708
     flags     = 
     frag      = 0
     ttl       = 128
     proto     = udp
     chksum    = 0xafcf
     src       = 192.168.86.1
     dst       = 192.168.86.255
     \options   \
###[ UDP ]### 
        sport     = 3002
        dport     = 2008
        len       = 28
        chksum    = 0x62e3
###[ Raw ]### 
           load      = 'BC 15DESKTOP-V5O50OK'


>>> p = IP()/UDP()
>>> p.show()
###[ IP ]### 
  version   = 4
  ihl       = None
  tos       = 0x0
  len       = None
  id        = 1
  flags     = 
  frag      = 0
  ttl       = 64
  proto     = udp
  chksum    = None
  src       = 127.0.0.1
  dst       = 127.0.0.1
  \options   \
###[ UDP ]### 
     sport     = domain
     dport     = domain
     len       = None
     chksum    = None

>>> p[UDP].chksum = 'domain'
>>> p.show()
###[ IP ]### 
  version   = 4
  ihl       = None
  tos       = 0x0
  len       = None
  id        = 1
  flags     = 
  frag      = 0
  ttl       = 64
  proto     = udp
  chksum    = None
  src       = 127.0.0.1
  dst       = 127.0.0.1
  \options   \
###[ UDP ]### 
     sport     = domain
     dport     = domain
     len       = None
     chksum    = domain


>>> p = IP(dst='127.78.45.133')/UDP(chksum=3214)
>>> p.show()
###[ IP ]### 
  version   = 4
  ihl       = None
  tos       = 0x0
  len       = None
  id        = 1
  flags     = 
  frag      = 0
  ttl       = 64
  proto     = udp
  chksum    = None
  src       = 127.0.0.1
  dst       = 127.78.45.133
  \options   \
###[ UDP ]### 
     sport     = domain
     dport     = domain
     len       = None
     chksum    = 0xc8e

>>> p = IP(dst='127.78.45.133')/UDP(chksum='3214')
>>> p.show()
###[ IP ]### 
  version   = 4
  ihl       = None
  tos       = 0x0
  len       = None
  id        = 1
  flags     = 
  frag      = 0
  ttl       = 64
  proto     = udp
  chksum    = None
  src       = 127.0.0.1
  dst       = 127.78.45.133
  \options   \
###[ UDP ]### 
     sport     = domain
     dport     = domain
     len       = None
     chksum    = 3214
