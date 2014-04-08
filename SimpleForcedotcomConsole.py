#!/usr/bin/python

import json
from simple_salesforce import Salesforce
import sys

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()

# Loop based on two inputs
# 'q' is quit, 'c' is contact, 'a' is account


# begin 
sf = Salesforce(username='tbd', password='tbd', security_token='tbd')



while 1:
	print 'Please choose from the following:'
	print 'q to quit, a for accounts, c for contacts'
	#next = sys.stdin.read(1)
	next = getch()
	if next == 'q' or next == 'g':
		break;
	elif next == 'c' or next == 's':
		divider = 'Contacts'
		header = "\tName\t\tEmail"
		records = sf.query("SELECT Id, Name, Email FROM Contact")
		records = records['records']
		value = 'Email'
	elif next == 'a':
		divider = 'Accounts'
		header = "\tName\t\tPhone"
		records = sf.query("SELECT Id, Name, Phone FROM Account")
		records = records['records']
		value = 'Phone'
	else:
		print "No valid input"
		print
		continue


	print "SELECT Id, Name, Email FROM Contact"

	print 
	print divider 
	print header
	for record in records:
			print " %-40s %20s " % (record['Name'], record[value])

print "done"


