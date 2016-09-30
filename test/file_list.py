"""
import os
os.chdir('F:/Save')
folder_list = os.walk('F:/Save')
with open('file_list.txt','w') as f:
	f.write(str(folder_list.next()))
"""
# win 默认路径分隔符：反斜杠'\'
# nix 默认路径分隔符：正斜杠'/'
import os
import os.path
rootdir = 'F:/Save/Ziguang'  # 指明被遍历的文件夹
# walk 遍历返回一个三元组(1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字)
for parent, dirnames, filenames in os.walk(rootdir):
	# 输出文件夹信息
    for dirname in dirnames:
        print "dir's parent is " + parent
        print "dir's dirname is " + dirname
    # 输出文件信息
    for filename in filenames:
        print "file's parent is " + parent
        print "file's filename is " + filename
        # 输出文件路径信息
        print "file's the full name of the file is " + os.path.normcase(os.path.join(parent, filename))