class Filter():

    def __init__(self):
        # list of slurs and dictionary of characters and their corresponding alternate characters
        self.slurs = ['Enter strings that you don\'t want in the server here']
        self.possibles = []
        self.relations = {'a':['@'], 'b':['8', '&'], 'e':['3'], 'i':['1', '!'], 'l':['1','!'], 'o':['0'], 's':['2', '5', '$'], 't':['7'], 'z':'2'} 
        
        # put all combinations into list of slurs
        for slur in self.slurs:
            self.possibles.append(slur)
            for c in slur:
                if c in self.relations:
                    n = 1
                    for repl in self.relations[c]:
                        while n <= slur.count(c):
                            if slur.replace(c, repl, n) not in self.possibles:
                                self.possibles.append(slur.replace(c, repl, n))
                            n += 1
        for slur in self.possibles:
            for c in slur:
                if c in self.relations:
                    for repl in self.relations[c]:
                        s = slur.replace(c, repl)
                        if s not in self.possibles:
                            self.possibles.append(s)
    
        self.possibles.sort()
        self.slurs = self.possibles
