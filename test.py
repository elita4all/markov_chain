import csv
import random

class DataReader:
  def __init__ (self):
    self.words = {}
    self.sentence = ''
    self.buildHash()
    self.randomSentence()
    print ()
    print (self.sentence)


  def getWords (self):
    words = []
    with open('clean_dialog.csv', newline='') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        for word in row['dialog'].split():
          words.append(word)    
        break  
    return words      

  def addToHash (self, key, word):
    if key in self.words:
      self.words[key].append(word)
    else:
      self.words[key] = [word]

  def buildHash (self):
    words = self.getWords()
    idx = 1
    for word in words[idx:]:
      key = words[idx - 1]
      word = word.replace('.', '')
      self.addToHash(key, word)
      idx += 1  
    print (self.words)

  def randomSentence (self):
    firstWord = random.choice(list(self.words.keys()))  
    self.sentence = firstWord.capitalize()

    while firstWord in self.words:
      secondWord = random.choice(self.words[firstWord])
      firstWord = secondWord
      self.sentence += ' ' + secondWord
    

        
o = DataReader()

