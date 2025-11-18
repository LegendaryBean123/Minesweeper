from minesweeper import Sentence
  
knowledge = []
safes = set()
mines = set()
      
s = Sentence(set(), 0)
knowledge.append(s)

print(knowledge)

s = Sentence(set(), 0)
knowledge.append(s)

print(knowledge)

s = Sentence(set([(1,1),(2,2),(3,3)]), 3)
knowledge.append(s)

print(knowledge)


s = Sentence(set([(0,0),(0,1),(0,2)]), 3)
knowledge.append(s)

print(knowledge)


s = Sentence(set([(1,0),(2,0),(3,0)]), 0)
knowledge.append(s) 

print(knowledge)

   
s = Sentence(set([(2,1),(1,2),(1,3),(3,2)]), 0)
knowledge.append(s) 

print(knowledge)

