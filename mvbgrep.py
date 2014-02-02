# -*- coding: latin1 -*-

import urllib.request
import re, sys
from datetime import datetime, date, time
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from array import array
from operator import itemgetter
from xml.etree import ElementTree as ET
import argparse

station = ""
line_filter = ""
line_filter_b = False

current_date = datetime.now().date()
current_year = current_date.year
current_month = current_date.month
current_day = current_date.day
current_time = datetime.now().time()
current_min = current_time.minute
current_hour = current_time.hour

parser = argparse.ArgumentParser(prog="MVBgrep", description = "Get the current tram / bus informations.")
parser.add_argument("--version", action="version", version='%(prog)s 0.3')
parser.add_argument('-s', "--station", nargs="*", metavar="Station", dest = "station", required=True,help="the sataion name you want information about")
parser.add_argument('-l', "--line", nargs="*", metavar="Line", dest = "filter_stations", help="a tram / bus number you want to filter for")
parser.add_argument('-t', "--time", nargs="*", default=["30"], choices=["30", "60", "120"], dest = "set_time", help="how long in the future should the depature times be (default: %(default)s)")
parser.add_argument('--link', action="store_true", help="display the search link")
args = parser.parse_args();

second = False
for x in args.station:
	if second :
		station += "+" + x
		break
	second = True
	station += x

station = station.encode('utf-8')
station = re.sub(r"\\x", "%", "%s" %station)

station_data = urllib.request.urlopen("http://www.movi.de/mvb/fgi2/index.php?suggest=1&search=%s" %station)
station_data = station_data.read()
station_data = re.sub(r"\\x", "%", "%s" %station_data)
station_data = re.sub(r"b'", "", station_data)
station_data = re.sub(r"'", "", station_data)
station_data = re.sub(r" ", "%20", station_data)
station_data = station_data.split('###')

station_str = "http://www.movi.de/mvb/fgi2/index.php?send_request=yes&refnr_stationname="+str(station_data[0])+"&day="+str(current_day)+"&month="+str(current_month)+"&year="+str(current_year)+"&hour="+str(current_hour)+"&min="+str(current_min)+"&nextTime=" + args.set_time[0]
if args.link:
	print(station_str)


shedule_html = urllib.request.urlopen(station_str)

soup = BeautifulSoup(shedule_html)

if args.filter_stations:
	line_filter_b = True
	line_filter = str(args.filter_stations[0])

table = ET.XML(soup.table.prettify())
rows = iter(table)
headers = [col.text.strip() for col in next(rows)]
for row in rows:
    values = [col.text.strip() for col in row]
    result = dict(zip(headers, values))
    if line_filter_b and result["Linie"] == '0':
    	print(dict(zip(headers,values)))
    elif not line_filter_b:
    	print(dict(zip(headers,values)))
    


