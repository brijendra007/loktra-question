h=int(raw_input())
no_of_char=int(raw_input())
letters="acdegilmnoprstuw"
length=len(letters)
a=[]
pos=0
for i in range(0,no_of_char):
    rem=h%37
    h=h/37
    pos=rem%(length)
    a.append(letters[pos])
a.reverse();
print ''.join(a)
    
    
    
