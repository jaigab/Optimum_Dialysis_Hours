width=int(input("How wide do you want your 2048 grid?"))
import random
gridfield=[]
counter={}
for i in range(width):
    counter[i]=[]
    line=[]
    for j in range(width):
        if random.randint(0,(width**2))<int(0.2*(width**2)):
            line=line+[2]
        else:
            line=line+['.']
        counter[i]=counter[i]+[0]
    gridfield=gridfield+[line]
two_count=0
for line in gridfield:
    for item in line:
        if item == 2:
            two_count=two_count+1
if two_count<3:
    for i in range(4):
        gridfield[width-1][i]=2
nfield=[]
strfield=[]
for n in gridfield:
    templ=[]
    for o in n:
        templ=templ+[str(o)]
    strfield=strfield+[templ]
for i in strfield:
    print("".join(i))

for repeat in range(200):
    nmove=input("What's your next move?")

    def two_oh_four_eight(grid,move):
        for i in range(width):
            for j in range(width):
                num=grid[i][j]
                if move =="up":
                    if grid[i][j] != '.':
                        for n in range(i):
                            if grid[n][j]!='.':
                                continue
                            else:
                                grid[n][j]=num
                                grid[i][j]='.'
                                break
                if move =="left":
                    if grid[i][j] != '.':
                        for n in range(j):
                            if grid[i][n]!='.':
                                continue
                            else:
                                grid[i][n]=num
                                grid[i][j]='.'
                                break
                if move =="right":
                    if grid[i][j] != '.':
                        for n in reversed(range(j,len(grid[i]))):
                            if grid[i][n]!='.':
                                continue
                            else:
                                grid[i][n]=num
                                grid[i][j]='.'
                                break
                if move =="down":
                    if grid[i][j] != '.':
                        for n in reversed(range(i,len(grid))):
                            if grid[n][j]!='.':
                                continue
                            else:
                                grid[n][j]=num
                                grid[i][j]='.'
                                break
        for i in range(width):
            for j in range(width):
                num=grid[i][j]
                if move =="up":
                    if i!=(width-1) and grid[i][j]==grid[i+1][j] and grid[i][j]!='.':
                        grid[i][j]=(num*2)
                        counter[i][j]=1
                        for n in range(i+1,len(grid)-1):
                            grid[n][j]=grid[n+1][j]
                if move =="left":
                    if j!=(width-1) and grid[i][j]==grid[i][j+1] and grid[i][j]!='.':
                        grid[i][j]=(num*2)
                        counter[i][j]=1
                        for n in range(j+1,len(grid[i])-1):
                            grid[i][n]=grid[i][n+1]
        for i in reversed(range(width)):
            for j in reversed(range(width)):
                num=grid[i][j]
                if move =="down":
                    if i!=0 and grid[i][j]==grid[i-1][j] and grid[i][j]!='.':
                        grid[i][j]=(num*2)
                        counter[i][j]=1
                        for n in reversed(range(0,i-1)):
                            grid[n+1][j]=grid[n][j]
                if move =="right":
                    if j!=0 and grid[i][j]==grid[i][j-1] and grid[i][j]!='.':
                        grid[i][j]=(num*2)
                        counter[i][j]=1
                        for n in reversed(range(0,j-1)):
                            grid[i][n+1]=grid[i][n]
        freespace=False
        for line in range(len(counter)):
            for item in range(len(counter[line])):
                if move == "up":
                    if freespace==False:
                        if random.randint(0,10)<3:
                            grid[width-1][item]=2
                        if 6>random.randint(0,10)>=3:
                            grid[width-1][item]=4
                        if 10>random.randint(0,10)>=6:
                            grid[width-1][item]=8
                        freespace=True
                        break
                    else:
                        grid[width-1][item]='.'
                        freespace==False
                        break
                if move == "down":
                    if freespace==False:
                        if random.randint(0,10)<3:
                            grid[0][item]=2
                        if 6>random.randint(0,10)>=3:
                            grid[0][item]=4
                        if 10>random.randint(0,10)>=6:
                            grid[0][item]=8
                        freespace=True
                        break
                    else:
                        grid[0][item]='.'
                        freespace==False
                        break
                if move == "left":
                    if freespace==False:
                        if random.randint(0,10)<3:
                            grid[line][width-1]=2
                        if 6>random.randint(0,10)>=3:
                            grid[line][width-1]=4
                        if 10>random.randint(0,10)>=6:
                            grid[line][width-1]=8
                        freespace=True
                        break
                    else:
                        grid[line][width-1]='.'
                        freespace=False
                        break
                if move == "right":
                    if freespace==False:
                        if random.randint(0,10)<3:
                            grid[line][0]=2
                        if 6>random.randint(0,10)>=3:
                            grid[line][0]=4
                        if 10>random.randint(0,10)>=6:
                            grid[line][0]=8
                        freespace=True
                        break
                    else:
                        grid[line][0]='.'
                        freespace==False
                        break
        return grid

    gridfield=two_oh_four_eight(gridfield,nmove)

    nfield=[]
    strfield=[]
    for n in gridfield:
        templ=[]
        for o in n:
            templ=templ+[str(o)+' ']
        strfield=strfield+[templ]
    for i in strfield:
        print("".join(i))
