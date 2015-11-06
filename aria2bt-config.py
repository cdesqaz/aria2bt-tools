#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------
# aria2 python script for bittorrent downloads (configuration tool)|
# http://aria2.sourceforge.net/                                    |
# Created by clamsawd (clamsawd@openmailbox.org)                   |
# Licensed by GPL v.3                                              |
# Last update: 01-11-2015                                          |
# Builds:                                                          |
#   * https://github.com/clamsawd/aria2-static-builds/releases     |
#   * https://github.com/tatsuhiro-t/aria2/releases                |
# Compatible with Python 3.x                                       |
# ------------------------------------------------------------------
version="1.0.1"

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
if os.path.isfile("aria2.conf"):
	print ("aria2.conf exists")
else:
	print ("aria2.conf created")
	acf=open('aria2.conf','w')
	acf.close()
	acf=open('aria2.conf','a')
	acf.write('# sample configuration file of aria2c\n')
	acf.close()

#Create configuration of aria2bt-tools
ClearScreen()	
print ("")
print ("** aria2bt-config.py v"+version+" **")
print ("")
TorrentFolderWhile = 1
while TorrentFolderWhile <= 2:
	TorrentFolderInput=input("Path of downloads folder (no spaces): ")
	if os.path.exists(TorrentFolderInput):
		TorrentFolderWhile += 2
	else:
		print ("")
		print ("'"+TorrentFolderInput+"' folder doesn't exist")
		print ("")
TorrentFilesWhile = 1
while TorrentFilesWhile <= 2:
	TorrentFilesInput=input("Path to load *.torrent files (folder) (no spaces): ")
	if os.path.exists(TorrentFilesInput):
		TorrentFilesWhile += 2
	else:
		print ("")
		print ("'"+TorrentFilesInput+"' folder doesn't exist")
		print ("")
CaCertificateFileInput=input("Path of CA-Certificates file (no spaces): ")
MaxSpeedDownloadNumber=input("[Default: 300K] Set the maximum download speed: ")
if MaxSpeedDownloadNumber != "":
	MaxSpeedDownloadInput=MaxSpeedDownloadNumber
else:
	MaxSpeedDownloadInput="300K"
MaxSpeedUploadNumber=input("[Default: 5K] Set the maximum upload speed: ")
if MaxSpeedUploadNumber != "":
	MaxSpeedUploadInput=MaxSpeedUploadNumber
else:
	MaxSpeedUploadInput="5K"
BtMaxPeersNumber=input("[Default: 25] Set the maximum BitTorrent peers: ")
if BtMaxPeersNumber != "":
	BtMaxPeersInput=BtMaxPeersNumber
else:
	BtMaxPeersInput="25"
MaxDownloadsNumber=input("[Default: 25] Set the maximum downloads: ")
if MaxDownloadsNumber != "":
	MaxDownloadsInput=MaxDownloadsNumber
else:
	MaxDownloadsInput="25"
EncryptationYesOrNo=input("[Default: y] Enable encryption? (y/n): ")
if EncryptationYesOrNo == "n":
	EncryptationInput="no"
else:
	EncryptationInput="yes"
RpcYesOrNo=input("[Default: y] Enable RPC? (y/n): ")
if RpcYesOrNo == "n":
	RpcInput="no"
	RpcPortInput="6800"
else:
	RpcInput="yes"
	RpcPortNumber=input("[Default: 6800] Set the port: ")
	if RpcPortNumber != "":
		RpcPortInput=RpcPortNumber
	else:
		RpcPortInput="6800"
SeedingYesOrNo=input("[Default: y] Enable seeding? (y/n): ")
if SeedingYesOrNo == "n":
	SeedingInput="no"
	SeedRatioInput="0.0"
else:
	SeedingInput="yes"
	SeedRatioInput="0.0"
aria2DebugYesOrNo=input("[Default: n] Enable debug? (y/n): ")
if aria2DebugYesOrNo == "y":
	aria2DebugInput="yes"
	DebugLevelInput="info"
else:
	aria2DebugInput="no"
	DebugLevelInput="info"
FileAllocationOption=input("[Default: none] Set file-allocation (none(n), prealloc(p), trunc(t), falloc(f)): ")
if FileAllocationOption == "p":
	FileAllocationInput="prealloc"
elif FileAllocationOption == "t":
	FileAllocationInput="trunc"
elif FileAllocationOption == "f":
	FileAllocationInput="falloc"
else:
	FileAllocationInput="none"
CaCertificateYesOrNo=input("[Default: n] Enable CA-Certificates? (y/n): ")
if CaCertificateYesOrNo == "y":
	CaCertificateInput="yes"
else:
	CaCertificateInput="no"

#Show your configuration	
ClearScreen()
print ("")
print ("** aria2bt-config.py v"+version+" **")
print ("")
print ("Your configuration:")
print ("")
print ('TorrentFolder="'+TorrentFolderInput+'"')
print ('TorrentFiles="'+TorrentFilesInput+'"')
print ('CaCertificateFile="'+CaCertificateFileInput+'"')
print ('MaxSpeedDownload="'+MaxSpeedDownloadInput+'"')
print ('MaxSpeedUpload="'+MaxSpeedUploadInput+'"')
print ('BtMaxPeers="'+BtMaxPeersInput+'"')
print ('MaxDownloads="'+MaxDownloadsInput+'"')
print ('Encryptation="'+EncryptationInput+'"')
print ('Rpc="'+RpcInput+'"')
print ('RpcPort="'+RpcPortInput+'"')
print ('Seeding="'+SeedingInput+'"')
print ('SeedRatio="'+SeedRatioInput+'"')
print ('aria2Debug="'+aria2DebugInput+'"')
print ('DebugLevel="'+DebugLevelInput+'"')
print ('FileAllocation="'+FileAllocationInput+'"')
print ('CaCertificate="'+CaCertificateInput+'"')
print ("")
print ("- Press ENTER to apply or Ctrl+C to cancel")
PauseScreen()

#Apply configuration to 'a2conf.py' file
os.remove("a2conf.py")
#Create configuration file
abcf=open('a2conf.py','w')
abcf.close()
abcf=open('a2conf.py','a')
abcf.write('#Default aria2 python-script config\n')
abcf.write('\n')
#abcf.write('DiscFiles="C:" # Only for Windows\n')
abcf.write('TorrentFolder="'+TorrentFolderInput+'"\n')
abcf.write('TorrentFiles="'+TorrentFilesInput+'"\n')
abcf.write('CaCertificateFile="'+CaCertificateFileInput+'"\n')
abcf.write('MaxSpeedDownload="'+MaxSpeedDownloadInput+'"\n')
abcf.write('MaxSpeedUpload="'+MaxSpeedUploadInput+'"\n')
abcf.write('BtMaxPeers="'+BtMaxPeersInput+'"\n')
abcf.write('MaxDownloads="'+MaxDownloadsInput+'"\n')
abcf.write('Encryptation="'+EncryptationInput+'"\n')
abcf.write('Rpc="'+RpcInput+'"\n')
abcf.write('RpcPort="'+RpcPortInput+'"\n')
abcf.write('Seeding="'+SeedingInput+'"\n')
abcf.write('SeedRatio="'+SeedRatioInput+'"\n')
abcf.write('aria2Debug="'+aria2DebugInput+'"\n')
abcf.write('DebugLevel="'+DebugLevelInput+'"\n')
abcf.write('FileAllocation="'+FileAllocationInput+'"\n')
abcf.write('CaCertificate="'+CaCertificateInput+'"\n')
abcf.close()
