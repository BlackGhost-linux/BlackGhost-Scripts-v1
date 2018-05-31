import urllib
import urlparse
import os
import re
from time import sleep
from datetime import date
def welcome(modulename):

  print  """
###########################################################################
      _________                                   _________ ___________
     /   _____/ __M-TECHNOLOGY________________   /   _____/ \__    ___/
     \_____  \_/ __ \_  __ \  \/ _/ __ \_  __ \  \_____  \    |    |   
     /        \  ___/|  | \/\   /\  ___/|  | \/  /        \   |    |   
    /_______  /\___  |__|    \_/  \___  |__|    /_______  /   |____|   
            \/     \/                 \/                \/ 2016/2017  
                          Server Scanning Tool
    ( Joomla , wordpress , Blogger , Drupa ) >====[ SQL Injection ]  V2.1.0
###############################################( www.m-technology.ml )#####

        """
  print  '#######    ' + modulename

###########################################################
def sqlihunt(dork , filename ):

  # extract Urls from a Bing search engin querying the given dork and test every url in 
  # the result is stored in a text file 
  file2 =open(filename+'.txt','w')
  start=0
  end=200
  sleep(3)
  print "[info]Getting Websites From Bing ... "
  while start<=end :
    try:
      con = urllib.urlretrieve('http://www.bing.com/search?q='+dork+"&first="+str(start))
      #con = con = urllib.urlretrieve('http://www.bing.com/search?q=ip%3A41.203.11.42+%22php%3Fid%3D%22&go=&qs=ds&form=QBLH&filt=all')
      conf = open(con[0])
      readd=conf.read()
      find=re.findall('<h2><a href="(.*?)"',readd)
      start = start+10
      #return find 
    except IOError:
      print "[ERROR]network error "
      print "[Info]reconnecting "
      sleep(10)
      print "[Info]retrying "
    try :
      for i in range(len(find)):
                  rez=find[i]+"'"
                  tst = urllib.urlretrieve(rez)
                  tstf = open(tst[0])
                  tstdd= tstf.read()
                  tstfind=re.findall('/error in your SQL syntax|mysql_fetch_array()|execute query|mysql_fetch_object()|mysql_num_rows()|mysql_fetch_assoc()|mysql_fetch_row()|SELECT * FROM|supplied argument is not a valid MySQL|Syntax error|Fatal error/i|You have an error in your SQL syntax|Microsoft VBScript runtime error',tstdd)
                  if(tstfind):
                    print "[SLQ] : "+ rez 
                    file2.write(rez + '\n')
                  else:
                    print "[No SQL ] : " + rez
    except IOError:
      print "[ERROR]No result found"

