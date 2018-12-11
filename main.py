#This is the test file
#need to bring in data
from Author import Author
def bringindata():
    #f = gzip.open('C:/Users/lmip/Documents/VE593/Project3/mnist.pkl.gz', 'rb')
    first = Author("apress", 5)
    second = Author("acrosby", 5)
    third = Author("next", 5)
    filteredone = first.filter("C:/Users/lmip/Documents/VE593/Project4/apresstrain.txt")
    first.countWords(filteredone)
    filteredtwo = second.filter("C:/Users/lmip/Documents/VE593/Project4/ACrosbytrain.txt")
    second.countWords(filteredtwo)

    filtered = first.filter("C:/Users/lmip/Documents/VE593/Project4/ACrosbytest.txt")
    total = 0
    for it in range(0,len(filtered),100):
        print(len(filtered))
        score2 = second.evaluate(filtered[it:it+100])
        score = first.evaluate(filtered[it:it+100])
        #print(score)
        #print(score2)
        print(score2>score)
        if (score2>score):
            total+=1
    print(total)



    return total
bringindata()
