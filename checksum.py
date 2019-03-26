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
    data = []
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
        sum_s += ((pow(2,nob)-1)^d)
    ## Appending the complementd sum in the data set 
    data.append(sum_s)
    print("Data set to be transmitted : -",data)
    print("Sender Checksum :-",sum_s)
    print("\n")
    receiver(data)
    
def receiver(data):
    print("Welcome to Receiver's End")
    sum_r = 0
    for i in range(len(data)):
        ## Calculating the no. of digits required to  represent a data in binary
        nob = count(data[i])
        #Calculating the complemented sum for the data set
        sum_r += ((1<<nob)-1)^data[i]
    print("1's Complemented Receiver Sum = ",sum_r)
    ## No. of binary digits for the 1;s complemented sum
    nob = count(sum_r)
    ## Complementing the Sum
    sum_r = ((1<<nob)-1)^sum_r
    print("Receiver Checksum :- ",sum_r)
    data_checker(sum_r)

def data_checker(sum_r):
    ## if the complemented sum is 0 , the data is correct
    if sum_r == 0:
        print("Transmission Successfull!!!!")
    else:
        print("Error in Transmission")    
sender()

