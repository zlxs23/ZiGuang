import os
os.chdir('F:\Save\ZiGuang')
with open('content.txt', 'r') as file:
    content = file.readlines()
    content_keys = []
    content_values = []
for i in range(len(content)):
    content_keys.append(content[i][0:2].strip())
    content_values.append(content[i][2:content[i].find('\t')].strip())
content = dict(zip(content_keys, content_values))
print(content)