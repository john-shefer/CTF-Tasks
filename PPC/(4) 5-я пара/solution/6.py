prost=[]
c = 2 
count=3 
key =0
prost.append(3)
while c<10001:
    key = 0;
    count+=2;
    for i in range(c):
        if count%prost[i]!=0:
          key+=1
    if key==c:
        prost.append(count)
        c+=1
        print(count)