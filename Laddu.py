# cook your dish here
for _ in range(int(input())):
    n , orgin = map(str,input().split())
    n = int(n)
    laddu = 0
    for i in range(n):
        act = input()
        if act[0] == "C":
            a,pos = map(str,act.split(" "))
            laddu = laddu + 300 - int(pos)
        
        elif act[0] == "T":
            laddu = laddu + 300
        
        elif act[0] == "B":
            a,bugs = map(str,act.split(" "))

            laddu = laddu + int(bugs)
        
        elif act[0] == "C":
            laddu = laddu + 50
        
        else:
            print("lusu")
            
    if origin == "INDIAN":
        print(laddu//200)
    else:
        print(laddu//400)
