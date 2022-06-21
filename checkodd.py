def countOdds(low, high):
             
        needed = []
        
        for i in range(low, high+1):            
           needed.append(i)      
       
        result = list(filter(lambda x: (x % 2 != 0), needed))
        
        print(len(result))

countOdds(3,7)