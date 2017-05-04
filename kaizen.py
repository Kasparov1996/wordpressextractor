# Simple Data Extractor
# Thanks to @tester2009 
import getopt, sys, os, json, urllib2
from urlparse import urlparse


# ---------------------------------------------------------------------------

def banner():
    print " _   _ _       _                                        "              
    print "| | / /       (_)                                       "                
    print "| |/ /   __ _  _  ____  ___  _ __                       "  
    print "|    \  / _` || ||_  / / _ \| '_ \                      "
    print "| |\  \| (_| || | / / |  __/| | | |                     "
    print "\_| \_/ \__,_||_|/___| \___||_| |_|                     "
    print "--------------------------------------------------------"
    print "           Wordpress Data Extractor                     "
    print " Command: kaizen.py -u www.example.com                  "
    print " Credit : @tester2009||Kaizen69                         "
    print "--------------------------------------------------------"

if len(sys.argv[1:]) < 1:
    banner()
    sys.exit()

# --------------------------------------------------------------------

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hu:v", ["url=", "version", "help"])
    except getopt.GetoptError as err:
        print str(err)  # will print something like "option -a not recognized"
        sys.exit(2)
    for o, a in opts:
        if o in ("-u", "--url"):
            print " Wordpress Data Extractor"
            path = "wp-json/wp/v2/users"
            yis_url = ""
            if urlparse(a).netloc != '':
                # diz got http or https
                yis_url = urlparse(a).scheme + '://' + urlparse(a).netloc + '/' + path
            else:
                # diz nutz.
                yis_url = 'http://' + urlparse(a).path + '/' + path
            print yis_url
            print " "
            data = json.load(urllib2.urlopen(yis_url))
            for i in range(len(data)):
            	print data[i]['id'] # id number
                print data[i]['slug'] #username
                print data[i]['name'] #full name
                print data[i]['description'] #brief description
            	print " "
        elif o in ("-v", "--version"):
            print "Data Extractor"
            print "Version 1.2"
            print "by https://fb.com/Kasparov1996"
        elif o in ("-h", "--help"):
            os.system('cls' if os.name == 'nt' else 'clear')
            print "Data Extractor"
            print "python " +sys.argv[0]+" -u url"
            sys.exit()
        else:
            assert False, "unhandled option"
    if len(sys.argv)<2:
        print "Data Extractor"
        print "python " +sys.argv[0]+" -u url"
        sys.exit()

if __name__ == "__main__":
    main()