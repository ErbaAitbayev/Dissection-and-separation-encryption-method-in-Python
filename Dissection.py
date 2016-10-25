import random

def ColumnToRow(lis):
    row = []
    for x in lis:
        row.append(x[0])
    return row
        
        
def Decrypt(rowKeys, columnKeys, Cipher, dic):
    items = sum(sum(1 for i in row if i) for row in Cipher)

    cols, rows = len(columnKeys)+1, int(items/len(columnKeys))+1
    
    array2d = [[0 for x in range(cols)] for y in range(rows)]
    array2d[0] = [0] + columnKeys
    
    j = 0
    for i in range(1,rows):
        array2d[i][0] = rowKeys[j]
        j += 1
        if j >= len(rowKeys):
            j = 0
    
    
    temp = ColumnToRow(array2d)
    
    for i in range(len(dic)):
        colIndex = array2d[0].index(dic[i][2])
        
        indices = [m for m, x in enumerate(temp) if x == dic[i][1]]
        rowIndex = indices[dic[i][3]-1]
        
        array2d[rowIndex][colIndex] = dic[i][0]
    
    for row in array2d:
        print(row)
    
    decrypted = ''
    for i in range(1,rows):
        for j in range(1,cols):
            decrypted += array2d[i][j]
            
    
    return decrypted
        
        
def Encrypt(Matrix, numberofCols, numberOfBlocks):
    Blocks = [[] for i in range(numberOfBlocks)]


    for i in range(1,ROWS):
        for j in range(1,COLS):
            colKey = Matrix[0][j]
            rowKey = Matrix[i][0]
            block = defineBlock(rowKey, colKey, numberofCols)
            Blocks[block-1].append(Matrix[i][j])
    return Blocks

    
def defineBlock(r, c, n):
    k = (r-1)*n + c
    return k


def defineSection(i, division):
    return (i//division + 1)


#message = "Metod$Rasse4eni9-Razneseni9."
#message = "Вечная беда России. Все в ней перепутано. Добро защищают дураки и мерзавцы, злу служат мученики и герои."

message = input("Enter a message to encrypt: ")
strlength = len(message)
print("Message length:", strlength)
blocksNumber = int(input("Enter number of blocks. Must be less than message length: ")) #blocksNumber = 16
ColKeysNumber = int(input("Enter number of columns (must be divisor of number of blocks; Message length must be divisible by it: ")) #ColKeysNumber = 8
RowKeysNumber = int(blocksNumber/ColKeysNumber)

print("Original message:", message + '\n')

COLS = ColKeysNumber+1 
ROWS = int(strlength//ColKeysNumber)+1

 
Matrix = [[0 for x in range(COLS)] for y in range(ROWS)]

columnKeys = random.sample(range(1,ColKeysNumber+1), ColKeysNumber)
Matrix[0] = [0] + columnKeys


repRange = list(range(1, RowKeysNumber+1))
rowKeys = list(reversed(repRange))

print("Column keys:", columnKeys)
print("Row keys:", rowKeys)
print("Number of blocks:", blocksNumber)
print()

j = 0
for i in range(1,ROWS):
    Matrix[i][0] = rowKeys[j]

    j += 1
    if j >= len(rowKeys):
        j = 0
 


dic = []
m= 0
for i in range(1,ROWS):
    for j in range(1,COLS):            
        Matrix[i][j] = message[m]
        cKey = Matrix[0][j]
        rKey = Matrix[i][0]
        section = defineSection(i-1, RowKeysNumber)
        dic.append([message[m], rKey, cKey, section])
        m += 1

print("Message distributed by defined rows and columns:")           
for row in Matrix:
    print(row)
print()   

Cipher = Encrypt(Matrix, ColKeysNumber, blocksNumber)

print("Encryption result (blocks):") 
i=1
for bl in Cipher:
    print("Block number "+ str(i) + ":", bl)
    i+=1
    
print()
print("Table structure decrypted:") 
decrypted = Decrypt(rowKeys, columnKeys, Cipher, dic)

print()
print("Final decrypted message:", decrypted)

    





