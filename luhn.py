class Luhn(object):
    def __init__(self, card_num):
        self.card_num=card_num
        self.num=self.card_num.replace(' ','')

    def is_valid(self):
        
        if self.card_num!=self.card_num.strip() or self.card_num=='0':
        	return False

        elif self.num.isdigit():
        	sum=0
        	for i in range(1,len(self.num)+1):
        		
        		if i%2==0:
                    add=int(self.num[-i])*2
        			if add>9:
                        sum+=add-9
        		    else:
        			    sum+=add
        		else:
        			sum+=int(self.num[-i])

        	return sum%10==0
        else:
        	return False
        	
