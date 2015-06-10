#!/usr/bin/env python

#####################################################################################
## [Name]: 2-mix-find_dns.py -- script to find dns servers amongst a list of machines
##-----------------------------------------------------------------------------------
## [Author]: Re4son re4son [at] whitedome.com.au
##-----------------------------------------------------------------------------------
## [Details]: 
## Script iterates through <target IP list> and checks if TCP port 53 is open.
## The result is diplayed on screen and written to <output directory>\DNS-servers.txt 
##-----------------------------------------------------------------------------------
## [Usage]: 
## python 2-mix-find_dns.py <target IP list> <output directory>
#####################################################################################

import subprocess
import sys

if len(sys.argv) != 3:
    print "\nUsage: python 2-mix-find_dns.py <target IP list> <output directory>\n"
    sys.exit(0)

TARGETS = sys.argv[1].strip()
OUTDIR = sys.argv[2].strip()

outfile = OUTDIR + "/DNS-Servers.txt"

def dnsScan(ip_address):
# Insert dns enumerations such as zone transfers here
# Not required if you only want to identify dns servers
    return

inf = open(TARGETS, 'r')
outf = open(outfile, 'w')
res = 0
print " "
print "[+] Enumerating TCP port 53 to find dns servers"
outf.write("[+] Enumerating TCP port 53 to find dns servers\n")
for ip_address in inf:
    ip_address = ip_address.strip()
    DNSSCAN = "nmap -n -sV -Pn -vv -p53 %s" % (ip_address)
    results = subprocess.check_output(DNSSCAN, shell=True)
    lines = results.split("\n")
    for line in lines:
        line = line.strip()
        line = line.rstrip()
        if ("53/tcp" in line) and ("open" in line) and ("open" in line) and not ("Discovered" in line):
	    print "[*] Found DNS service running on: %s/TCP" % (ip_address)
            outf.write("[*] Found DNS service running on: %s/TCP\n" % (ip_address))
	    print "   [>] %s" % (line)
            outf.write("   [>] %s\n" % (line))
	    res += 1
print " "
outf.write("\n")
print "[*] Found %s DNS servers" % (res)
outf.write("[*] Found %s DNS servers\n" % (res))
print "[*] Pick one and include in 3-mix-recon.py"
print " "
inf.close()
outf.close()
