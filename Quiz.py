def is_prime(num):
 if num<2:
        print("not a prime num")
 else:
     for i in range(2,num):
         if num%i==0:
              print("not prime num")
              break
     else:
             print("num is prime num")
        
