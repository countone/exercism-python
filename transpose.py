def transpose(input_lines):
	input_lines=input_lines.split('\n')
	length=[]
	for i in range(len(input_lines)):
		length.append(len(input_lines[i]))

	max_length= max(length)

	for i in range(len(input_lines)):
		extra=len(input_lines[i])
		for j in range(i,len(input_lines)):
			if extra<len(input_lines[j]):
				extra=len(input_lines[j])
		if extra>len(input_lines[i]):
			input_lines[i]=input_lines[i]+' '*(extra-len(input_lines[i]))

	transpose=[]
	for i in range(max_length):
		item=''
		for j in range(len(input_lines)):
			try:
				item+=input_lines[j][i]
			except IndexError:
				pass
		transpose.append(item)

	return '\n'.join(transpose)