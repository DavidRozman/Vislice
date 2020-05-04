

print(2)
print(3)

for j in range(4, 200):

    je_prastevilo = True

    for mozni in range(2,j):
        if j % mozni == 0:
            je_prastevilo = False
            break
    
    if je_prastevilo:
        print(j)
        