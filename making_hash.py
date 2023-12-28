import hashlib 
word=input("Enter the Password here:- ")
print(" type 1 for sha1\n type 2 for sha224\n type 3 for sha256\n type 4 for md5\n type 5 for sha512")
a=int(input("Enter the value:- "))
if(a==1):
    print("you have selected sha1")
    result=hashlib.sha1(word.encode())
    print(result.hexdigest())
elif(a==2):
    print("you have selected sha224")
    result=hashlib.sha224(word.encode())
    print(result.hexdigest())
elif(a==3):
    print("you have selected sha256")
    result=hashlib.sha256(word.encode())
    print(result.hexdigest())
elif(a==4):
    print("you have selected md5")
    result=hashlib.md5(word.encode())
    print(result.hexdigest())    
elif(a==5):
    print("you have selected sha512")
    result=hashlib.sha512(word.encode())
    print(result.hexdigest())
else:
    print("Sorry you have typed out of reach")