def count(ascii_diagram):
	
	count=0
	if len(ascii_diagram)<1:
		return count
	else:
		horizontal=len(ascii_diagram[0])

	for x in range(len(ascii_diagram)):
		for i in range(horizontal):
			if ascii_diagram[x][i]=='+':
				top_left = i
				for j in range(i+1,horizontal):
					if ascii_diagram[x][j]=='-':
						continue
					elif ascii_diagram[x][j]=='+':
						top_right=j
						for i in range(x+1,len(ascii_diagram)):
							if ascii_diagram[i][top_left]=='|':
								continue
							elif ascii_diagram[i][top_left]=='+':
								bottom_left=i
								for j in range(top_left+1,horizontal):
									if ascii_diagram[i][j]=='-':
										continue
									elif ascii_diagram[i][j]=='+':
										if j==top_right:
											bottom_right=j
											for y in range (x+1,bottom_left):
												if ascii_diagram[y][top_right] not in ['|','+']:
													
													break
											else:
												count+= 1
												
												
											
							else:
								break


	return count

