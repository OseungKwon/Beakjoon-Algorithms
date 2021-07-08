a,b,v=map(int,input().split())
if a==b==v:
    print(1)
else:
    result=(v-a)/(a-b)
    if result>int(result):
        result+=1
    print(int(result+1))
