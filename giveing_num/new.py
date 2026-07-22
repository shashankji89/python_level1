def new_pr(n):
    ran=n//2
    for no in range(ran):
       sqr=no*no
       if sqr>n:
           print("its not sqr")
       elif sqr==n:
           print("its perfect sqr: " , n)     
       
       
    
new_pr(21)   