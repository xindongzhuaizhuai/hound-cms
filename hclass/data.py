#coding:utf-8
import MySQLdb,time;
class data():
	
	"mysql 登录"
	host = '127.0.0.1';
	user = 'root';
	passwd = 'zladmin';
	db = 'hound';
	port = 3306;
	charset = 'utf8';

	def __init__(self):
		try:
			self.db=MySQLdb.connect(host=data.host,user=data.user,passwd=data.passwd,charset=data.charset); #登录数据库
			
			self.mysql = self.db.cursor();#使用cursor()方法获取操作游标
			sql = "select schema_name from information_schema.schemata where schema_name='%s'" % (data.db);
			self.mysql.execute(sql); #提交数据


			if not self.mysql.fetchone():
				sql = "CREATE DATABASE IF NOT EXISTS %s " % (data.db);
				self.mysql.execute(sql);
				self.db.select_db(data.db) #选择数据库
			else:
				self.db.select_db(data.db) #选择数据库


		except Exception,e:
			print'\031[1;31;1m'+"Mysql Error: %s" % (e) + '\031[0m';
			exit();


	#查询所有表
	def tableshow(self):
		try:
			self.mysql.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '%s'" % (data.db));
			self.db.commit();
			ables = self.mysql.fetchall()
			tables_list = [];
			for x in ables:
				tables_list.append(x[0]);
			return tables_list;
		except Exception,e:
			print'\031[1;31;1m'+"Mysql Error: %s" % (e) + '\031[0m';
			exit();

	#查询所有url
	def urlshow(self,sql):
		try:
			url_list = [];
			urlshow = self.mysql.fetchmany(self.mysql.execute(sql));
			for url in urlshow:
				url_list.append(url[0])
			return url_list;
		except Exception,e:
			print'\031[1;31;1m'+"Mysql Error: %s" % (e) + '\031[0m';
			exit();



	#修改数据
	def update(self,sql):
		try:
			print sql;
			print '..>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>';
			self.mysql.execute(sql); #修改数据
			self.db.commit()
		except Exception,e:
			print'\031[1;31;1m'+"Mysql Error: %s" % (e) + '\031[0m';
			exit();







