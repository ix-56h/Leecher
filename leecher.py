#!/usr/bin/env python
import sys
sys.path.append('Sublist3r')

import argparse, requests
import sublist3r
from art import *

silent_mod = True
verbose_mod = False
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
        if ("404" or "Not found" or "not found") in response.content:
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
        parser.add_argument("-s", "--silent", help="Disable modules output", action="store_true")
        parser.add_argument("-v", "--verbose", help="Verbose mod", action="store_true")
        self.args = parser.parse_args()
        if not self.args.silent:
            silent_mod = False
        if self.args.verbose:
            verbose_mod = True 
        if not self.args.target:
            parser.error("Target needed")

    def launch_scan(self):
        subdomains = self.sublister_wrapper(self.args.target)
        self.process_scan(subdomains)

    def sublister_wrapper(self, domain):
        print("Launching Sublist3r...")
        try:
            subdomains = sublist3r.main(
                    domain,
                    40,
                    None,
                    ports=None,
                    silent=False, verbose=False, enable_bruteforce=False, engines=None
                    )
            subdomains.insert(0, domain)
            print("Subdomains founds :")
            print(subdomains)
            return subdomains
        except:
            sys.exit("Error while processing Sublist3r");

    def process_scan(self, subdomains):
        for domain in subdomains:
            response = make_request(domain, True)
            if not response:
               continue
            if response.status_code in status_accepted:
                print("[%s] is responding" % domain)
                self.process_basic_tests(domain)
            else:
            #    print("[%s] is not responding" % domain)
                continue

    def process_basic_tests(self, domain):
        for test in basic_tests:
            response = make_request(domain+'/'+test, False)
            if response == None:
                continue
            if response.status_code == 200 and not fucking_false_positive(response):
                print("[%s/%s] succeed" % (domain, test))
            #else:
            #    print("[%s/%s] failed" % (domain, test))

    def wpscan_wrapper(self):
        print("WPScan processing...")
        #use wpscan and save result with sublist for the current url
        return

def     leecher_launch():
    instance = Leecher()
    instance.launch_scan()

if __name__ == '__main__':
    leecher_launch()
