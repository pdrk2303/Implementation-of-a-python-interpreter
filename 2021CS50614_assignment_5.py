import sys

def member(S,e):# Checks whether e is a member of list S
    n=len(S)
    pivot=False  
    for i in range(0,n):
        if(S[i]==e):
            pivot=True
            return pivot 
        else:
            pivot=False 
    if(pivot==False):
        return pivot

def tuple_index(P):# Returns the indices of tuples in the list P 
    r=[]
    for i in range(0,len(P)):
        if(type(P[i])==tuple):
            r.append(i)
    return r

def value_index(P):# Returns the indices of values(which are in the form of strings) in the list P
    r=[]
    for i in range(0,len(P)):
        if(type(P[i])==str): 
            r.append(i)
    return r 

f=open("D:\\priya iit d\\col assignment\\trial\\7.txt","r")  
lines=f.readlines()
l=[] 
flag=False
pivot=False
for i in lines:
    r=''
    k=i.split()
    # INPUT is valid only if 3<=len(k)<=5
    if(len(k)==5):# i is of the form "VARIABLE = TERM BINARY_OPERATOR TERM" 
        t=k[3]
        if(k[0].isalpha()==False):# k[0] can only be a variable and not a digit
            if(k[1]!='='):
                sys.exit("Invalid Input: There is no variable to which the value is assigned")
            else:
                sys.exit("Invalid Input: A digit cannot be assigned to some other value")  
        elif(k[0]=='True' or k[0]=='False'):# k[0] can only be a variable and not a boolean
            if(k[1]!='='):
                sys.exit("Invalid Input: There is no variable to which the value is assigned")
            else:
                sys.exit("Invalid Input: A boolean cannot be assigned to some other value")
        elif(k[1]!='='):# k[1] should only be an '=' operator(assignment operator) 
            sys.exit("Invalid Input: There is no '=' assignment operator")   
        elif(t!='+' and t!='-' and t!='*' and t!='/' and t!='>' and t!='<' and t!='<=' and t!='>=' and t!='==' and t!='!=' and t!='and' and t!='or'):
        # Between two terms there can only be a binary operator
            sys.exit("Invalid Input: There can only be a binary operator between two terms")
        elif(k[2].isalpha()==False and k[2].isdigit()==False):# The terms can be variables or digits or booleans only
            sys.exit("Invalid Input: The terms can only be variables or digits or booleans")
        elif(k[4].isalpha()==False and k[4].isdigit()==False):# The terms can be variables or digits or booleans only
            sys.exit("Invalid Input: The terms can only be variables or digits or booleans")
    elif(len(k)==4):# i is of the form "VARIABLE = UNARY_OPERATOR TERM"
        t=k[2] 
        if(k[0].isalpha()==False):# k[0] can only be a variable and not a digit 
            if(k[1]!='='):
                sys.exit("Invalid Input: There is no variable to which the value is assigned")
            else:
                sys.exit("Invalid Input: A digit cannot be assigned to some other value")   
        elif(k[0]=='True' or k[0]=='False'):# k[0] can only be a variable and not a boolean
            if(k[1]!='='):
                sys.exit("Invalid Input: There is no variable to which the value is assigned")
            else:
                sys.exit("Invalid Input: A boolean cannot be assigned to some other value")
        elif(k[1]!='='):# k[1] should only be an '=' operator(assignment operator) 
            sys.exit("Invalid Input: There is no '=' assignment operator")
        elif(t!='-' and t!='not'):# k[2] can only be an unary operator 
            sys.exit("Invalid Input: There can only be a unary operator befor a term")
        elif(k[3].isalpha()==False and k[3].isdigit()==False):# The term can be variable or digit or boolean only 
            sys.exit("Invalid Input: The term can only be a variable or digit or boolean")
    elif(len(k)==3):# i is of the form "VARIABLE = TERM"
        if(k[0].isalpha()==False):# k[0] can only be a variable and not a digit
            if(k[1]!='='):
                sys.exit("Invalid Input: There is no variable to which the value is assigned")
            else:
                sys.exit("Invalid Input: A digit cannot be assigned to some other value")
        elif(k[0]=='True' or k[0]=='False'):# k[0] can only be a variable and not a boolean
            if(k[1]!='='):
                sys.exit("Invalid Input: There is no variable to which the value is assigned")
            else:
                sys.exit("Invalid Input: A boolean cannot be assigned to some other value")
        elif(k[1]!='='):# k[1] should only be an '=' operator(assignment operator) 
            sys.exit("Invalid Input: There is no '=' assignment operator")
        elif(k[2].isalpha()==False and k[2].isdigit()==False):# The term can be variable or digit or boolean only 
            sys.exit("Invalid Input: The term can only be a variable or digit or boolean")
    else:# INPUT is invalid if len(k)<3 and len(k)>5
        sys.exit("Invalid Input: Input is not of the form mentioned")  
            
    for j in k:
        if(j.isdigit()):# if the j contains a whole number
            r+=j
            if(member(l,j)==False): 
                l.append(j) 
        elif(j=='+' or j=='-' or j=='*' or j=='<' or j=='>' or j=='<=' or j=='>=' or j=='==' or j=='!='):
            # if j contains a binary operator except division operator(/) 
            r+=j
        elif(j=='/'):
            # if j contains division operator(/), it has to perform floor division(//)
            r+='//'
        elif(j.isalpha()):# if j contains alphabets
            if(j=='True' or j=='False'):# if j contains boolean values
                if(member(l,j)==False):
                    l.append(j)
                r+=' '+j
            elif(j=='not' or j=='or' or j=='and'):# if j contains unary or binary operators
                r+=' '+j
            else:# if j ia a variable
                h=tuple_index(l) 
                if(j!=k[0]):
                    for m in h:
                        if(j==l[m][0]):# if the variable is defined and has a values assigned to it
                            pivot=True
                            r+=' '+l[l[m][1]] 
                            break
                        else:# the variable is not defined and has no value assigned to it
                            pivot=False
                    if(pivot==False):
                        raise ValueError("Variable",j,"is not defined")  
    z=eval(r)
    a=str(z)
    if(member(l,a)==False):# if 'a' is not a member of list l
    # then a and (VARIABLE,l.index(a)) are appended to list l
        l.append(a)
        h=tuple_index(l)
        for m in h:
            if(l[m][0]!=k[0]):
                flag=False
            else:
                flag=True
                break
        if(flag==False):# if the variable is newly defined and a value is assigned to it
            l.append((k[0],l.index(a)))
        else:# if the variable is already defined and a new value is assigned to it 
        # then the index of the value in l to which the variable is assigned changes  
            index_a=l.index(a)
            l.pop(m)
            l.insert(m,(k[0],index_a))
            
    elif(member(l,a)==True):# if 'a' is a member of list l
    # then (VARIABLE,l.index(a)) is appended to list l 
        h=tuple_index(l)
        for m in h:
            if(l[m][0]!=k[0]):
                flag=False 
            else:
                flag=True
                break
        if(flag==False):# if the variable is newly defined and a value is assigned to it
            l.append((k[0],l.index(a)))
        else:# if the variable is already defined and a new value is assigned to it 
        # then the index of the value in l to which the variable is assigned changes  
            index_a=l.index(a)
            l.pop(m)
            l.insert(m,(k[0],index_a))  
# l is the data list 

h=tuple_index(l)
for m in h:
    print(l[m][0],"=",l[l[m][1]])                
    
k=value_index(l)    
r=[] 
for i in k:
    for j in h:
        if(i!=l[j][1]):
            flag=False 
        else:
            flag=True
            break
    if(flag==False):# the values used in the program but not referred to any more by any variable at the end of the program
        k=eval(l[i])
        r.append(k) 
# r is the garbage list 
print("Garbage List:",r) 








































