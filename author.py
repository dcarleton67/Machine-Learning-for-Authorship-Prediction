class Author:
  def __init__(self, authorName, filterLength):
    """Initializes Author class"""
    self.authorName = authorName
    self.wordCount = 0
    self.wordFrequency = {}
    self.filterLength = filterLength
    
  def filter(self, story):
    """Parses a story and filters out words greater than filterLength"""
    punctuation = ['.', ',', '!', '?', ':', ';', '\'', '"']
    storyFile = open(story, "r")
    unfiltered = storyFile.read().split()
    filtered = []
    for i in range(len(unfiltered)):
      unfiltered[i] = unfiltered[i].lower()
      if unfiltered[i][-1] in punctuation:
        unfiltered[i] = unfiltered[i][:-1]
        
      if unfiltered[i][0] in punctuation:
        unfiltered[i] = unfiltered[i][0:]
        
      if len(unfiltered[i]) < self.filterLength:
        filtered.append(unfiltered[i])
    return filtered
    
    
  def countWords(self, story):
    """Parses a story and counts each word in dictionary"""
    for word in story:
      self.wordCount += 1
      if word not in self.wordFrequency:
        self.wordFrequency[word] = 1
      else:
        self.wordFrequency[word] += 1
    
 def evaluate(self, story):
    """Parses a story and gives a score based on likelihood of this being the author"""
    score = 0
    for word in story:
        if word in self.wordFrequency:
            score += self.wordFrequency[word]/self.wordCount
    return score
