import requests
import urllib
from bs4 import BeautifulSoup
import re
import os
import random
import time
import xlwt


#打开网址
def dakaiwangye(num,n):
	#ip代理切换仍需摸索
	#
	#proxy_handler = urllib.request.ProxyHandler({'http':'125.112.173.11:47193'})  
	#opener = urllib.request.build_opener(proxy_handler) 
	#urllib.request.install_opener(opener)  
	url='http://www.dianping.com/shop/32864388/review_all/p'+str(num)

	n=n*2
	user_agent= 'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0'
	#cookie 可能也可以固定不换
	cookie='hc.v=a86df87e-bb98-81ee-ec57-849bed114334.1518073076; _lxsdk_cuid=1617434dc8ac8-05e0619dd9cd69-32677403-13c680-1617434dc8bc8; _lxsdk=1617434dc8ac8-05e0619dd9cd69-32677403-13c680-1617434dc8bc8; s_ViewType=10; JSESSIONID=A63DFECF3B9334A6906693F515655FB5; thirdtoken=A63DFECF3B9334A6906693F515655FB5; _lxsdk_s=1621d149194-b21-e00-d33%7C%7C'+str(n)
	

	headers={'User-Agent':user_agent,'Cookie':cookie}
	req = urllib.request.Request(url=url,headers=headers)

	respone=urllib.request.urlopen(req)

	html=respone.read().decode('utf-8')
	return html

#处理数据
def handledate(content):
	alldata=[]
	relink = '<span class="sml-rank-stars sml-str(.*) star">'
	
	star = re.findall(relink,content)
	
	#其他
	soup=BeautifulSoup(content)
	s=soup.find_all('span',class_="score")
	s2=soup.find_all('span',class_="time")
	number=0
	for a in s:
		st=[]
		
		st.append(star[number])
		
	#时间
		relink6 = '<span class="time">\n(.*)'
		times = re.findall(relink6,str(s2[number]))
		times[0]=times[0].rstrip()

	#口味
		relink2 = '口味：(.*)'
		kouwei=re.findall(relink2,str(a))
	#环境
		relink3 = '环境：(.*)'
		huanjing=re.findall(relink3,str(a))
	#服务
		relink4 = '服务：(.*)'
		fuwu=re.findall(relink4,str(a))
	#人均
		relink5 = '人均：(.*)</span>'
		renjun=re.findall(relink5,str(a))
		
		hebing=times+st+kouwei+huanjing+fuwu+renjun
		number=number+1
		alldata.append(hebing)
		
	return alldata
#存储数据至excel
def savedata(li):
	book=xlwt.Workbook(encoding='utf-8')
	booksheet=book.add_sheet('Sheet 1', cell_overwrite_ok=True) 
	for i,p in enumerate(li):
		for j,q in enumerate(p):
			
			booksheet.write(i,j,q)
	book.save('grade5.xls')


num=4
n=1
data=[]
while num<=4:
	html=dakaiwangye(num,n)
	handle_data=handledate(html)
	data=data+handle_data
	print('正在录入第%d页'%num)
	savedata(data)
	num=num+1
	time.sleep(3)
	


