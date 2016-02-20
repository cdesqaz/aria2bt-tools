#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --------------------------------------------------------------
# aria2 python script for bittorrent downloads.                |
# http://aria2.sourceforge.net/                                |
# Created by clamsawd (clamsawd@openmailbox.org)               |
# Licensed by GPL v.3                                          |
# Last update: 20-02-2016                                      |
# Builds:                                                      |
#   * https://github.com/clamsawd/aria2-static-builds/releases |
#   * https://github.com/tatsuhiro-t/aria2/releases            |
# Compatible with Python 3.x                                   |
# --------------------------------------------------------------
version="1.2.1"

#Import python-modules
import subprocess
import os
import sys
import shutil

#Check if your system use Python 3.x
if sys.version_info<(3,0):
	print ("")
	print ("You need python 3.x to run this program.")
	print ("")
	exit()

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
	ConfigFile=os.environ["HOME"]+"/.aria2/aria2bt.conf"
	FilesTorrent="/*.torrent"
	print ("POSIX detected")
elif os.name == "nt":
	os.chdir(os.environ["USERPROFILE"])
	ConfigFile=os.environ["USERPROFILE"]+"\\.aria2\\aria2bt.conf"
	FilesTorrent="\\*.torrent"
	print ("Windows detected")

if not os.path.exists(".aria2"):
	os.makedirs(".aria2")
	os.chdir(".aria2")
if os.path.exists(".aria2"):
	os.chdir(".aria2")

#Check if exists 'aria2.conf'
if os.path.isfile("aria2.conf"):
	print ("aria2.conf exists")
else:
	print ("aria2.conf created")
	acf=open('aria2.conf','w')
	acf.close()
	acf=open('aria2.conf','a')
	acf.write('# sample configuration file of aria2c\n')
	acf.close()

#Check if exists 'aria2bt.conf'
if os.path.isfile("aria2bt.conf"):
	print ("aria2bt.conf exists")
else:
	ClearScreen()
	print ("")
	print ("* The configuration file doesn't exist")
	print ("")
	print ("* You can create it if you run 'aria2bt-config.py'")
	print ("")
	PauseReturn=input("+ Press ENTER to exit ")
	print ("Exiting...")
	exit()

#Import variables from aria2bt.conf
exec(open("aria2bt.conf").read())

#Check input files
try:
	if os.path.isfile(sys.argv[1]):
		ClearScreen()
		print ("")
		print ("** aria2bt-tools (main) v"+version+" **")
		print ("")
		print ("* File detected: "+sys.argv[1])
		print ("")
		InputFile=input("- Do you want to copy file to "+TorrentFiles+" directory (y/n): ")
		if InputFile == "n":
			print ("")
			print ("Exiting...")
		else:
			try:
				shutil.copy(sys.argv[1], TorrentFiles)
				print ("")
				print ("* File copied successfully")
				print ("")
				PauseReturn=input("+ Press ENTER to continue ")
				print ("Loading...")
			except:
				print ("")
				print ("* Failed to copy the file")
				print ("")
				PauseReturn=input("+ Press ENTER to continue ")
				print ("Loading...")
except:
	print ("No input files")

#Define aria2c variables
SpeedOptions="--max-overall-download-limit="+MaxSpeedDownload+" --max-overall-upload-limit="+MaxSpeedUpload
PeerOptions="--bt-max-peers="+BtMaxPeers
if CaCertificate == "no":
	OtherOptions="-V -j " +MaxDownloads+" --file-allocation="+FileAllocation+" --auto-file-renaming=false --allow-overwrite=false"
elif CaCertificate == "yes":
	OtherOptions="-V -j "+MaxDownloads+" --file-allocation="+FileAllocation+" --auto-file-renaming=false --allow-overwrite=false --ca-certificate="+CaCertificateFile
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
	print ("* Error: 'aria2' is not installed!")
	print ("")
	print ("* Builds:")
	print ("  * https://github.com/clamsawd/aria2-static-builds/releases")
	print ("  * https://github.com/tatsuhiro-t/aria2/releases")
	print ("")
	PauseExit=input("+ Press ENTER to exit ")
	exit()

#Show main menu
MainMenu = 1
while MainMenu <= 2:
	ClearScreen()
	print ("")
	print ("** aria2bt-tools (main) v"+version+" **")
	print ("")
	print ("- aria2bt-tools config:")
	print ("")
	print (" * Config.file: "+ConfigFile)
	print ("")
	print (" * Download directory: "+TorrentFolder)
	print (" * Torrents directory: "+TorrentFiles+FilesTorrent)
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
			PauseReturn=input("+ Press ENTER to return ")
			print ("Exiting...")
		elif os.name == "nt":
			#os.chdir(DiscFiles)
			os.chdir(TorrentFiles)
			os.system('dir /B | find ".torrent" > aria2-list.txt')
			os.system("aria2c "+OtherOptions+" -i aria2-list.txt "+AllOptions+" -d "+TorrentFolder)
			print ("")
			PauseReturn=input("+ Press ENTER to return ")
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
		PauseReturn=input("+ Press ENTER to return ")
		print ("Exiting...")
	elif InputMenu == "m" or InputMenu == "3":
		ClearScreen()
		os.chdir(TorrentFiles)
		print ("")
		print ("* Make torrent file from Magnet-link")
		print ("")
		MagnetLink=input("- Type the Magnet-link (in quotes): ")
		print ("")
		os.system("aria2c --bt-metadata-only=true --bt-save-metadata=true -d "+TorrentFiles+" "+MagnetLink)
		print ("")
		PauseReturn=input("+ Press ENTER to return ")
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
		readfile=open('urls.txt', 'r')
		print(readfile.read())
		readfile.close()
		print ("")
		LoadUrls=input("- Load URLs? (y/n): ")
		if LoadUrls == "y":
			ClearScreen()
			print ("")
			print ("Running aria2c.... (Ctrl + C to stop)")
			os.system("aria2c "+OtherOptions+" -i urls.txt "+AllOptions+" -d "+TorrentFolder)
			print ("")
			PauseReturn=input("+ Press ENTER to return ")
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
		print ("* Invalid Option")
		print ("")
		PauseReturn=input("+ Press ENTER to return ")
