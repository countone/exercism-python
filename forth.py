operators = ['*','+','-','/','OVER','DROP','DUP','SWAP']
class StackUnderflowError(Exception):
	pass


def evaluate(input_data):
	user_def_operators = {}

	defintions = [lines.upper() for lines in input_data[:-1]]
	statement  = input_data[-1].upper()
	if statement.startswith(':'):
		raise ValueError('ValueError')
	#defintions = [[lines.split(' ')] for lines in defintions]
	#defintions = [lists[1:-1] for lists in defintions]
	if defintions:
		temp = defintions[0].split(' ')
		user_def_operators[temp[1]] = (' ').join(temp[2:-1])
	for defintion in defintions[1:]:
		temp = defintion.split(' ')
		rhs = temp[2:-1]
		for i in range(len(rhs)):
			if rhs[i] in user_def_operators.keys():
				rhs[i] = user_def_operators[rhs[i]]
		temp = temp[:2] + rhs
		user_def_operators[temp[1]] = (' ').join(temp[2:])
	for key, value in user_def_operators.items():
		statement = statement.replace(key, value)
	statement = statement.split(' ')

	for items in statement:
		try:
			int(items)
		except ValueError:
			if items not in operators:
				raise ValueError('ValueError')
	data 	= []
	operator = []

	while True:
		for i in range(len(statement)):
			try:
				if statement[i] == 'DUP':
					if len(statement) > 1:
						statement[i] = statement[i-1]
					else:
						raise StackUnderflowError('StackUnderflowError')
				elif statement[i] == 'OVER':
					if len(statement) > 2:
						statement[i] = statement[i-2]
					else:
						raise StackUnderflowError('StackUnderflowError')
					
				elif statement[i] == 'DROP':
					if len(statement) > 1:
						pass
					else:
						raise StackUnderflowError('StackUnderflowError')
					if i == len(statement)-1:
						statement = statement[:i-1]
					else:
						statement = statement[:i-1]+statement[i+1:]
					break
				elif statement[i] == 'SWAP':
					if len(statement) > 2:
						pass
					else:
						raise StackUnderflowError('StackUnderflowError')
					if i == len(statement)-1:
						statement = statement[:i-2] + [statement[i-1],statement[i-2]]
					else:
						statement = statement[:i-2] + [statement[i-1],statement[i-2]] + statement[i+1:]
					break
				elif statement[i] == '+':
					if len(statement) >= 3:
						pass
					else:
						raise StackUnderflowError('StackUnderflowError')
					if i == len(statement)-1:
						statement = [int(statement[i-2])+int(statement[i-1])]
					else:
						statement = [int(statement[i-2])+int(statement[i-1])] + statement[i+1:]
					break
				elif statement[i] == '-':
					if len(statement) >= 3:
						pass
					else:
						raise StackUnderflowError('StackUnderflowError')
					if i == len(statement)-1:
						statement = [int(statement[i-2])-int(statement[i-1])]
					else:
						statement = [int(statement[i-2])-int(statement[i-1])] + statement[i+1:]
					break
				elif statement[i] == '/':
					if len(statement) >= 3:
						pass
					else:
						raise StackUnderflowError('StackUnderflowError')
					if i == len(statement)-1:
						statement = [int(statement[i-2])/int(statement[i-1])]
					else:
						statement = [int(statement[i-2])/int(statement[i-1])] + statement[i+1:]
					break
				elif statement[i] == '*':
					if len(statement) >= 3:
						pass
					else:
						raise StackUnderflowError('StackUnderflowError')
					if i == len(statement)-1:
						statement = [int(statement[i-2])*int(statement[i-1])]
					else:
						statement = [int(statement[i-2])*int(statement[i-1])] + statement[i+1:]
					break

			except IndexError:
				raise StackUnderflowError('StackUnderflowError')
		
		for i in range(len(statement)):
			try:
				int(statement[i])
			except ValueError :
				break
			else:
				statement[i]=int(statement[i])
		else:
			break
	return statement

			



		
