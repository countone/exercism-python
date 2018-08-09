WHITE=1
BLACK=0
NONE=2
markers = { 'W': WHITE , 'B' : BLACK , ' ': NONE}
class Board:
    """Count territories of each player in a Go game
    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.board = board

    
    def get_owner(self, x, y):

        owner = None

        #traversing left
        i=1
        if (x-i) > 0:
            marker= self.board[y][x-i]
            if  marker != ' ':
                owner = marker
                
        #traversing right
        i=1
        if x+i < len(self.board[0]):
            marker = self.board[y][x+i]                
            if owner is None:
                if marker != ' ':
                    owner = marker
                    
            else:
                if marker == ' ':
                    pass
                else:
                    if marker != owner:
                        owner = ' '
                    

        #traversing up
        if y-i > 0:
            marker = self.board[y-i][x]                
            if owner is None:
                if marker != ' ':
                    owner = marker
                    
            else:
                if marker == ' ':
                    pass
                else:
                    if marker != owner:
                        owner = ' '
                    

        #traversing down
        if y+i < len(self.board): 
            marker = self.board[y+i][x]                
            if owner is None:
                if marker != ' ':
                    owner = marker
                    
            else:
                if marker == ' ':
                    pass
                else:
                    if marker != owner:
                        owner = ' '
                    

        #traversing upleft
        if y-i>0 and x-i>0:
            try:
                if self.board[y][x-i] != ' ' and self.board[y-i][x] != ' ':
                    raise IndexError
                marker= self.board[y-i][x-i]
                if owner is None:
                    if marker != ' ':
                        owner = marker
                        
                else:
                    if marker == ' ':
                        pass
                    else:
                        if marker != owner:
                            owner = ' '
                        
            except IndexError:
                pass
                    
        #traversing downright
        if x+i < len(self.board[0]) and y+i< len(self.board):
            try:
                if self.board[y][x+i] != ' ' and self.board[y+i][x] != ' ':
                    raise IndexError
                marker = self.board[y+i][x+i]                
                if owner is None:
                    if marker != ' ':
                        owner = marker
                        
                else:
                    if marker == ' ':
                        pass
                    else:
                        if marker != owner:
                            owner = ' '
                        
            except IndexError:
                pass

        #traversing upright
        if y-i >0 and x+i < len(self.board[0]):
            try:
                if self.board[y-i][x] != ' ' and self.board[y][x+i] != ' ':
                    raise IndexError
                marker = self.board[y-i][x+i] 
                if owner is None:
                    if marker != ' ':
                        owner = marker
                else:
                    if marker == ' ':
                        pass
                    else:
                        if marker != owner:
                            owner = ' '
                        
            except IndexError:
                pass

        #traversing downleft
        if x-i>0 and y+i < len(self.board):
            try:
                if self.board[y][x-i] != ' ' and self.board[y+i][x] != ' ':
                    raise IndexError
                marker = self.board[y+i][x-i]                
                if owner is None:
                    if marker != ' ':
                        owner = marker
                        
                else:
                    if marker == ' ':
                        pass
                    else:
                        if marker != owner:
                            owner = ' '
                        
            except IndexError:
                pass
        return owner

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board
        Args:
            x (int): Column on the board
            y (int): Row on the board
        """

        if x<0 or x>len(self.board[0])-1 or y<0 or y> len(self.board)-1:
            raise ValueError('ValueError')
        owner= None
        territory=[]
        if self.board[y][x]==' ':

            territory.append((x,y))
            
            #traversing left
            i=1
            while  -1< (x-i) :
                try:
                    marker= self.board[y][x-i]
                    if  marker != ' ':
                        owner = marker
                        break
                    
                    territory.append((x-i,y))

                except IndexError:
                    break
                i+= 1
                    
            #traversing right
            i=1
            while (x+i) < len(self.board[0]):
                try:
                    marker = self.board[y][x+i]                
                    if owner is None:
                        if marker != ' ':
                            owner = marker
                            break
                        
                        territory.append((x+i,y))
                    
                    else:
                        if marker == ' ':
                            territory.append((x+i,y))
                            pass
                        else:
                            if marker != owner:
                                owner = ' '
                            break
                except IndexError:
                    break
                i+= 1

            #traversing up
            i=1                    
            while -1< (y-i):
                try:
                    marker = self.board[y-i][x]                
                    if owner is None:
                        if marker != ' ':
                            owner = marker
                            break
                        territory.append((x,y-i))
                    else:
                        if marker == ' ':
                            territory.append((x,y-i))
                            pass
                        else:
                            if marker != owner:
                                owner = ' '
                            break
                except IndexError:
                    break
                i+= 1 

            #traversing down
            i=1                   
            while (y+i) < len(self.board):
                try:
                    marker = self.board[y+i][x]                
                    if owner is None:
                        if marker != ' ':
                            owner = marker
                            break
                        territory.append((x,y+i))
                    else:
                        if marker == ' ':
                            territory.append((x,y+i))
                            pass
                        else:
                            if marker != owner:
                                owner = ' '
                            break
                except IndexError:
                    break
                i+= 1

            #traversing upleft
            i=1
            while -1< (x-i) and -1< (y-i):
                try:
                    if self.board[y][x-i] != ' ' and self.board[y-i][x] != ' ':
                        break
                    marker= self.board[y-i][x-i]
                    if owner is None:
                        if marker != ' ':
                            owner = marker
                            break
                        territory.append((x-i,y-i))
                    else:
                        if marker == ' ':
                            owner = self.get_owner(x-i,y-i)
                            territory.append((x-i,y-i))
                            pass
                        else:
                            if marker != owner:
                                owner = ' '
                            break
                except IndexError:
                    break
                i+= 1
                    
            #traversing downright
            i=1
            while (x+i) < len(self.board[0]) and (y+i) < len(self.board):
                try:
                    if self.board[y][x+i] != ' ' and self.board[y+i][x] != ' ':
                        break
                    marker = self.board[y+i][x+i]                
                    if owner is None:
                        if marker != ' ':
                            owner = marker
                            break
                        territory.append((x+i,y+i))
                    else:
                        if marker == ' ':
                            owner = self.get_owner(x+i,y+i)
                            territory.append((x+i,y+i))
                            pass
                        else:
                            if marker != owner:
                                owner = ' '
                            break
                except IndexError:
                    break
                i+= 1

            #traversing upright
            i=1                    
            while (x+i) < len(self.board[0]) and y-i>-1:
                try:
                    if self.board[y-i][x] != ' ' and self.board[y][x+i] != ' ':
                        break
                    marker = self.board[y-i][x+i]                
                    if owner is None:
                        if marker != ' ':
                            owner = marker
                            break
                        territory.append((x+i,y-i))
                    else:
                        if marker == ' ':
                            owner = self.get_owner(x+i,y-i)
                            territory.append((x+i,y-i))
                            pass                                
                        else:
                            if marker != owner:
                                owner = ' '
                            break
                except IndexError:
                    break
                i+= 1 

            #traversing downleft
            i=1                   
            while -1< (x-i) and -1< (y-i):
                try:
                    if self.board[y][x-i] != ' ' and self.board[y+i][x] != ' ':
                        break
                    marker = self.board[y+i][x-i]                
                    if owner is None:
                        if marker != ' ':
                            owner = marker
                            break
                        territory.append((x-i,y+i))
                    else:
                        if marker == ' ':
                            owner = self.get_owner(x-i,y+i)
                            territory.append((x-i,y+i))
                            pass
                        else:
                            if marker != owner:
                                owner = ' '
                            break
                except IndexError:
                    break
                i+= 1                
            if owner is None:
                owner = ' '
        else:
            owner = ' '

        """
        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        
        return markers[owner],set(territory)

    def territories(self):
        """Find the owners and the territories of the whole board
        Args:
            none
        """
        territories = {BLACK: set(), WHITE: set(), NONE: set()}

        for y in range(len(self.board)):
            for x in range(len(self.board[y])) :
                if self.board[y][x] == ' ':
                    result = self.territory(x,y)
                    for values in result[1]:
                        territories[result[0]].add(values)
                        
        """
        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        return territories
