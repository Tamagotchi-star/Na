import subprocess
import ctypes
#import requests 
import urllib
#from urllib import urlopen
from os import system, getuid, path
from time import sleep
from platform import system as systemos, architecture
from subprocess import check_output
RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2= '\033[91m', '\033[46m', '\033[36m', '\033[1;32m', '\033[0m' , '\033[1;33m' , '\033[1;93m', '\033[1;92m'
def verCheck():
    system('clear')
    print("{0}[{2}#{0}] {2}Checking For Updates{2}...".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW ))
    system('wget -O test.txt https://raw.githubusercontent.com/404-ghost/symbiote/master/version.txt')
    file = open('version.txt','r')
    a = file.read()
    x = a.split("\n")
    file2 = open('test.txt','r')
    b = file2.read()
    z = b.split("\n")
    file.close()
    file2.close()
    if x[0] == z[0]:
        print("{0}[{2}#{0}] {2}[Up-To-Date]- {0}v {6}{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, z[0]))
        system('rm -rf test.txt')
        sleep(3)
    else:
        print("{0}[{2}#{0}] {2}Their Is A Newer Version Available.".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW))
        print("{0}[{2}#{0}] {0}[{2}Current{0}]{2}- {0}v {6}\n{0}[{2}#{0}] {0}[{2}Available{0}]{2}- {0}v.{7}".format(RED, WHITE, CYAN, GREEN, DEFAULT, YELLOW, x[0], z[0])) 
        print("{0}[{2}#{0}] {2}Updating To The Latest Version {0}[{2}v {6}{0}] \n{0}[{2}#{0}] {2}Please Wait....{7}\n".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, z[0] ,GREEN2))
