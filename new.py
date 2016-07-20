# _*_coding:utf-8_*_

import os
import os.path
import csv
from datetime import date

root_dir = 'F:/Save/Ziguang'
csv_file = 'F:/Save/Ziguang/file_list.csv'

with open(csv_file, 'a') as csvfile:
	csvwriter = csv.writer(csvfile, dialect='excel')
	for parent, dirnames, filenames in os.walk(root_dir):
	    for filename in filenames:
	        path_str = os.path.normcase(os.path.join(parent, filename))
	        # csvwriter.writerow(path_str.split('\\'))
	        file_mtime = date.fromtimestamp(os.path.getmtime(path_str))
	        # print date.fromtimestamp(file_mtime)
	        print type(path_str.split('\\'))
	        csvwriter.writerow((file_mtime,path_str.split('\\')))