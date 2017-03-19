#coding=utf-8
import requests,re,time


class httprequest(object):
	"""所有http请求类"""
	def __init__(self):
		self.header2 = {
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
		'Connection':'keep-alive',
		'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'};

	def get_http(self,url):
		try:
			print url;
			r = requests.get(url,headers=self.header2,timeout=5)  
			return r;
		except Exception,e:
			return "";
			print "\033[1;31;1m function : get_http errer: %s  \033[0m" % e;

	def post_http(self,url,h_type,data2):
		try:
			r = requests.post(url,headers=self.header2,data=data2,timeout=10)  
			if h_type == "h": #返回响应的请求头
				return r.headers
			elif h_type == "t":#返回源码
				return r.text.encode('utf-8');
		except Exception,e:
			print '\033[1;31;1m function : post_http  errer: %s \r \033[0m' % e;




