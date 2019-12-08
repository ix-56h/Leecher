#!/usr/bin/env python
import sys
sys.path.append('Sublist3r')

import argparse, requests
import sublist3r
from art import *

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

class   Leecher:
    def __init__(self):
        ascii_header = text2art("LEECHER", "rand")
        print(ascii_header)
        print("\t\t\tAutomated Security Audit\n")
        parser = argparse.ArgumentParser()
        parser.add_argument("-t", "--target", help="Set the target") 
        parser.add_argument("--full-check", help="Make a recursive check for all subdomains for all CMS", action="store_true")
        self.args = parser.parse_args()
        if not self.args.target:
            parser.error("Target needed")

    def launch_scan(self):
        #self.check_domain(self, args.target)
        self.sublister_wrapper(self.args.target)
        return

    def sublister_wrapper(self, domain):
        print("Launching Sublist3r...")
        subdomains = sublist3r.main(
                    domain,
                    40,
                    None,
                    ports=None,
                    silent=True, verbose=False, enable_bruteforce=False, engines=None
                    )
        print(subdomains)
        return

    def check_domain(self, domain_url):
        print("Check server status...")
        #if fail to connect go to next 
        #else check basic_tests and check if CMS are used and check versionning
        return

    def wpscan_wrapper(self):
        print("WPScan processing...")
        #use wpscan and save result with sublist for the current url
        return

def     leecher_launch():
    instance = Leecher()
    instance.launch_scan()
if __name__ == '__main__':
    leecher_launch()
