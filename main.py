import string
import random

if __name__ == "__main__":
    
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    
    s = []
    s.extend(list(s1))
    s.extend(list(s2)) 
    s.extend(list(s3)) 
    s.extend(list(s4)) 
    
     
    # random.shuffle(s)
    passLen = int(input("Enter Your Password length in NUMBER:-->> \n"))
    print("Your Password is")
    # print("".join(s[0:passLen]))  # Method 1 
    
    print("".join(random.sample(s,passLen)))    # Method 2
    