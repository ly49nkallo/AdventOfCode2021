
from collections import defaultdict

file='input2.txt'
with open(file,'r') as f:
    data=[n for n in f.read().split("\n")][:-1]  
    if file=='test.txt' :
        data=[data[n]+data[n+1] for n in range(len(data)) if n%2==0]
    data=[n.split('|' ) for n in data]
    data=[[n[0].split(),n[1].split()] for n in data] 
    

segs={0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6} 
lit=defaultdict(list)
{lit[v].append(k) for k, v in segs.items()}
lit=dict(lit)
unique_segments={k:v[0] for k,v in lit.items() if len(v)==1}

ttl=0

for d in data:
    
    seg_map={}
    index={}
    fives=[]
    sixes=[]

    for i in d[0]:
        if len(i) in unique_segments:
            seg_map[unique_segments[len(i)]]=set(i)
        if len(i)==5:
            fives.append(i)   
        if len(i)==6:
            sixes.append(i)
                
    fives=[set(n) for n in fives]
    sixes=[set(n) for n in sixes]
    index['A']=(seg_map[7]-seg_map[1])
    index['ADG']=fives[0]&fives[1]&fives[2]
    index['DG']=index['ADG']-index['A']
    index['D']=index['DG']&seg_map[4]
    index['G']=index['DG']-index['D']
    index['B']=seg_map[4]-seg_map[1]-index['D']
    seg_map[3]=index['ADG']|seg_map[1]
    seg_map[9]=seg_map[3]|seg_map[4]
    index['E']=seg_map[8]-seg_map[9]
    seg_map[0]=seg_map[8]-index['D']
    for i in sixes:
        if i not in [seg_map[0],seg_map[9]] :
            seg_map[6]=i
    index['C']=seg_map[8]-seg_map[6]
    index['F']=seg_map[1]-index['C']
    seg_map[5]=seg_map[6]-index['E']
    seg_map[2]=seg_map[8]-index['B']-index['F']
                
    seg_list=[("".join(sorted(list(v))),k) for k,v in seg_map.items()]
    seg_list=dict(seg_list)
    
    disp=[]
    for i in d[1]:
        disp.append(str(seg_list["".join(sorted(i))]))
    
    result=int("".join(disp))
    #print(d[1],result)
    
    ttl=ttl+result

print(ttl)
