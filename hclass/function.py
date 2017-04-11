# coding=utf-8
import os,threading,os,Queue,time,thread,re
from simple import *

"""读目录下文件"""

def dirfile(path): #读目录下文件名
	list_file = os.listdir(path);
	return list_file;

def textfile(file):
	f = open(file);
	lines = f.readlines();#读取全部内容 
	return lines;

"""判断cms"""

#请求,并且批评内容
def if_cms(url,cmsurl,cmsmatching,cmsname,q):
	if not re.match(r"^https?://",url):
		url = "http://"+url;
		http = httprequest();
		try:
			html2 = http.get_http(url+cmsurl);
			status_code = html2.status_code;
		except Exception,e:
			html2 = "11111111111111111111111111111111"
			#print "\033[1;31;1m function : if_cms  errer: %s  \033[0m" % e;
		if html2 != "11111111111111111111111111111111":
			if status_code == 200 and re.findall(r"%s" % cmsmatching , html2.text.encode('utf-8') , re.I):
				q.put(cmsname);

def for_if_cms(url,file3,q):
	tsk = [];
	#print url,file3;
	if q.empty():
		xxcms_list = textfile(file3);
		for i, cms in enumerate(xxcms_list):
			i=i+1;
			#识别的字典，匹配内容，cms名字
			cmsurl,cmsmatching,cmsname = cms.split('------')
			
			if q.empty():
				if len(tsk) < 30:
					t = threading.Thread(target=if_cms,args=[url,cmsurl,cmsmatching,cmsname,q]); #函数名称
					t.start();
					tsk.append(t) #设置T线程等待结束
				else:
					print 'Wait for thread end !';
					for tt in tsk:
						tt.join()
					tsk = [];
			else:
				#thread.exit()  #结束当前线程
				break;
			time.sleep(0.2);


