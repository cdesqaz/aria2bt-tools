#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------
# aria2 python script for bittorrent downloads (run without menu). |
# http://aria2.sourceforge.net/                                    |
# Created by clamsawd (clamsawd@openmailbox.org)                   |
# Licensed by GPL v.3                                              |
# Last update: 31-10-2015                                          |
# Builds:                                                          |
#   * https://github.com/clamsawd/aria2-static-builds/releases     |
#   * https://github.com/tatsuhiro-t/aria2/releases                |
# Compatible with Python 3.x                                       |
# ------------------------------------------------------------------
version="1.0"

#Import python-modules
import subprocess
import os
import sys

#Check if your system use Python 3.x
if sys.version_info<(3,0):
	print ("")
	print ("You need python 3.x to run this program.")
	print ("")
	exit(1)

#Function to clear screen
def ClearScreen():
	if sys.platform == "cygwin":
		print (300 * "\n")
	elif os.name == "posix":
		os.system("clear")
	elif os.name == "nt":
		os.system("cls")
	else:
		print ("Error: Unable clear screen")

#Detect system & PATH of user folder
if os.name == "posix":
	os.chdir(os.environ["HOME"])
	print ("POSIX detected")
elif os.name == "nt":
	os.chdir(os.environ["USERPROFILE"])
	print ("Windows detected")

if not os.path.exists(".aria2"):
	os.makedirs(".aria2")
	os.chdir(".aria2")
if os.path.exists(".aria2"):
	os.chdir(".aria2")

#Check if exists 'aria2.conf'
def createaria2cf():
	acf=open('aria2.conf','w')
	acf.close()
def writearia2cf():
	acf=open('aria2.conf','a')
	acf.write('# sample configuration file of aria2c\n')
	acf.close()

if os.path.isfile("aria2.conf"):
	print ("aria2.conf exists")
else:
	print ("aria2.conf created")
	createaria2cf()
	writearia2cf()

#Check if exists 'a2conf.py'
def createaria2btcf():
	abcf=open('a2conf.py','w')
	abcf.close()
def writearia2btcf():
	abcf=open('a2conf.py','a')
	abcf.write('#Default aria2 python-script config\n')
	abcf.write('\n')
	#abcf.write('DiscFiles="C:" # Only for Windows\n')
	abcf.write('TorrentFolder="/Torrent" # Edit the path (Paths without spaces)\n')
	abcf.write('TorrentFiles="/Torrent/Files" # Edit the path (Paths without spaces)\n')
	abcf.write('CaCertificateFile="/Certs/ca-certificates.crt" # Edit the path (Paths without spaces)\n')
	abcf.write('MaxSpeedDownload="300K"\n')
	abcf.write('MaxSpeedUpload="5K"\n')
	abcf.write('BtMaxPeers="25"\n')
	abcf.write('MaxDownloads="25"\n')
	abcf.write('Encryptation="yes"\n')
	abcf.write('Rpc="yes"\n')
	abcf.write('RpcPort="6800"\n')
	abcf.write('Seeding="yes"\n')
	abcf.write('SeedRatio="0.0"\n')
	abcf.write('aria2Debug="no"\n')
	abcf.write('DebugLevel="info"\n')
	abcf.write('FileAllocation="none"\n')
	abcf.write('CaCertificate="no"\n')
	abcf.close()

if os.path.isfile("a2conf.py"):
	print ("a2conf.py exists")
else:
	print ("a2conf.py created")
	createaria2btcf()
	writearia2btcf()

#Import variables from a2conf.py
exec(open("a2conf.py").read())

#Define aria2c variables
SpeedOptions="--max-overall-download-limit="+MaxSpeedDownload+" --max-overall-upload-limit="+MaxSpeedUpload
PeerOptions="--bt-max-peers="+BtMaxPeers
if CaCertificate == "no":
	OtherOptions="-V -j " +MaxDownloads+" --file-allocation="+FileAllocation+" --auto-file-renaming=false --allow-overwrite=false"
elif CaCertificate == "yes":
	OtherOptions="-V -j "+Maxdownloads+" --file-allocation="+FileAllocation+" --auto-file-renaming=false --allow-overwrite=false --ca-certificate="+CaCertificateFile
if Encryptation == "no":
	TorrentOptions="--bt-require-crypto=false"
elif Encryptation == "yes":
	TorrentOptions="--bt-min-crypto-level=arc4 --bt-require-crypto=true"
if Rpc == "no":
	RpcOptions="--rpc-listen-all=false"
elif Rpc == "yes":
	RpcOptions="--enable-rpc --rpc-listen-all=true --rpc-allow-origin-all --rpc-listen-port="+RpcPort
if Seeding == "no":
	SeedOptions="--seed-time=0"
elif Seeding == "yes":
	SeedOptions="--seed-ratio="+SeedRatio
if aria2Debug == "no":
	AllOptions=TorrentOptions+" "+SpeedOptions+" "+PeerOptions+" "+RpcOptions+" "+SeedOptions
elif aria2debug == "yes":
	AllOptions=TorrentOptions+" "+SpeedOptions+" "+PeerOptions+" "+RpcOptions+" "+SeedOptions+" --console-log-level="+DebugLevel

#Check if aria2 is installed
from subprocess import PIPE, Popen
try:
	aria2Check = Popen(['aria2c', '-v'], stdout=PIPE, stderr=PIPE)
	aria2Check.stderr.close()
except:
	ClearScreen()
	print ("")
	print ("Error: 'aria2' is not installed!")
	print ("")
	print ("Builds:")
	print ("  * https://github.com/clamsawd/aria2-static-builds/releases")
	print ("  * https://github.com/tatsuhiro-t/aria2/releases")
	print ("")
	PauseExit=input("Press ENTER to exit ")
	exit(1)

#Run aria2c
ClearScreen()
print ("")
print ("Running aria2c.... (Ctrl + C to stop)")
if os.name == "posix":
	os.system("aria2c "+OtherOptions+" "+TorrentFiles+"/*.torrent "+AllOptions+" -d "+TorrentFolder)
	print ("")
	PauseExit=input("Press ENTER to exit ")
	print ("Exiting...")
elif os.name == "nt":
	#os.chdir(DiscFiles)
	os.chdir(TorrentFiles)
	os.system('dir /B | find ".torrent" > aria2-list.txt')
	os.system("aria2c "+OtherOptions+" -i aria2-list.txt "+AllOptions+" -d "+TorrentFolder)
	print ("")
	PauseExit=input("Press ENTER to exit ")
	print ("Exiting...")
