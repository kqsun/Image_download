#coding:utf-8
from PIL import Image
import urllib
import sys
import os
import re
reload(sys)
sys.setdefaultencoding('utf-8')
current_path = os.getcwd()
res = os.path.isdir(os.path.join(current_path, 'Pic'))
pic_path = os.path.join(current_path, 'Pic')
if not res:
	os.mkdir(os.path.join(current_path, 'Pic'))

def get_image(image_num,i = 1):
	url_search = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E7%8C%AB%E5%9B%BE%E7%89%87&pn='+str(image_num)
	html = urllib.urlopen(url_search).read()
#with open(os.path.join(current_path,'html.txt'), 'wb') as f:
	#f.write(html)
	pattern = re.compile(r'"objURL":"(.+?)",')
	image_url = pattern.findall(html)

	try:
		f = open(os.path.join(current_path, 'html.txt'),'a')
	except Exception, e:
		print e
	else:
		for url in image_url:
			f.write(url+'\n')
		f.close()
	for url in image_url:
		with open(os.path.join(pic_path, 'image_%04d.jpg' %i),'wb') as fb:
			try:
				html = urllib.urlopen(url)
			except Exception, e:
				print url + ' invalid'
			else:
				fb.write(html.read())
				i = i+1
	return i
def main(image_num):
	res = image_num%20
	if res != 0:
		print "image_num should be a multiple of 20"
	num = image_num/20
	number_image = 1
	for j in range(num):
		number_image = get_image(j*20, i = number_image)
main(80)