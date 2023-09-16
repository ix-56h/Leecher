#!/usr/bin/env python
import sys
sys.path.append('Sublist3r')
import argparse, requests
import sublist3r
from colorama import Fore
from art import *

status_accepted = [200, 403, 402, 404, 503, 505]
basic_tests =   [
				".htaccess",
				".htaccess~",
				"htaccess",
				"htaccess~",
				"htaccess.txt",
				"robots.txt",
				"readme.txt",
				"config/install.php",
				"config/readme.txt"
				]

def fucking_false_positive(response):
	if response.status_code == 200:
		if response.content == None:
			return True
		if (b"404" or b"Not found" or b"not found") in response.content:
			return False
	return False

def print_header():
		ascii_header = text2art("LEECHER", "rand")
		print(ascii_header)
		print("\t\t\tAutomated Security Audit\n")

def make_request(domain, redirect):
	try:
		response = requests.get("https://"+domain, allow_redirects=redirect, verify=False, timeout=5)
		if not response:
			response = requests.get("http://"+domain, allow_redirects=redirect, verify=False, timeout=5)
		return response
	except:
		return None 

class   Leecher:
	def __init__(self):
		print_header()
		parser = argparse.ArgumentParser()
		parser.add_argument("-t", "--target", help="Set the target") 
		parser.add_argument("--full-check", help="Make a recursive check for all subdomains for all CMS", action="store_true")
		parser.add_argument("-s", "--silent", help="Disable modules output", default=False, action="store_true")
		parser.add_argument("-v", "--verbose", help="Verbose mod", default=False, action="store_true")
		self.args = parser.parse_args()
		if not self.args.target:
			parser.error("Target needed")

	def launch_scan(self):
		subdomains = self.sublister_wrapper(self.args.target)
		print("\nLet's h4ck\n")
		self.process_scan(subdomains)

	def sublister_wrapper(self, domain):
		print("Launching Sublist3r...")
		try:
			subdomains = sublist3r.main(
					domain,
					40,
					None,
					ports=None,
					silent=self.args.silent, verbose=self.args.verbose, enable_bruteforce=False, engines=None
					)
			subdomains.insert(0, domain)
			if self.args.verbose:
				print("Subdomains founds :")
				print(subdomains)
			return subdomains
		except:
			sys.exit("Error while processing Sublist3r");

	def process_scan(self, subdomains):
		for domain in subdomains:
			response = make_request(domain, True)
			if response:
				if response.status_code in status_accepted:
					print("[" + Fore.YELLOW + "+" + Fore.RESET + "] [%s] is responding" % domain)
					self.process_basic_tests(domain)
				else:
					if self.args.verbose:
						print("[" + Fore.RED + "-" + Fore.RESET + "] [%s] is not responding" % domain)

	def process_basic_tests(self, domain):
		for test in basic_tests:
			response = make_request(domain+'/'+test, False)
			if response is not None:
				if response.status_code == 200 and not fucking_false_positive(response):
					print("[" + Fore.GREEN + "✓" + Fore.RESET + "]\t[%s/%s] succeed" % (domain, test))
				else:
					if self.args.verbose:
						print("[" + Fore.RED + "X" + Fore.RESET + "]\t[%s/%s] failed" % (domain, test))

	def wpscan_wrapper(self):
		print("WPScan processing...")
		#use wpscan and save result with sublist for the current url
		return

def	leecher_launch():
	instance = Leecher()
	instance.launch_scan()

if __name__ == '__main__':
	leecher_launch()
