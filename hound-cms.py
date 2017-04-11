#coding:utf-8
from hclass.simple import *
from hclass.function import *
from hclass.data import *
from Queue import Queue;
import re,time,sys
reload(sys)
sys.setdefaultencoding('utf-8')


if __name__ == '__main__':
	httpget = httprequest();
	q= Queue();
	path = os.path.dirname(os.path.realpath(__file__));
	while True:
		mysql = data()
		tables_list =  mysql.tableshow()
		for table in tables_list: #遍历表
			if table != 'lis':
				if mysql.urlshow("select count(url) from %s where cms = '0'" % (table))[0]:
					sql = "select url from %s where cms = '0'" % (table);

					data_url = mysql.urlshow(sql);  #获取url
					for url in data_url:#遍历url
						if not simple(url):
							sql = "update %s set cms = null where url = '%s' " % (table,url);
							mysql.update(sql);
							continue;
						print "\033[4;32;1m Current domain : --->  %s \033[0m" % url ;
						cms_list = dirfile(path+"/cms/"); #获取cms文件匹配路径
						for cms in cms_list: #遍历路径
							sql = "update %s set cms = null where url = '%s' " % (table,url);
							mysql.update(sql)
							print "\033[1;33;1m  current path : %s  \033[0m" % cms;
							for_if_cms(url,path+"/cms/"+cms,q);
							time.sleep(0.2)
							if not q.empty():
								url_cms = q.get();
								sql = "update %s set cms = '%s' where url = '%s' " % (table,url_cms,url);
								mysql.update(sql)
								del url_cms;
								break;
								time.sleep(0.4);

		time.sleep(2);
		
