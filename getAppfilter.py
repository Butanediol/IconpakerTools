import json as JS
from urllib.request import urlopen
from pprint import pprint
import _thread

def getInfo():

	appName = input('请输入应用名')
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

getInfo()



	# <item component="ComponentInfo{com.oblatum.iconpack/com.by_syk.lib.nanoiconpack.MainActivity}" drawable="oblatum_icon_pack" />