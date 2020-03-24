def hanoi():
    start=[]
    temp=[]
    finish=[]
    
    L=set(input("enter a list :"))
    if len(L) > 3:
        return
    start=list(L.copy())
    start.sort(reverse=True)
    print('start= ',start)
    print('temp= ',temp)
    print('finish= ',finish)
    print('................................')
    finish.append(start[2])
    start.pop()
    temp.append(start[1])
    start.pop()
    temp.append(finish[0])
    finish.pop()
    finish.append(start[0])
    start.pop()
    start.append(temp[1])
    temp.pop()
    finish.append(temp[0])
    temp.pop()
    finish.append(start[0])
    start.pop()
    
    print('start= ',start)
    print('finish= ',finish)
    
hanoi()


    
    






