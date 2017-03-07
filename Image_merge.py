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
	pattern = re.compile(r'"objURL":"(.+?.jpg)",')
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
def image_reszie():
	current_path = os.getcwd()
	res =  os.path.isdir(os.path.join(current_path, 'resize_image'))
	if not res:
		os.mkdir(os.path.join(current_path, 'resize_image'))
	resize_image_folder = os.path.join(current_path, 'resize_image')

	for i in range(1,251):
		try:
			im = Image.open(os.path.join(pic_path, 'image_%04d.jpg' %i))
		except 	Exception, e:
			print e
		else:
			im2 = im.resize((20, 20))
			im2.save(os.path.join(resize_image_folder,'image_%04d.jpg' %i))
			im.close()
def image_merge():
	new_image = Image.new('RGBA',(1000, 1000),(255, 255, 255))
	resize_image_folder = os.path.join(current_path, 'resize_image')
	m = 1
	try:
		im = Image.open(os.path.join(current_path, 'cat.png'))
	except Exception, e:
		return e
	for i in range(1,51):
		for j in range(1,51):
			try:
				im_resize = Image.open(os.path.join(resize_image_folder, 'image_%04d.jpg' %m))
				im_resize = im_resize.convert('RGBA')
			except Exception, e:
				print e
			else:
				background_pixel = im.getpixel((10*i, 10*j))
				background = Image.new('RGBA',(20, 20),(background_pixel[0],background_pixel[1],background_pixel[2]))
				image_res = Image.blend(im_resize, background, 0.5)
				x0 = (j-1)*20
				y0 = (i-1)*20
				x1 = j*20
				y1 = i*20
				new_image.paste(image_res, (x0, y0, x1, y1))
				im_resize.close()
				m += 1

	new_image.save('image_merge.png')
	im.close()

main(1200)