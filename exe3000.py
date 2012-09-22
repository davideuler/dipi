from executor import executor
import db
import urllib,urllib2
import config

class exe3000(executor):

	mobi_dic = {}
	
	def __init__(self):
		sql = 'select email, mobi from user'
		self.mobi_dic = db.query_dic(sql)

	def help(self):
		return 'usage => to:[email_users] cc:q@dianping.com subject:sms?[sms content]'

	
	def cmd_name(self):
		return 'sms'
	
	def biz(self, m):
		mobi_to = self.get_mobi_to(m.to)
		print 'send %s to %s' % (m.para, mobi_to)
		for n in mobi_to:
			self.send_sms(m.para, n)
		return {'body' : 'sms sent'}
	
	def get_mobi_to(self, mail_to):
		mobi_to = []
		for (key,value) in self.mobi_dic.iteritems():
			if key in mail_to : mobi_to.append(value)
		return mobi_to

	def send_sms(self, body, mobi):
		para = {'enterpriseid': config.EXE3000_ENTERPRISE_ID,'accountid': config.EXE3000_ACCOUNT_ID,'pswd':config.EXE3000_PWD, 'mobs' : mobi, 'msg' : body.encode('gbk')}
		s = urllib.urlencode(para)
		url = config.EXE3000_URL + s	
		n = urllib2.urlopen(url)




