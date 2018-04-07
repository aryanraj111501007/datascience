import csv
import numpy as np
f=open('student-performance.csv',"r")
#ifile  = open('sample.csv', "rt", encoding=<theencodingofthefile>)
from numpy.linalg import inv
reader=csv.reader(f)

x=[]
for row in reader:
	x+=[row]
x=x[1:]



y=[]
for r in x:
	y+=[float(r[len(r)-1])]
	
def preprocessdata(x):
	X=[]
	for r in x:
		temp=[]
		#temp+=[int(r[2])]
		if r[0]=='Male':
			temp+=[1]
		else:
			temp+=[0]
		if r[4]=='A':
			temp+=[3]
		elif r[4]=='B':		
			temp+=[2]
		else:
			temp+=[1]
		if r[5]=='IT':
			temp+=[12]
		elif r[5]=='Math':		
			temp+=[11]
		elif r[5]=='Arabic':
			temp+=[10]
		elif r[5]=='Science':
			temp+=[9]
		elif r[5]=='English':
			temp+=[8]
		elif r[5]=='Quran':
			temp+=[7]
		elif r[5]=='French':
			temp+=[6]
		elif r[5]=='Spanish':
			temp+=[5]
		elif r[5]=='History':
			temp+=[4]
	
		elif r[5]=='Biology':
			temp+=[3]
	
	
		elif r[5]=='Chemistry':
	
			temp+=[2]		
		else:
			temp+=[1]	
		
		
		if r[6]=='First':
			temp+=[1]
		else:
			temp+=[2]
		if r[7]=='Father':
			temp+=[2]
		else:
			temp+=[1]
			
		
		temp+=[int(r[8])]
		temp+=[int(r[9])]
		temp+=[int(r[10])]
		temp+=[int(r[11])]
	
		if r[12]=='Yes':
	
			temp+=[2]		
		else:
			temp+=[1]
		
		if r[13]=='Good':
	
			temp+=[2]		
		else:
			temp+=[1]	
		
		if r[14]=='Under-7':

			temp+=[2]		
		else:
			temp+=[1]		
	
	
	
		X+=[temp]
	
	
	X=np.array(X)
	return X
	
def train(X1,Y1,sigma,lamda):
	k=np.matmul(inv(np.matmul(X1.T,X1)*(sigma/2) +(np.identity(12)*lamda/2)),np.matmul(X1.T,Y1)*sigma/2)
	return k

X=preprocessdata(x)	
w=train(X,y,2,4)
print('training-completed')

test_file=input("give filename to be tested\n")
f_test=open(test_file,'r')
x=[]
reader=csv.reader(f_test)
for row in reader:
	x+=[row]
x=x[1:]
X_test=preprocessdata(x)
print("the output is::")
predicted=np.matmul(X_test,w)
print(predicted)




	
	
	
	
