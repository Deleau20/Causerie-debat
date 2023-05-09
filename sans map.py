# 

def parityRange(M,N):
    tab = []
    for i in range(M,N):
      if M < N and i%2 ==0:
        tab.append(i)
      else:
        return -1
    print(tab)



parityRange(1,10)