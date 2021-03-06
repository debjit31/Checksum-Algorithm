#Latest Working Code
import random
b=0
tm =0 
def comp(s):
    s = "".join('1' if x == '0' else '0' for x in s)
    return s
def comp_two(s):
    x = "1"
    s = "".join('1' if x == '0' else '0' for x in s)
    s = bin(int(s,2)+ int(x,2))
    s = s[2:]
    return s

def sender():
    data = []
    print("Sender's End")
    sum_s = 0
    n = int(input("Enter the number of data items:- "))
    b = int(input("Enter the maximum no. of bits for each data : -"))
    print("Enter data to send : = ")
    ## taking data input from user
    data = list(int (x) for x in input().strip().split())
    ## Appending the complementd sum in the data set
    sum_s = sum(data)
    if sum_s < 0:
        bs = bin(sum_s)
        bs = bs[3:]
        d = b-len(bs)
        while d!=0:
            bs = "0" + bs
            d = d - 1
        #print(bs)
        bs = comp_two(bs)
        #print(bs)
        checksum = comp(bs)
        #print(checksum)
        sum_s = int(checksum,2)
        #print(sum_s)
    else:
        bs = bin(sum_s)
        bs = bs[2:]
    if len(bs)>b:
        a_s = ""
        c_sum = ""
        d = len(bs) - b
        a_s = bs[0:d]
        bs = bs[(len(bs)-b):]
        c_sum = bin(int(bs,2) + int(a_s,2))
        c_sum = c_sum[2:]
        if len(c_sum) < b:
            c_sum = "0"+c_sum
        checksum = comp(c_sum)
        sum_s = int(checksum,2)
    elif len(bs) < b:
        d = b - len(bs)
        while d!=0:
            bs = "0" + bs
            d=d-1
        checksum = comp(bs)
        sum_s = int(checksum,2)
    else:
        checksum = comp(bs)
        sum_s = int(checksum,2)
    data.append(sum_s)
    print("Data set to be transmitted : -",data)
    print("Sender Checksum :-",sum_s)
    print("\n")
    tm = int(input("Enter transmission mode.\n1.Error-Prone/n2.Error-free\n"))
    if tm == 1:
        error_generator(data)
        receiver(data,b)
    else:
        receiver(data,b)
        
def error_generator(data):
    offset  = 0
    for i in range(random.randint(0,5)):
        #generating a random position from the list
        rp= random.randint(0,len(data)-1)
        #print(data[rp])
        #generating a random offset value to multiply with the original data
        offset = random.randint(10,30)
        data[rp] += offset   
        
def receiver(data,b):
    print("Welcome to Receiver's End")
    sum_r = 0
    print("Dataset received by receiver is  = ",data)
    sum_r = sum(data)
    if sum_r > 0:
        bsr = bin(sum_r)
        bsr = bsr[2:]
    else:
        bsr = bin(sum_r)
        bsr = bsr[3:]
        #print(bsr)
        d = b - len(bsr)
        while d!=0:
            bsr = "0" + bsr
            d = d - 1
        #print(bsr)
        bsr = comp_two(bsr)
        c_sum = bsr
        #print(bsr)
    if len(bsr) > b:
        dr = len(bsr)-b
        a = bsr[0:dr]
        bsr = bsr[2:]
        c_sum = bin(int(bsr,2) + int(a,2))
        c_sum = c_sum[2:]
    c_sum = comp(c_sum)
    sum_r = int(c_sum,2)
    print("Receiver Checksum = ",sum_r)
    data_checker(sum_r)
      
def data_checker(sum_r):
    ## if the complemented sum is 0 , the data is correct
    if sum_r == 0:
        print("Transmission Successfull!!!!")
        #data.clear()
    else:
        print("Error in Transmission")
        #data.clear()
        main()
        
def main():
    print("Welcome to Checksum Error Detection Algorithm\n")
    while True:
        ch = input("Want to tranmit some data to  your neighbour ? Press y or n: ")
        if ch == 'y' or ch == 'Y':
            sender()
        elif ch == 'n' or ch == 'N':
            print("Goodbye!!!")
            break
    quit()
main()
