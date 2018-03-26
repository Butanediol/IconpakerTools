# -*- coding: utf-8 -*-

import xml.etree.ElementTree as XET
import os
path = input()
files = os.listdir(path) #文件列表
filesCode = str(path)+'/code.xml' #xml文件路径
outputPath = str(path)+'/output' #输出文件路径
# print(filesCode)
f = open(filesCode,'w')

files.sort()

for file in files:
	if (file != '.DS_Store') & (file != 'code.xml'):
		f.write('<item>')
		f.write(file[:-4])
		f.write('</item>')
		f.write('\n')

f.write('\n')

for file in files:
	if (file != '.DS_Store') & (file != 'code.xml'):
		f.write('''<item drawable="''')
		f.write(file[:-4])
		f.write('''" />''')
		f.write('\n')

f.write('\n')

# 接下来是xml文件

appfilterFileLocation = str(path)+'/appfilter.xml'
xmlTree = XET.parse(appfilterFileLocation)
xmlRoot = xmlTree.getroot()
childAttribution = ''
childAttributionPackageName = ''
childAttributionLaunchActivity = ''
childAttributionIconName = ''
print('\nxmlRoot.tag:',xmlRoot.tag,'\nxmlRoot.attrib:',xmlRoot.attrib,'\nxmlRoot.text:',xmlRoot.text)
for child in xmlRoot:
	if child.tag == 'item':
		childAttribution = str(child.attrib)
		# print(childAttribution)
		childAttributionPackageName = childAttribution[29:childAttribution.index('/')] # 获取包名
		childAttributionLaunchActivity = childAttribution[childAttribution.index('/')+1:childAttribution.index('}')] #获取启动项
		childAttributionIconName = childAttribution[childAttribution.index('}')+17:childAttribution.index("'}")] # 获取图标名
		# print('包名是 ',childAttributionPackageName)
		# 输出包名
		f.write('包名是 ')
		f.write(childAttributionPackageName)
		f.write('\n')
		# 输出启动项
		f.write('启动项 ')
		f.write(childAttributionLaunchActivity)
		f.write('\n')
		# 输出图标名
		# print('图标名 ',childAttributionIconName)
		print('属性 ',childAttribution)
		f.write('图标名 ')
		f.write(childAttributionIconName)
		f.write('\n\n')





	# print('\nchild-tag是：',child.tag,'\nchild.attrib：',child.attrib,'\nchild.text：',child.text)
# 	for sub in child:
# 		print('\nsub-tag是：',sub.tag,'\nsub.attrib：',sub.attrib,'\nsub.text：',sub.text)

f.close() 		
