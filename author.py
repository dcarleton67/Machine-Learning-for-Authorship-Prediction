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
    """Parses a story and counts each word in said dictionary"""
    return NotImplemented
    
  def evaluate(self, story):
    """Parses a story and gives a score based on likelihood of this being the author"""
    return NotImplemented
