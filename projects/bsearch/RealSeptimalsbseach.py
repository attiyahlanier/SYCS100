# Alston Clark

def bsearch(list,search):




  top = len(list)

  bottom = 0

  
 

  if (top < search) and (search < bottom):
    return -1 
  
  if (len(list) == 0):
    return -1 
    
   
  while ( bottom <= top):
    # when bottom == top then you have found the index



    mid = (top + bottom) / 2

    if (search < list[mid]):
      top = mid - 1


    elif ( search > list[mid]):
      bottom = mid + 1


    

    else:
      return mid

      
# Hannah's new update 
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

      
      
#Hannah's bsearch

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


    
#Lena's bsearch 
def bsearch(list, element):              #bsearch function definition 
    if len(list) != 0:                     #condition checking for emptiness 
        first = 0                   
        last = len(list)-1                #declaration of last index variable 
        found = False                        #bool found variable defined 
        while not found:                  #while loops until element is found 
            midpoint = (first + last)/2         #updates midpoint checking
            if (first==last) and (element != list[first]):      #when one element is left to be searched and that element is not the desired value   
                print 'Element is not in list.'     
                return -1                                   #ends function 
            elif element < list[midpoint]:              #if element is less than element at current list position 
                last = midpoint - 1                     #updates last index value 
            elif element > list[midpoint]:              #if element is greater than element at current list positon 
                first = midpoint + 1                    #updates first index value 
            else:                                       #else element equals element at current list positon 
                found = True                        #ends while loop 
                return midpoint     #returns index of searched element 
    else:                           #list is empty 
        print 'Element cannot be found. List is empty.'
        return -1


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
#print bsearch(myList,9)                         #function call to bsearch passing the variable myList


#Cesa Salaam bsearch
def bsearch (List, element): # defining the function
    bottom = 0
    top = len(List)-1
    if len(List)== 0: #checks if the List is empty
        return -1
    elif len(List)!= 0:
        if element <= List[top] and element >= List[0]: # checks to see if the element is within the range of the List.
                while top >= bottom: # While loop to repeat the Binary search
                    middle = (bottom+top)//2 #Variable to split list in half
                    if element == List[middle]: #if statement to check if the element has been found
                        return middle
                    elif element > List[middle]: #Else if statement to check if the element is above the middle
                        bottom = middle + 1
                    elif element < List[middle]: #Else if statement to check if the element is below the middle
                        top = middle - 1
        else:
            return str(-1) + " Your element was not found in the list, sorry try again...."

#Sarah Jones
def bsearch( lista, element):
    start = 0
    end = len(lista) - 1
    while (end >= start):
          mid = (start + end) / 2
          if (lista[mid] < element):
            start = mid + 1
          elif lista[mid] > element:
            end = mid - 1
          else:
            return mid
            
        
    return -1
    
#Attiyah Lanier

 
def bsearch (searchList, element):
    first = 0 
    last = len(searchList) - 1    
    midPoint = (first + last) / 2       
    found = False    
    
    

    while found == False and first <= last:    
        
        if element > searchList[midPoint]:      
            first = midPoint + 1                
            midPoint = (first + last) /2        
            found = False                       

        elif element < searchList[midPoint]:    
            last = midPoint - 1                 
            midPoint = (first + last) / 2       
            found = False                       

        elif element == searchList[midPoint]:   
            found = True                        

    if found == False:                          
        return -1

    
    return midPoint 











