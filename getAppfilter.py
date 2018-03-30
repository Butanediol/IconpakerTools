import json as JS
from urllib.request import urlopen
from pprint import pprint
import _thread
import config as CF

def getInfo(appName):

	# appName = input('请输入应用名')
	appNameLink = 'http://nano.by-syk.com:8083/code/' + appName
	appNameURL = urlopen(appNameLink)
	apiResponsed = JS.loads(appNameURL.read().decode('utf-8'))

	num = 0
	for i in apiResponsed['result']:
		print('第',num+1,'个结果：')
		print('应用名称 ',apiResponsed['result'][num]['label'])
		print('英文名称 ',apiResponsed['result'][num]['labelEn'])
		print('应用包名 ',apiResponsed['result'][num]['pkg'])
		print('启动项名 ',apiResponsed['result'][num]['launcher'])
		print('申请数量 ',apiResponsed['result'][num]['sum'])
		appfilterCode = '''应用代码  <item component="ComponentInfo{'''
		appfilterCode += apiResponsed['result'][num]['pkg']
		appfilterCode += '/'
		appfilterCode += apiResponsed['result'][num]['launcher']
		appfilterCode += '''" drawable="'''
		appfilterCode += appName
		appfilterCode += '''" />'''
		print(appfilterCode,'\n')
		num += 1

if CF.infiniteLoop:
	cntinue = True
	while cntinue:
		getName = input('请输入应用名/包名(输入#停止)')
		if getName == '#':
			break
		getInfo(getName)
else:
	getName = input('请输入应用名/包名')
	getInfo(getName)
