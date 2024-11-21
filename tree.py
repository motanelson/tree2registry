a=input("give a file .txt to convert to .dat? ")
b=a.replace(".txt",".dat")
f1=open(a,"r")
source=f1.read()
f1.close()
source=source.split("\n")
d=""
counter2=0
stacks=[]
for n in source:
     counter=0
     TTrue=True
     if n.strip()!="":
         while TTrue:
             if n[counter]==" ":
                 counter+=1
             else:
                 TTrue=False
     lines=n.split("=")
     if len(stacks)<=counter:
         stacks=stacks+[lines[0].strip()]
     else:
         if len(stacks)>0:
             TTrue=True
             TTrue=len(stacks)>counter
             while TTrue:
                 __=stacks.pop()
                 TTrue=len(stacks)>counter
             stacks=stacks+[lines[0].strip()]
             counter2=counter
     l=0
     for h in stacks:
          if l==0: 
              d=d+h
          else:
              d=d+"\\"+h
          l+=1
     if len(lines)>1:
         d=d+"="+lines[1]+"\n"
     else:
         d=d+"\n"

f1=open(b,"w")
source=f1.write(d)
f1.close()
