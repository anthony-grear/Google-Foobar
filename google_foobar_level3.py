target = 0
sequence = []
start = 0
temp = 0
while temp<5:  
  sequence.append(temp)
  if temp==4:
    target+=1
    temp =target
    start =0 
    continue
    if target == 5:
      break    
  if start==temp:
    start+=1
    temp = 0    
    continue
  temp+=1
  
print(sequence)