##            system('rm -rf symbiote.py && wget https://raw.githubusercontent.com/404-ghost/symbiote/master/symbiote.py')
##            system('clear')
##            system('rm -rf Checks.py && wget https://raw.githubusercontent.com/404-ghost/symbiote/master/Checks.py')
##            system('clear')
##            system('rm -rf logo.py && wget https://raw.githubusercontent.com/404-ghost/symbiote/master/logo.py')
##            system('clear')
##            system('rm -rf makepath.py && wget https://raw.githubusercontent.com/404-ghost/symbiote/master/makepath.py') 
##            system('clear')
##            system('rm -rf Server/www_b/face.jpg && cd Server/www_b/ && wget https://raw.githubusercontent.com/404-ghost/symbiote/master/Server/www_b/face.jpg')
##            system('rm -rf Server/www_b/index.php && cd Server/www_b/ && wget https://raw.githubusercontent.com/404-ghost/symbiote/master/Server/www_b/index.php')
##            system('clear')
##            system('rm -rf Server/www_b/index2.html && cd Server/www_b/ && wget https://raw.githubusercontent.com/404-ghost/symbiote/master/Server/www_b/index2.html')
##            system('rm -rf Server/www_b/ip.php && cd Server/www_b/ && wget https://raw.githubusercontent.com/404-ghost/symbiote/master/Server/www_b/ip.php')
##            system('clear')
##            system('rm -rf Server/www_b/post.php && cd Server/www_b/ && wget https://raw.githubusercontent.com/404-ghost/symbiote/master/Server/www_b/post.php')
##            system('rm -rf Server/www_b/worldmap.jpg && cd Server/www_b/ && wget https://github.com/404-ghost/symbiote/blob/master/Server/www_b/worldmap.jpg')
##            system('clear')
##                   
##            system('rm -rf Server/www_f/face.jpg && cd Server/www_f/ && wget https://raw.githubusercontent.com/404-ghost/symbiote/master/Server/www_f/face.jpg')
##            system('rm -rf Server/www_f/index.php && cd Server/www_f/ && wget https://raw.githubusercontent.com/404-ghost/symbiote/master/Server/www_f/index.php')
##            system('clear')
##            system('rm -rf Server/www_f/index2.html && cd Server/www_f/ && wget https://raw.githubusercontent.com/404-ghost/symbiote/master/Server/www_f/index2.html')
##            system('rm -rf Server/www_f/ip.php && cd Server/www_f/ && wget https://raw.githubusercontent.com/404-ghost/symbiote/master/Server/www_f/ip.php')
##            system('clear')
##            system('rm -rf Server/www_f/post.php && cd Server/www_f/ && wget https://raw.githubusercontent.com/404-ghost/symbiote/master/Server/www_f/post.php')
##            system('rm -rf Server/www_f/worldmap.jpg && cd Server/www_f/ && wget https://github.com/404-ghost/symbiote/blob/master/Server/www_f/worldmap.jpg')
##            system('clear')
##            system('rm -rf version.txt && wget https://raw.githubusercontent.com/404-ghost/symbiote/master/version.txt')
##            system('clear')
            #system("git clean -d -f > /dev/null && git pull -f > /dev/null")
        system('git checkout HEAD^ CapturedData && git checkout HEAD^ Server && git checkout HEAD^ LICENSE && git checkout HEAD^ Checks.py && git checkout HEAD^ logo.py && git checkout HEAD^ makepath.py && git checkout HEAD^ symbiote.py && git checkout HEAD^ version.txt')
        system('git stash')
        system('git pull')
        sleep(1)
        system('rm -rf test.txt')
        file = open('version.txt','r')
        a = file.read()
        x = a.split("\n")      
        print("{0}[{2}*{0}] {2}Version Status After Update.{2}.\n".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW))
        print("{0}[{2}*{0}] {0}[{2}Current{0}]{2}- {0}v {6}\n{0}[{2}*{0}] {0}[{2}Available{0}]{2}- {0}v.{7}{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, x[0], z[0]))
        sleep(5)
def checkjp2a():
    system('clear')
    if 256 != system('which jp2a > /dev/null'):
        print(" {0}[{2}*{0}] {2}JP2A INSTALLATION FOUND....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(1)
    else:
        print("{0}[{2}*{0}] {2}JP2A NOT FOUND\n {0}[{2}*{0}] {2}Installing PHP... ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        system('apt-get install jp2a > /dev/null')
        exit()

def checkwget():
    system('clear')
    if 256 != system('which wget > /dev/null'):
        print(" {0}[{2}*{0}] {2}WGET INSTALLATION FOUND....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(1)
    else:
        print("{0}[{2}*{0}] {2}WGET NOT FOUND\n {0}[{2}*{0}] {2}Installing PHP... ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        system('apt-get install wget > /dev/null')
        exit()

def checkPHP():
    if 256 != system('which php > /dev/null'):
        print(" {0}[{2}*{0}] {2}PHP INSTALLATION FOUND.....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(1)
    else:
        print("{0}[{2}*{0}] {2}PHP NOT FOUND\n {0}[{2}*{0}] {2}Installing PHP... ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        system('apt-get install php > /dev/null')
        exit()

def checkNgrok():
    if path.isfile('Server/ngrok') == False:
        print(' {0}[{2}*{0}]{2} Ngrok Not Found {0}!!'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        print(' {0}[{2}*{0}]{2} Downloading Ngrok...{5}'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):
            filename = 'ngrok-stable-linux-arm.zip'
            url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
            req=system('wget {0}'.format(url))
            #with open(filename, "wb") as file_obj:
            #file_obj.write(req.content)
            system('unzip ' + filename)
            system('mv ngrok Server/ngrok')
            system('rm ' + filename)
            system('chmod +x ngrok')
            system('clear')
            print("{1} ".format(GREEN, DEFAULT, RED)) 
            exit()
        else:
            ostype = systemos().lower()
            if architecture()[0] == '64bit':
                filename = 'ngrok-stable-{0}-amd64.zip'.format(ostype)
            else:
                filename = 'ngrok-stable-{0}-386.zip'.format(ostype)
        url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
        req=system('wget {0}'.format(url))
        #with open(filename, "wb") as file_obj:
            #file_obj.write(req.content)
        system('unzip ' + filename)
        system('mv ngrok Server/ngrok')
        system('rm ' + filename)
        system('clear')
        print("{4} ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW)) 
        exit() 
    else:
        print(" {0}[{2}*{0}] {2}NGROK INSTALLATION FOUND......".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(1)

def checkLocalxpose():
    if path.isfile('Server/loclx') == False:
        print(' {0}[{2}*{0}]{2} Localxpose Not Found {0}!!'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        print(' {0}[{2}*{0}]{2} Downloading Localxpose...{5}'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):
            filename = 'loclx-linux-arm.zip'
            url = 'https://lxpdownloads.sgp1.digitaloceanspaces.com/cli/'+filename
            req=system('wget {0}'.format(url))
            #with open("{0}", "wb".format(filename)) as file_obj:
            #file_obj.write(req.content)
            system('unzip {0} && rm {0}'.format(filename))
            system('mv loclx-linux-* loclx && chmod +x loclx && mv loclx Server/')
            #system('chmod +x loclx')
            print("{4} ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
            exit()
        else:
            ostype = systemos().lower()
            if architecture()[0] == '64bit':
                filename = 'loclx-linux-amd64.zip'.format(ostype)
            else:
                filename = 'loclx-linux-386.zip'.format(ostype)
        url = 'https://lxpdownloads.sgp1.digitaloceanspaces.com/cli/'+filename
        req=system('wget {0}'.format(url))
        #with open("{0}", "wb".format(filename)) as file_obj:
            #file_obj.write(req.content)
        system('unzip {0} && rm {0}'.format(filename))
        system('mv loclx-linux-* loclx && mv loclx Server/')
        print("{1} ".format(GREEN, DEFAULT, RED)) 
        exit()
    else:
        print(" {0}[{2}*{0}] {2}LOCALXPOSE INSTALLATION FOUND.....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(1)


