import xml.etree.ElementTree as XET
import os

def analyseAppfilter():
	appfilterFileLocation = str(path)+'/appfilter.xml'
	xmlTree = XET.parse(appfilterFileLocation)
	xmlRoot = xmlTree.getroot()
	childAttribution = ''
	childAttributionPackageName = ''
	childAttributionLaunchActivity = ''
	childAttributionIconName = ''
	print('\nxmlRoot.tag:',xmlRoot.tag,'\nxmlRoot.attrib:',xmlRoot.attrib,'\nxmlRoot.text:',xmlRoot.text)

	counts = 0

	for child in xmlRoot:
		if child.tag == 'item':
			childAttribution = str(child.attrib)
			# print(childAttribution)
			childAttributionPackageName = childAttribution[29:childAttribution.index('/')] # 获取包名
			childAttributionLaunchActivity = childAttribution[childAttribution.index('/')+1:childAttribution.index('}')] #获取启动项
			childAttributionIconName = childAttribution[childAttribution.index('}')+17:childAttribution.index("'}")] # 获取图标名

			if(childAttributionIconName):
				cmd = 'cp ' + path + '/' + childAttributionIconName + '.png ' + path + '/output/' + childAttributionPackageName + '.png'
				# print(childAttributionIconName)
				os.system(cmd)
				counts += 1
	print('\n' + str(counts) + ' in total.')

# path = input('')
print("Please input the dir path.")
path = input('Appfilter.xml must included.\n')
os.system('mkdir ' + path + '/output')
analyseAppfilter()
