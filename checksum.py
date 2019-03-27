from operator import xor
import sys
import random
flag = 0
tm = 0
data = []
def count(n):
    ### Counting the number of digits for  binary representation of a deciml number
    digits = 0
    while n > 0 :
        r = n % 2
        digits+=1
        n = n // 2
    return digits
    
def sender():
    print("Sender's End")
    sum_s = 0
    n = int(input("Enter the number of data items:- "))
    print("Enter data to send : = ")
    ## taking data input from user
    for i in range(n):
        d = int(input())
        data.append(d)
        nob = count(d)
        ## calculating the complemented sum for each data item
        ## we perform a XOR operation between the the data and 2^n - 1 
        sum_s += xor((pow(2,nob)-1) , d)
    ## Appending the complementd sum in the data set 
    data.append(sum_s)
    print("Data set to be transmitted : -",data)
    print("Sender Checksum :-",sum_s)
    print("\n")
    tm = int(input("Enter transmission mode.\n1.Error-Prone/n2.Error-free\n"))
    #print("tm = ",tm)
    if tm == 1:
        error_generator()
        receiver()
        
    else:
        receiver()
        
        
                    
def receiver():
    print("Welcome to Receiver's End")
    sum_r = 0
    print("Dataset received by receiver is  = ",data)
    for i in range(len(data)):
        ## Read each data item calculating the no. of digits required to  represent a data in binary
        nob = count(data[i])
        d = data[i]
        #Calculating the complemented sum for the data set
        sum_r += xor((pow(2,nob)-1) , d)
    print("1's Complemented Receiver Sum = ",sum_r)
    ## No. of binary digits for the 1;s complemented sum
    nob = count(sum_r)
    ## Complementing the Sum
    sum_r = xor(((1<<nob)-1), sum_r)
    print("Receiver Checksum :- ",sum_r)
    data_checker(sum_r)
    
def error_generator():
    offset  = 0
    for i in range(random.randint(0,5)):
        #generating a random position from the list
        rp= random.randint(0,len(data)-1)
        #print(data[rp])
        #generating a random offset value to multiply with the original data
        offset = random.randint(10,30)
        data[rp] += offset 
    
    
def data_checker(sum_r):
    ## if the complemented sum is 0 , the data is correct
    if sum_r == 0:
        print("Transmission Successfull!!!!")
        data.clear()
    else:
        print("Error in Transmission")
        data.clear()
        flag = 1
        program_runner()

def program_runner():
    print("Welcome to Checksum Error Detection Algorithm\n")
    while True:
        ch = input("Want to tranmit some data to  your neighbour ? Press y or n: ")
        if ch == 'y' or ch == 'Y':
            sender()
        elif ch == 'n' or ch == 'N':
            print("Goodbye!!!")
            break
    quit()
program_runner()
