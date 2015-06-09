#!/usr/bin/env python
##########################################################################
## [Name]: 1-mix-ping_sweep.py -- a recon/enumeration script
## [Author]: Re4son re4son [at] whitedome.com.au
##------------------------------------------------------------------------
## [Details]: 
## Script to perform a ping sweep over a given range and list each live 
## host in file <outputdir>/targets.txt. 
##------------------------------------------------------------------------
## [Usage]: 
## python 1-mix-ping_sweep.py <target IP range> <output directory>
##########################################################################

import subprocess
import sys
import os

if len(sys.argv) != 3:
    print "\nUsage: 1-mix-ping-sweep.py <range> <output directory>\n"
    sys.exit(0)

RANGE = sys.argv[1].strip()
OUTDIR = sys.argv[2].strip()


try:
    os.stat(OUTDIR)
except:
    os.mkdir(OUTDIR)
    print " "
    print "[!] %s didn't exist, created %s" % (OUTDIR, OUTDIR)

outfile = OUTDIR + "/targets.txt"

res = 0
f = open(outfile, 'w')
print " "
print "[+] Performing ping sweep over %s" % (RANGE)
SWEEP = "nmap -n -sP %s" % (RANGE)
results = subprocess.check_output(SWEEP, shell=True)
lines = results.split("\n")
for line in lines:
    line = line.strip()
    line = line.rstrip()
    if ("Nmap scan report for" in line):
        ip_address = line.split(" ")[4]
        if (res > 0):
            f.write('\n')
        f.write("%s" % (ip_address))
        print "[*] %s" % (ip_address)
        res += 1
print " "
print "[*] Found %s live hosts" % (res)
print "[*] Created target list %s" % (outfile)
print "[*] Paste %s into 3-mix-recon.py" % (outfile)
print " "
f.close()
