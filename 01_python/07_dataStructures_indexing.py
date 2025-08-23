# #data structures 
# # 1.list 
# # name=["sami","ahmad","osman","taqi","amaar"] #list of string
# # #accessing elements
# # print(name[0]) #sami
# # print(name[1]) #ahmad
# # print(name[2]) #osman
# # print(name[3]) #taqi
# # print(name[4]) #amaar
# #isme indexing 0 se start hota hai
# #negative indexing
# # print(name[-1]) #amaar
# # print(name[-2]) #taqi   
# # print(name[-3]) #osman
# # print(name[-4]) #ahmad      
# # print(name[-5]) #sami
# # Ager indexing ma change karna ho to
# # name[0]="samiullah" #sami ko samiullah se replace kar dia
# # print(name) #['samiullah', 'ahmad', 'osman', 'taqi', 'amaar']


# # 2.tuple
# #tuple is immutable
# name_tuple=("sami","ahmad","osman","taqi","amaar") #tuple of string
# # #accessing elements
# # print(name_tuple[0]) #sami
# # print(name_tuple[1]) #ahmad
 




# #3.set
# # fruit_set={"apple","banana","cherry","date","elderberry"} #set of string
# #accessing elements
# print(fruit_set) #order is not guaranteed
# # fruit_set(1)="mango" #this will give error because set is unordered and does not support indexing
# #adding elements
# fruit_set.add("watermelon") #adding watermelon to the set
# print(fruit_set) #{'banana', 'cherry', 'date', 'elderberry', 'apple', 'watermelon'}
# #removing elements
# fruit_set.remove("banana") #removing banana from the set    
# print(fruit_set) #{'cherry', 'date', 'elderberry', 'apple', 'watermelon'}




#4.dictionary
student_dict={"name":"sami","age":20,"city":"karachi"} #dictionary of string and integer
print(student_dict) #{'name': 'sami', 'age': 20, 'city': 'karachi'}
#accessing elements 
print(student_dict["name"]) #sami
# changing elements
student_dict["age"]=21 #changing age from 20 to 21


