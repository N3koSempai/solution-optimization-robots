class Robot():

    def __init__(self, items):
        self.items = (str(items)) #convert entry in a iterable list
        self.listp = [] #list of package (for total boxes)


    def classic_robot(self):
        listbox = [] #list for items inside a box (a box)

        for i in self.items: # for value in the array
            if sum(listbox, 0) + int(i) <= 10: #test if is reached the maximun items per box(10)
                listbox.append(int(i)) #add item to the box
            else:
                self.listp.append(listbox) #add box to the list with the total package
                listbox = [] # reset the box
                listbox.append(int(i)) #add the last item exceeded the maximun in the previous box
    
        self.listp.append(listbox) #add the leftover box

        print("this is the basic list: \n %s \n total of box: %s" % ((self.listp),(len(self.listp)))) #return the basic list


    def optimized_algo(self):  
        array = self.items #copy the items
        array = list(str(array)) #convert the items in a list of string
        listpo = [] #list for total boxs
        listbox = {} #list for items inside a box
        temp_dic = {} # temporal dict for save number no reached the maximun 10 in a sum
        length = len(array) #get the length of the list
        for i in range(0, length): #iterating in the length of array
            
            count = False #this variable act like a switch for taking the first number
            for index,j in enumerate(array):  #iterating in the array take the number and create a index
                j = int(j) # convert to a int for future calculations
                if sum(list(listbox.values()), 0) == 10: # if the box reached the maximun stop to count
                    break

                elif count == False: # take the first number and add to the box(remember the box is a dict so this add index too)
                    listbox[index]=j
                    count = True
                
                elif sum(list(listbox.values()), 0) + j == 10: #if actual number + total number in the box reached 10, add actual number to the box and stop to count 
                    listbox[index] = j
                    temp_dic = {}
                    break
                

                elif sum(list(temp_dic.values())) + sum(list(listbox.values()), 0) == 10: # if the sum of temporal dict with sum the box reached 10 add one per one temp to box

                    for k,v in temp_dic.items(): # for item inside temp add to the box one per one
                        listbox[k]=v 

                    temp_dic = {}  #delete dic because this box is full
                    break
                
                elif sum(list(listbox.values()), 0) + j < 10: #if sum of the box more actual number less to 10 add to temp dict for future calculations
                    temp_dic[index] = j
                    


            if temp_dic != [] and sum(list(listbox.values()), 0) < 10: #if any inside temp dict and sum of box less than 10 continue
                temp_copy = temp_dic.copy() #copy for not iteration in a changing dict
                for k,v in temp_copy.items(): # take index and value for the copy of temp dict
                    
                    maxim = max(listbox.values()) #take the maximun inside the box
                    if sum(list(listbox.values()),0) == 10: #if the box is maximun stop
                        break
                    
                    elif  maxim + v <= 10 and v + sum(list(listbox.values()),0) <= 10: #if maximun inside the box adding to the actual value of ...
                        #  copy of temp dict is less or equal to 10 and the actual value more sum all inside of box less or iqual to 10....
                        #  add index and value to the box and reset original temp dict 
                        
                        listbox[k] = v
                        del temp_dic[k]
        
            temp_dic = {} #reset temp dict in case dont reset before inside the ifs statemant
            listpo.append(list(listbox.values())) #add the box to the list of package
            listpo = [i for i in listpo if i != []]  #clean of entys boxs
            

            if list(listbox.keys()) != []: #if the index inside box not enty
                    
                a = [array[b] for b in range(len(array)) if not b in list(listbox.keys())] #take only the number in array whose index dont match with box index
                array = a 
                
            listbox = {} #reset the box
            length = len(array) #reset the new length in array
  
        print("this is the optimized list: \n %s \n total of box: %s" % ((listpo),(len(listpo)))) #return the optimized list


while True: #loop for input
    number = input("insert your number \n ==>") #insert the number, demo = 163841689525773
    try: 
        number = int(number) #convert the number in the input to int
        request = Robot(number) #instanciate the robot class
        request.classic_robot() #call to a clasical algorithm
        request.optimized_algo()  #call to the optimized algorithm
    except: #capturing any errors
        print("!error!, check the data") # sugestions in case of error
