def is_armstrong(number):
    length=len(str(number))
    sum=0
    for i in range(length):
    	sum+= int(str(number)[i])**length
    if sum==number:
    	return True
    else:
    	return False
