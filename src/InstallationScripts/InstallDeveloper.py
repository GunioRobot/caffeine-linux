#!/usr/bin/env python

import os
from subprocess import call
import sys

def installDeveloperPackages():
	"""Installs the packages necessary for a caffeine linux develoment
	environment """
	print "Now marking packages for installation"
	return_code = call("apt-get install --assume-yes install build-essential git cmake qtcreator vim virtualbox-ose \
						debhelper dbus-x11 libxml12-utils libxkbfile-dev network-manager-dev \
						libqt4-dev libstreamanalyzer-dev libstrigiqtdbusclient-dev \
						libxft-dev libxss-dev libpci-dev libpolkit-backend-1-dev libpoppler-qt4-dev \
						liblcmsl-dev libv41-dev devscripts ", shell=True)
	if retrun_code != 0:
		print """An error has occured, please review the console output to determine what went wrong 
		If it is a problem with this script please file a bug report."""
	else:
		print "The operation complete successfully!"

def installBuildDepends():
	"""This function installs dependencies necessary to build the KDE SC from source.
	There are a lot of dependencies so this will only get called if the user wishes"""

	error_code = call("apt-get install --assume-yes graphviz libxml2-utils libopenexr-dev libjasper-dev libenchant-dev \
					libavahi-common-dev libaspell-dev libasound2-dev libldap2-dev libsasl12-dev \
					libsmbclient-dev libxkbfile-dev libxcbl-dev libxklavier-dev libxdamage-dev \
					libxcomosite-dev libbluetooth-dev libusb-dev network-manager-dev \
					libsensors4-dev libnm-util-dev libcfitsio3-dev libnova-dev libeigen2-dev \
					libopenbable-dev libfacile-ocaml-dev libboost-python-dev libsvn-dev libsvncpp-dev \
					libcommoncpp2-dev libidn11-dev libpci-dev libxss-dev libxft-dev \
					libpolkit-agent-1-dev libpolkit-backend-1-dev libpolkit-gobject-1-dev libspectre-dev", shell=True)

if __name__ == "__main__":
	# Check to see if we are root
	uid = os.getuid()
	if uid != 0:
		print "This script must be run as root!"
		sys.exit()
	installDeveloperPackages()
	prompt = ">"
	print "Install KDE build dependencies as well? [Y/n]"
	answer = raw_input(prompt)
	if answer == "Y" or answer == "y":
		installBuildDepends()
	elif answer == "N" or answer == "n":
		print "OK! Your initial packaging and development packages are now installed. For help \
		with packaging please visit http://wiki.debian.org/IntroDebianPackaging\n \
		For help with caffeine linux related problems, please open an issue on github \
		or send a message to the caffeine linux devel mailing list."
		sys.exit()
	else: 
		print "Invalid input detected, now exiting!"
		sys.exit()

