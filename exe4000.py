from executor import executor
import db
import urllib,urllib2
import json

class exe4000(executor):

	def cmd_name(self):
		return 'show me the movie'
	
	def	help(self):
		return 'usage => to:help@dianping.com subject:show me the movie?[movie name]'
		
	
	def biz(self, m):
		keyword = m.para.encode('utf8')
		para = {'searchkeyword' : keyword}
		s = urllib.urlencode(para)
		url = 'http://192.168.8.98:9099/dp-searcher/search?appname=AppName.FTPFILE&s=0&n=15&fl=filename,fullftppath&' + s
		#print url
		#exit()
		n = urllib2.urlopen(url).read()
		res = json.loads(n)
		
		if len(res['records']) == 0:
			return 'movie not found.'
		else:
			txt = ''
			for i in res['records']:
				txt = txt + i['filename'] + '\n'
				txt = txt + i['fullftppath'] + '\n\n'
			return {'body':txt}
		




