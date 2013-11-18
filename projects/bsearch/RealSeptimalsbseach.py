# Alston Clark

def bsearch(list,search):




  top = len(list)

  bottom = 0

  
 

  if (top >= search >= bottom):
    return -1 

   
  while ( bottom != top):
    # when bottom == top then you have found the index

    mid = (top + bottom) / 2

    if (search < list[mid]):
      top = mid - 1


    elif ( search > list[mid]):
      bottom = mid + 1


    else:
      return mid


# Hannah's Bsearch

def search(item,numbers):
        searchend=len(numbers)                                          # end of search
        search=0                                                                        # start of search
        found=False
        while(found==False):
                scope=(search+searchend)/2                              # scope to hold span of search
                if(item<numbers[scope]):
                        searchend=scope-1
                elif(item>numbers[scope]):
                        search=scope+1
                else:                                                                   # if its is not greater or less than it is equal to
                        found=True
                        return scope                                            # return correct index




#Attiyah's bsearch

#bsearch: binary search function of sorted list 
def bsearch (searchList, element):
    first = 0 #variable used to manuvear through list
    last = len(searchList) - 1    #variable used to manuvar through list
    midPoint = (first + last) / 2       #variable used to split list in half
    found = False    #variable to mark whether the element has been found in the list 
    
    #print "My first element is ", searchList[first]
    #print "My last element is ", searchList[last]
    #print "My midpoint is ", searchList[midPoint]

    while found == False and first <= last:    #while loop used to look through entire list once
        
        if element > searchList[midPoint]:      #conditional used to determine whether to search the upper or lower half of the list
            first = midPoint + 1                #changes the first position to the midpoint + 1
            midPoint = (first + last) /2        #updates the midpoint 
            found = False                       #updates the value of found

        elif element < searchList[midPoint]:    #used to determine whether to search the lower or upper half of the list
            last = midPoint - 1                 #changed the last poistion to midpoint - 1
            midPoint = (first + last) / 2       #updates the midpoint
            found = False                       #updates the value of found

        elif element == searchList[midPoint]:   #if the element is found
            found = True                        #found is set to True, exiting the loop

    if found == False:                          #if statement to return false if element is not found
        return -1

    
    return midPoint                             #if statement to return the index of the element if found

#myList = [22,33,44,55,66,77,88,99]              #declaration and assignment of myList 
p#rint bsearch(myList,9)                         #function call to bsearch passing the variable myList










