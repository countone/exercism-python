def chain(dominoes , last = None):
	
	chains = []

	if last:
		left = list(dominoes)
		start = left.pop(0)
		#print(dominoes,left,start,chains)
		#import code; code.interact(local=dict(globals(), **locals()))
		for j in range(len(left)):
			if start[1] == left[j][0]:
				chains.append(start)
				second = left.pop(j)
				# print(start,second,left)
				# print(1,chains,'start')
				rest = chain([second]+left,1)
				if len(rest) == len(left)+1:
					chains = chains + chain([second]+left,1)
				# print(1,chains,'stop')
				left.insert(j,second)
			elif start[1] ==  left[j][1]:
				chains.append(start)
				second = left.pop(j)
				# print(2,chains)
				rest = chain([(second[1],second[0])]+left,1	)
				if len(rest) == len(left) +1:
					chains = chains + chain([(second[1],second[0])]+left,1)
				# print(2,chains)
				left.insert(j,second)

			if len(chains) >= len(dominoes):
				break
			else:
				chains = []
		else:
				left.insert(0,start)
		if chains == [] and len(dominoes) ==1:
			chains = dominoes
		return chains



	else:
		for i in range(len(dominoes)):
			chains=[]
			left = list(dominoes)
			start = left.pop(i)
			#print(dominoes,left,start,chains)
			#import code; code.interact(local=dict(globals(), **locals()))
			for j in range(len(left)):
				print(start,left,j,chains)
				if start[1] == left[j][0]:
					chains.append(start)
					second = left.pop(j)
					print(3,'chains',chains,j,'start')
					print([second]+left)
					rest = chain([second]+left,1)
					if len(rest)==len(left)+1:
						chains= chains + rest
					print(3,'chains',chains,'stop')
					left.insert(j,second)
				if len(chains) >= len(dominoes) :
					print('break')
					break
				else:
					chains = []
				if start[1] ==  left[j][1]:
					chains.append(start)
					second = left.pop(j)
					print(4,'chains',chains,j)
					rest = chain([(second[1],second[0])]+left,1)
					if len(rest)==len(left)+1:
						chains = chains + rest
					print(4,'chains',chains)
					left.insert(j,second)


				if len(chains) >= len(dominoes) :
					print('break')
					break
				else:
					chains = []
			else:
				left.insert(i,start)

			if chains:
				if chains[0][0] == chains[-1][1]:
					print('len')
					break

		if chains ==[]:
			chains = dominoes	
		if chains:
			if chains[0][0] == chains[-1][1] and len(chains)==len(dominoes):
				return chains
		else:
			if chains:
				return None
			else:
				return chains


output_chain = chain([(1, 2), (2, 3), (3, 1), (1, 1), (2, 2), (3, 3)] )
print(output_chain)