from executor import executor
import os.path
import urllib,urllib2
import json
import imghdr

class exe5000(executor):
	
	def cmd_name(self):
		return 'show me the girl'
	
	def help(self):
		return 'usage => to:help@dianping.com subject:show me the girl?[girl name]'
	
	def biz(self, m):
		return self.get_girl(m.para)
	
	def get_girl(self, name):
		fn = name + '.png'
		if(os.path.exists(fn) and imghdr.what(fn)):
			return {"body":"your girl","file": fn}
		else:
			keyword = name.encode('utf8')
			para = {'q' : keyword}
			s = urllib.urlencode(para)

			url = 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&' + s
			
			response = urllib2.urlopen(url)
			res = json.load(response)
			for x in res['responseData']['results']:
				imurl = x['unescapedUrl']
				urllib.urlretrieve(imurl,fn)
				if imghdr.what(fn):
					return {"body":"Your Girl","file": fn}
		return {'body' : 'girl not found'}