############################################################
def serverTargeting(IP):
  welcome("perform many  scans to target the given server's IP ")
  os.system("mkdir "+IP)
  #fil = open(logsfilename+'.txt','a')
  #fil.write("[Info] : new target "+now.strftime("%A %d %b %Y")+"IP adress : "+IP)
  #print "[Info] : new target "+now.strftime("%A %d %b %Y")+"IP adress : "+IP
  #fil.write("[Info] : getting links from Bing")
  print " New TARGET " + IP
  print "[Info] : getting Hosted domains from Bing"
  file2 =open(IP+'/hosted-MTD.txt','w')
  start=0
  end=200
  sleep(3)
  dork = 'IP:'+IP
  #print "[info]Getting Websites From Bing ... "
  while  start <= end :
    try:
      con = urllib.urlretrieve('http://www.bing.com/search?q='+dork+"&first="+str(start))
      #con = con = urllib.urlretrieve('http://www.bing.com/search?q=ip%3A41.203.11.42+%22php%3Fid%3D%22&go=&qs=ds&form=QBLH&filt=all')
      conf = open(con[0])
      readd=conf.read()
      find=re.findall('<h2><a href="(.*?)"',readd)
      start = start+10
    except IOError:
      print "[ERROR]network error "
      print "[Info]reconnecting "
      sleep(10)
      print "[Info]retrying "
    try :

      for i in range(len(find)):
       rez=find[i]
       file2.write(urlparse.urlparse(rez).netloc + '\n')
    except IOError:
      print "[ERROR]No result found"
  print "[Info] : links list saved in file "+IP+"hosted-MTD.txt"
  print "[Info] : getting wordpress sites from server ...."

  
  file2 =open(IP+'/WordPress-MTD.txt','w')
  start=0
  end=200
  sleep(3)
  dork = 'IP:'+IP + "  /wp-content/"
  wplist = []
  #print "[info]Getting Websites From Bing ... "
  while  start <= end :
    try:
      con = urllib.urlretrieve('http://www.bing.com/search?q='+dork+"&first="+str(start))
      #con = con = urllib.urlretrieve('http://www.bing.com/search?q=ip%3A41.203.11.42+%22php%3Fid%3D%22&go=&qs=ds&form=QBLH&filt=all')
      conf = open(con[0])
      readd=conf.read()
      find=re.findall('<h2><a href="(.*?)"',readd)
      start = start+10
    except IOError:
      print "[ERROR]network error "
      print "[Info]reconnecting "
      sleep(10)
      print "[Info]retrying "
    try :

      for i in range(len(find)):
       rez=find[i]
       wplist.append(rez)
       file2.write(urlparse.urlparse(rez).netloc  + '\n')
    except IOError:
      print "[ERROR]No result found"
  
  #getsitesbing("IP:"+IP+" /wp-content/" , 'wp_Powred' )
  print "[Info] : links list saved in file "+IP+"WordPress-MTD.txt"
  print "[Info] : getting joomla sites from server ...."

   
  file2 =open(IP+'/joomla-MTD.txt','w')
  start=0
  end=200
  joomlist = []
  sleep(3)
  dork = 'IP:'+IP +" index.php?option=com_content"
  #print "[info]Getting Websites From Bing ... "
  while  start <= end :
    try:
      con = urllib.urlretrieve('http://www.bing.com/search?q='+dork+"&first="+str(start))
      #con = con = urllib.urlretrieve('http://www.bing.com/search?q=ip%3A41.203.11.42+%22php%3Fid%3D%22&go=&qs=ds&form=QBLH&filt=all')
      conf = open(con[0])
      readd=conf.read()
      find=re.findall('<h2><a href="(.*?)"',readd)
      start = start+10
    except IOError:
      print "[ERROR]network error "
      print "[Info]reconnecting "
      sleep(10)
      print "[Info]retrying "
    try :

      for i in range(len(find)):
       rez=find[i]
       joomlist.append(rez)
       file2.write(urlparse.urlparse(rez).netloc  + '\n')
    except IOError:
      print "[ERROR]No result found"
  
  #getsitesbing("IP:"+IP+" index.php?option=com_content" , 'joom_Powred' )

  print "[Info] : links saved in file "+IP+"joomla-MTD.txt"
  print " ALL is done good luck dude !!!!! "
  print " starting SCanning phase for worpress sites Using wpscan"
  os.system("mkdir "+IP+"/wpscan_results")
  wps = set(wplist)
  for url in wps:
    print " Scanning  "+urlparse.urlparse(url).netloc
    os.system("wpscan --url "+urlparse.urlparse(url).netloc+"| tee "+IP+"/wpscan_results/"+urlparse.urlparse(url).netloc+".txt")
    print urlparse.urlparse(url).netloc+"  SCANNED "
  print " ALL wordpress Sites were scanned NOw scanning Joomla sites using Joomscan"
  os.system("mkdir "+IP+"/joomscan_results")
  joomlas = set(joomlist)
  for url in joomlas:
    print " Scanning "+urlparse.urlparse(url).netloc
    os.system("joomscan -u "+urlparse.urlparse(url).netloc+" tee "+IP+"/joomscan_results/"+urlparse.urlparse(url).netloc+".txt")
    print " SCANNED " +urlparse.urlparse(url).netloc
###########################################################
welcome("Server Scanning Tool ( MTD ) ")
IPadress=raw_input("[INFO] : enter IP adress  : ")
serverTargeting(IPadress)
sqlihunt("IP:"+IPadress+" id =" , IPadress+"/SQLinjectable-MTD.txt" )