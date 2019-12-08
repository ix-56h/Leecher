#!/usr/bin/env python
import argparse, requests

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
        parser = argparse.ArgumentParser()
        parser.add_argument("-t", "--target", help="Set the target") 
        parser.add_argument("--full-check", help="Make a recursive check for all subdomains for all CMS", action="store_true")
        args = parser.parse_args()
        if not args.target:
            parser.error("Target needed")
    
    def sublister_wrapper(self):
        #use sublister and save urls with list
        return

    def check_domain(self, domain_url):
        #if fail to connect go to next 
        #else check basic_tests and check if CMS are used and check versionning
        return

    def wpscan_wrapper(self):
        #use wpscan and save result with sublist for the current url
        return

def     leecher_launch():
    instance = Leecher()    

if __name__ == '__main__':
    leecher_launch()
