try:
    file=open("file_1.xt", "r")
    for i in file:
        p=i.split()
        s=int(p[0])
        t=int(p[1])
        x=s*t
        print (x)
        
except IOError :
    
   print("Error: file not found.")
   
except ValueError as exception :
    
   print("Error:", str(exception))