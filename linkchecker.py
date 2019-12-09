#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

import time 

import sys 

import os 

def load_animation(): 

  

    
    load_str = "we are the next level team"

    ls_len = len(load_str) 
 

    animation = "|/-\\"

    anicount = 0
    counttime = 0        
    i = 0                     

  

    while (counttime != 100): 

        time.sleep(0.075)  
        load_str_list = list(load_str)
        x = ord(load_str_list[i]) 
        y = 0                             
        if x != 32 and x != 46:              
            if x>90: 
                y = x-32
            else: 
                y = x + 32
            load_str_list[i]= chr(y) 
        res =''              

        for j in range(ls_len): 

            res = res + load_str_list[j] 
        sys.stdout.write("\r"+res + animation[anicount]) 

        sys.stdout.flush() 

        load_str = res 

        anicount = (anicount + 1)% 4

        i =(i + 1)% ls_len 

        counttime = counttime + 1

      

    # windows

    if os.name =="nt": 

        os.system("cls") 

          

    # linux / Mac OS 

    else: 

        os.system("clear") 

if __name__ == '__main__':  

    load_animation() 
   
class warna:
    HEADER = '\033[95m'
    CYAN = '\033[86m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    BADFAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1
    
def carilink():
	f = open("link.txt","r");
	print "\n\nMohon tunggu cok: \n"
	while True:
		link = f.readline()
		if not link:
			break
		req_link = "http://"+link										
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print warna.WARNING+"HTTP 200 ok :) >>> ",req_link

def Credit():
	Space(8); print warna.OKGREEN+"101011        010100"
	Space(8); print "011001        010001"
	Space(8); print "010001        100101"
	Space(8); print "111001        001101"
	Space(8); print "000101        110101"
	Space(8); print "00001101010100101011"
	Space(8); print "11100001010110011001"
	Space(8); print "01100101100001100111"
	Space(8); print "010001        010101"
	Space(8); print "111001        101010"
	Space(8); print "000101        010101"
	Space(8); print "000011        110101"
	Space(8); print "111000        001010"

Credit()
carilink()