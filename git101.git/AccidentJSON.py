#-------------------------------------------------------------------------------
#-*-coding: utf-8 -*-
import urllib,urllib2,json,os,datetime
from xml.etree import ElementTree as ET
#reddit parse
##accident_file = urllib2.urlopen('http://event.longdo.com/feed')
#convert to string:
#######accident_data = accident_file.read()
#print accident_data
#close file because we dont need it anymore:
#accident_file.close()

Url = 'http://event.longdo.com/feed'
urllib.urlretrieve(Url, 'DATA.json')

tree = ET.parse('DATA.json')
root = tree.getroot()
# Read Json data and convert to text
geometry = '{\"geometry\" : {'
attributes = '\"attributes\" : {'
data = ""

print '\n'+"********************** STEP 1 **********************"
for child in root:
    print child.tag
print '\n'+"********************** STEP 2 **********************"
for neighbor in child:
        tag = neighbor.tag
        if tag == 'item':
            title = neighbor[0].text
            description = neighbor[6].text
            latitude = neighbor[3].text
            longitude = neighbor[4].text
            starttime = neighbor[7].text
            stoptime = neighbor[9].text
            pubdate = neighbor[13].text
            link = neighbor[1].text
            print title
            print description
            print latitude
            print longitude
            print starttime
            print stoptime
            print pubdate
            print link
            print '\n'
            field1 = '\"x\" : '+ longitude +', '
            field2 = '\"y\" : '+ latitude +'},'
            field3 = '\"' + 'TITLE' + '\" : ' + "\"" + title +"\"" +','
##            field4 = '\"' + 'DESCRIPTION' + '\" : ' + "\"" + description +"\"" +','
            field5 = '\"' + 'STARTTIME' + '\" : ' + "\"" + starttime +"\"" +','
            field6 = '\"' + 'STOPTIME' + '\" : ' + "\""+stoptime +"\""','
            field7 = '\"' + 'PUBDATE' + '\" : ' + "\""+pubdate +"\""','
            field8 = '\"' + 'LINK' + '\" : ' +"\"" +link +"\""'}},'
            body = geometry+field1+field2+'\n'+attributes+field3+field5+field6+field7+field8
            data = data + body
        else:
            pass
compleate_data = '[' + data[0:-1] + ']'
print compleate_data

print '\n'+"********************** STEP 3 **********************"
