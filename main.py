#This is the test file
#need to bring in data
from Author import Author
from Author import predict
from Author import eliminate
def bringindata():
    #f = gzip.open('C:/Users/lmip/Documents/VE593/Project3/mnist.pkl.gz', 'rb')
    first = Author("apress", 5)
    second = Author("acrosby", 5)
    third = Author("BK", 5)
    four = Author("BH",5)
    five = Author("AS", 5)
    filteredone = first.filter("C:/Users/lmip/Documents/VE593/Project4/APtrain.txt")
    first.countWords(filteredone)
    filteredtwo = second.filter("C:/Users/lmip/Documents/VE593/Project4/ACtrain.txt")
    second.countWords(filteredtwo)
    filteredthree = third.filter("C:/Users/lmip/Documents/VE593/Project4/BKtrain.txt")
    third.countWords(filteredthree)
    filteredfour = four.filter("C:/Users/lmip/Documents/VE593/Project4/BHtrain.txt")
    four.countWords(filteredfour)
    fivedat = five.filter("C:/Users/lmip/Documents/VE593/Project4/AStrain.txt")
    five.countWords(fivedat)

    filtered = first.filter("C:/Users/lmip/Documents/VE593/Project4/APtest.txt")
    filtered1 = first.filter("C:/Users/lmip/Documents/VE593/Project4/ACtest.txt")
    filtered2 = first.filter("C:/Users/lmip/Documents/VE593/Project4/AStest.txt")
    filtered3 = first.filter("C:/Users/lmip/Documents/VE593/Project4/BKtest.txt")
    filtered4 = first.filter("C:/Users/lmip/Documents/VE593/Project4/BHtest.txt")
    stories = [filtered, filtered1, filtered2, filtered3, filtered4]


    total = 0
    authors = [first, second, third, four, five]
    #authors = [ second, four, five]
    eliminate(authors,stories)
   


    return total
bringindata()
