#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --------------------------------------------------------------
# aria2 python script for bittorrent downloads.                |
# http://aria2.sourceforge.net/                                |
# Created by clamsawd (clamsawd@openmailbox.org)               |
# Licensed by GPL v.3                                          |
# Last update: 26-10-2015                                      |
# Builds:                                                      |
#   * https://github.com/clamsawd/aria2-static-builds/releases |
#   * https://github.com/tatsuhiro-t/aria2/releases            |
# Compatible with Python 3.x                                   |
# --------------------------------------------------------------
version="0.9-beta"

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
	if os.name == "posix":
		os.system("clear")
	elif os.name == "nt":
		os.system("cls")
	else:
		print ("Error: Unable clear screen")

#Function to pause screen
def PauseScreen():
	if os.name == "posix":
		os.system("read pause")
	elif os.name == "nt":
		os.system("pause > nul")

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
	abcf.write('DiscFiles="C:" # Only for Windows\n')
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
aria2Check = Popen(['aria2c', '-v'], stdout=PIPE, stderr=PIPE)
ErrorFound = aria2Check.stderr.read()
aria2Check.stderr.close()

if not ErrorFound:
	print ("aria2 detected")
else:
	print ("")
	print ("Error: 'aria2' is not installed!")
	print ("")
	print ("Builds:")
	print ("  * https://github.com/clamsawd/aria2-static-builds/releases")
	print ("  * https://github.com/tatsuhiro-t/aria2/releases")
	print ("")

#Show main menu
MainMenu = 1
while MainMenu <= 2:
	ClearScreen()
	print ("")
	print ("** aria2bt-main.py bittorrent v"+version+" **")
	print ("")
	print ("- aria2bt-main.py config:")
	print ("")
	if os.name == "posix":
		print (" * Config.file: "+os.environ["HOME"]+"/.aria2/a2conf.py")
	elif os.name == "nt":
		print (" * Config.file: "+os.environ["USERPROFILE"]+"\.aria2\\a2conf.py")
	print ("")
	print (" * Download directory: "+TorrentFolder)
	if os.name == "posix":
		print (" * Torrents directory: "+TorrentFiles+"/*.torrent")
	elif os.name == "nt":
		print (" * Torrents directory: "+TorrentFiles+"\*.torrent ("+DiscFiles+")")
	print (" * Download speed: "+MaxSpeedDownload+" | Upload speed: "+MaxSpeedUpload)
	print (" * Encryption: "+Encryptation+" | RPC: "+Rpc+" (Port: "+RpcPort+")")
	print (" * Max.peers: "+BtMaxPeers+" | Max.downloads: "+MaxDownloads)
	print (" * Seeding: "+Seeding+" | Seed ratio: "+SeedRatio)
	print (" * Debugging: "+aria2Debug+" | Debug.level: "+DebugLevel)
	print (" * CA-Certificate: "+CaCertificate+" ("+CaCertificateFile+")")
	print (" * File allocation: "+FileAllocation)
	print ("")
	InputMenu=input("- run(r) | list(l) | magnet(m) | urls(u) | quit(q): ")
 #Options from InputMenu variable
	if InputMenu == "r" or InputMenu == "1":
		ClearScreen()
		print ("")
		print ("Running aria2c.... (Ctrl + C to stop)")
		if os.name == "posix":
			os.system("aria2c "+OtherOptions+" "+TorrentFiles+"/*.torrent "+AllOptions+" -d "+TorrentFolder)
			print ("")
			print ("Press ENTER to return")
			PauseScreen()
			print ("Exiting...")
		elif os.name == "nt":
			os.chdir(DiscFiles)
			os.chdir(TorrentFiles)
			os.system('dir /B | find ".torrent" > aria2-list.txt')
			os.system("aria2c "+OtherOptions+" -i aria2-list.txt "+AllOptions+" -d "+TorrentFolder)
			print ("")
			print ("Press ENTER to return")
			PauseScreen()
			print ("Exiting...")
	elif InputMenu == "l" or InputMenu == "2":
		ClearScreen()
		print ("")
		print ("* List of torrents that will be loaded:")
		print ("")
		if os.name == "posix":
			os.system("ls "+TorrentFiles+" | grep '.torrent'")
		elif os.name == "nt":
			os.system('dir /B '+TorrentFiles+' | find ".torrent"')
		print ("")
		print ("* List of incomplete downloads:")
		print ("")
		if os.name == "posix":
			os.system("ls "+TorrentFolder+" | grep '.aria2'")
		elif os.name == "nt":
			os.system('dir /B '+TorrentFolder+' | find ".aria2"')
		print ("")
		print ("Press ENTER to return")
		PauseScreen()
		print ("Exiting...")
	elif InputMenu == "m" or InputMenu == "3":
		ClearScreen()
		print ("")
		print ("* Make torrent file from Magnet-link")
		print ("")
		MagnetLink=input("- Type the Magnet-link (in quotes): ")
		print ("")
		os.system("aria2c --bt-metadata-only=true --bt-save-metadata=true -d "+TorrentFiles+" "+MagnetLink)
		print ("")
		print ("Press ENTER to return")
		PauseScreen()
		print ("Exiting...")
	elif InputMenu == "u" or InputMenu == "4":
		os.chdir(TorrentFiles)
		if os.path.isfile("urls.txt"):
			print (TorrentFiles+"/urls.txt exists")
		else:
			urlsfile=open('urls.txt','w')
			urlsfile.close()
			urlsfile=open('urls.txt','a')
			urlsfile.write("")
			urlsfile.close()
		ClearScreen()
		print ("")
		if os.name == "posix":
			print ("* List URLs ("+TorrentFiles+"/urls.txt):")
		elif os.name == "nt":
			print ("* List URLs ("+TorrentFiles+"\\urls.txt):")
		print ("")
		if os.name == "posix":
			os.system("cat urls.txt")
		elif os.name == "nt":
			os.system("type urls.txt")
			print ("")
		print ("")
		LoadUrls=input("- Load URLs? (y/n): ")
		if LoadUrls == "y":
			ClearScreen()
			print ("")
			print ("Running aria2c.... (Ctrl + C to stop)")
			os.system("aria2c "+OtherOptions+" -i urls.txt "+AllOptions+" -d "+TorrentFolder)
			print ("")
			print ("Press ENTER to return")
			PauseScreen()
		elif LoadUrls == "n":
			print ("")
			print ("Exiting...")
		else:
			print ("")
			print ("Exiting...")
	elif InputMenu == "q" or InputMenu == "5":
		print ("")
		print ("Exiting...")
		MainMenu += 2
	else:
		ClearScreen()
		print ("")
		print ("Invalid Option")
		print ("")
		print ("Press ENTER to return")
		PauseScreen()
