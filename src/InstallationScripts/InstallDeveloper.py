#!/usr/bin/env python

import os
from subprocess import call

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
	installDeveoperPackages()
	prompt = ">"
	print "Install KDE build dependencies as well? [Y/n]"
	answer = raw_input(prompt)
	if answer == "Y" or answer == "y":
		installBuildDepends()
	elif answer == "N" or answer == "n":
		pass
	else: print "Invalid input detected, now exiting!"

