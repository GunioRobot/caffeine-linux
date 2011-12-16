import os
import sys
from subprocess import call
import InstallDeveloper

def DeveloperHelper():

	print "Welcome to the Caffeine Linux Developer Helper!\n"
	print "Please select what you would like to do: "
	print "Your options are:"
	print "1. Install Developer Packages\n 2. Install KDE SC Build Dependencies\n 3. Clean Up Developer Environment"
	print "Please enter the number of your choice at the prompt."
	prompt = ">"
	choice = int(raw_input(prompt))
	if choice == 1:
		InstallDeveloper.installDeveloperPackages()
	elif choice == 2:
		InstallDeveloper.installBuildDepends()
	elif choice == 3:
		InstallDeveloper.cleanUpDevEnv()
	else:
		print "I'm sorry, I did not recognize your input. Please try again or C-c to quit"
		DeveloperHelper()

if __name__ == "__main__":
	DeveloperHelper()