#!/usr/bin/python2
#crontab set to 0,30 * * * *  //every 30min download latest comic...

import json
import urllib

url = 'http://dynamic.xkcd.com/api-0/jsonp/comic/'

if( urllib.urlopen(url).getcode() != 200 ) :
	exit()

output = json.load(urllib.urlopen(url))

urllib.urlretrieve(output['img'], "xkcd.png")
