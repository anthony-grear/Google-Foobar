target = 0
sequence = []
start = 0
temp = 0
counter=0
while counter < 25:
    counter +=1
    sequence.append(temp)
    if temp == start:
        target +=1
        if target==5:
            target-=1
            start+=1
            temp=target
            continue
        temp=target
        
            
        continue
    temp -=1
  
print(sequence)