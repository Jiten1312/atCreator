import csv
import os
import time
from datetime import datetime
import shutil
path='C:/Users/Jitn dhimmar/Downloads'
dest='C:/Users/Jitn dhimmar/Desktop/attendance'

def getSlot(h,m):
	if h==7:
		if m>=30:
			return 1

	if h==8:
		if m<=25:
			return 1
		elif m>=35:
			return 2

	if h==9:
		if m<=30:
			return 2
		elif m>=50:
			return 3
	if h==10:
		if m<=45:
			return 3
		elif m>=55:
			return 4

	if h==11:
		if m<=50:
			return 4

def getClass(slot,day):
	if day=='Mon':
		l=['(7.30) T.Y.B.Com 6 Ad Ac & Aud 6','(8.35) T.Y.B.Com 5 Ad Ac & Aud 6','','(10.55) T.Y.B.Com 4 Ad Ac & Aud 6']
		print(slot-1)
		return l[slot-1]
	if day=='Tue':
		l=['','(8.35) M.Com 2 F & M Ac 6','(9.50) S.Y.B.Com 4 AC & TAX 3','(10.55) S.Y.B.Com 6 AC & TAX 3']
		return l[slot-1]
	if day=='Wed':
		l=['(7.30) M.Com 2 F & M Ac 6','(8.35) T.Y.B.Com 5 Ad Ac & Aud 6','(9.50)T.Y.B.Com 4 Ad Ac & Aud 6','(10.55)S.Y.B.Com 4 AC & TAX 3']
		return l[slot-1]
	if day=='Thu':
		l=['(7.30) S.Y.B.Com 4 AC & TAX 3','(8.35) T.Y.B.Com 4 Ad Ac & Aud 6','(9.50) S.Y.B.Com 4 AC & TAX 3','(10.55)T.Y.B.Com 5 Ad Ac & Aud 6']
		return l[slot-1]
	if day=='Fri':
		l=['(7.30) T.Y.B.Com 6 Ad Ac & Aud 6','(8.35) S.Y.B.Com 5 AC & TAX 3','','(10.55) S.Y.B.Com 6 AC & TAX 3']
		return l[slot-1]
	if day=='Sat':
		l=['(7.30) S.Y.B.Com 5 AC & TAX 3','(8.35) S.Y.B.Com 6 AC & TAX 3','(9.50) T.Y.B.Com 6 Ad Ac & Aud 6','']
		return l[slot-1]		

try:
	for r,d,f in os.walk(path):
		for file in f:
			# meetingAttendanceList
			if 'meetingAttendanceList' in file:
				nname=""
				c_time=time.ctime(os.path.getctime(os.path.join(path,file)))
				# print(c_time)
				tlist=c_time.split(' ')
				day=tlist[0]
				month=tlist[1]
				date=tlist[2]
				if date=='':
					date=tlist[3]
					ttime=tlist[4]
				else:
					ttime=tlist[3]
				print(ttime)
				hm=ttime.split(':')
				# print(hm[1])
				print(file)
				slot=int(getSlot(int(hm[0]),int(hm[1])))
				nname=nname+date+" "+month+"-21"+getClass(slot,day)+'.csv'
				os.rename(os.path.join(path,file),os.path.join(path,nname))
				shutil.move(os.path.join(path,nname),dest)
				print(nname+' moved to '+dest)

				# converting
				dpath='C:/Users/Jitn dhimmar/Desktop/converted'
				sid=set()
				with open(os.path.join(dest,nname),'r',encoding='utf16') as csv_file:
					csvr=csv.reader(csv_file,delimiter='\t')

					cnt=0
					total=0
					for line in csvr:
						if len(line) < 3:
							continue
						if line[0].startswith('1') or line[0].startswith('2'):
							getId=line[0].split(' ')
							# print(getId[0])
							sid.add(line[0])

					with open(os.path.join(dpath,nname),'w',encoding='utf16') as csvw_file:
						# writer=csv.writer(csv_file)
						for s in sid:
							total=total+1
							getId=s.split(' ')
							# print(getId[0])
							id=int(getId[0])
							# print(id)
							csvw_file.write('%s\n'%id)
except Exception as e:
	print(e)
