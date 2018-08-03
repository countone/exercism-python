def encode(numbers):
	numbers=[bin(num) for num in numbers ]
	binary= [str(num) for num in numbers]
	binary= [num[2:] for num in numbers]
	binary= ['0'*(-len(num)%7)+num for num in binary]
	encoded=[]
	for num in binary:
		byte= len(num)//7
		for i in range(byte):
			if len(num)==7:
				encoded.append('0'+num)
				break
			else:
				encoded.append('1'+num[:7])
				num= num[7:]

	encoded=[int(num,base=2) for num in encoded]
	
	return encoded

def decode(bytes_):
	
	numbers=[str(bin(b)) for b in bytes_]
	numbers=[b[2:].rjust(8,'0') for b in numbers]
	decoded=[]
	data=''
	for num in numbers:
		
		if num[0]=='1':
			data+=num[1:8]
			num=num[8:]
		elif num[0]=='0':
			data+= num[1:]
			decoded.append(data)
			data=''
	if not decoded:
		raise ValueError('ValueError')
	decoded=[int(m,base=2) for m in decoded]
	return decoded

