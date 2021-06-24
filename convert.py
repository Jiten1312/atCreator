import csv
import os

path='C:/Users/Jitn dhimmar/Desktop/attendance'
dpath='C:/Users/Jitn dhimmar/Desktop/converted'
		
try:
	for r,d,f in os.walk(path):
		for file in f:
			sid=set()
			with open(os.path.join(path,file),'r',encoding='utf16') as csv_file:
				csvr=csv.reader(csv_file,delimiter='\t')
				index = 0
				
				cnt=0
				total=0
				for line in csvr:
					if len(line) < 3:
						continue
					if line[0].startswith('1') or line[0].startswith('2'):
						getId=line[0].split(' ')
						# print(getId[0])
						sid.add(line[0])

				with open(os.path.join(dpath,file),'w',encoding='utf16') as csv_file:
					# writer=csv.writer(csv_file)
					print(file)
					for s in sid:
						total=total+1
						getId=s.split(' ')
						# print(getId[0])
						id=int(getId[0])
						# print(id)
						csv_file.write('%s\n'%id)

				print(file+'\t'+str(total))
except Exception as e:
	print(e)