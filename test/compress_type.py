zip, tar.gz, gz
# 
def compress(filelist,path):
	postfix = os.path.split(path)[1].split('.')[1]
	if postfix == 'zip':
		# zip_cop
	if postfix == 'tar':
		# tar_cop
	if postfix == 'gz':
		# gz_cop
	return path
def decompress(decompressfile,path):
	postfix = os.path.split(decompressfile)[1].split('.')[1]
	if postfix == 'zip':
		# zip_decop
	if postfix == 'tar':
		# tar_decop
	if postfix == 'gz':
		# gz_decop
	return path
# 
def uppername():
	pass

