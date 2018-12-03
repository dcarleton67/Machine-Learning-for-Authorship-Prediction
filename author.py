class Author:
  def __init__(self, authorName, filterLength):
    """Initializes Author class"""
    self.authorName = authorName
    self.wordCount = 0
    self.wordFrequency = {}
    
  def filter(self, story):
    """Parses a story and filters out words greater than filterLength"""
    return NotImplemented
    
    
  def countWords(self, story):
    """Parses a story and counts each word in dictionary"""
    for word in story:
      if word not in self.wordFrequency:
        self.wordFrequency[word] = 0
      else:
        self.wordFrequency[word] += 1
    
  def evaluate(self, story):
    """Parses a story and gives a score based on likelihood of this being the author"""
    return NotImplemented
