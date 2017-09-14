import numpy as np
Rclockwise=["right","right","down","down","left","left","up","up"]
R987452369=["right","right","down","left","down","left","up","up"]
Rrrddluulddrruull=["right","right","down","down","left","up","up","left",\
                   "down","down","right","right","up","up","left","left"]
R9852369=["right","down","down","left","up","up"]
Rddrurull=["down","down","right","up","right","up","left","left"]
Rrrdluldrurdlurdllu=["right","right","down","left","up","left","down","right","up",\
                     "right","down","left","up","right","down","left","left","up"]
Rsmallclockwise=["right","down","left","up"]
R9874569=["right","right","down","left","left","up"]

def find_n_posi(block,n):
    return [int(np.where(block == n)[0]), int(np.where(block == n)[1])]  # [row,col]
def solve(state):
    procedure = []
    p0=find_n_posi(state,0)
    if p0!=[2,2]:
        for r in range(2-p0[0]):
            procedure.append("up")
        for c in range(2-p0[1]):
            procedure.append("left")
    else:
        p1=find_n_posi(state,1)
        if p1!=[0,0]:
            if p1==[1,1]:
                procedure.extend(["right","right","down","left","down","right","up","left","left","up"])
            else:
                procedure.extend(Rclockwise)
        else:
            p2=find_n_posi(state,2)
            p3=find_n_posi(state,3)
            if p3==[0,2] and p2==[0,1]:
                p4 = find_n_posi(state, 4)
                p7 = find_n_posi(state, 7)
                if p4 == [1, 0] and p7 == [2, 0]:
                    p5 = find_n_posi(state, 5)
                    if p5 != [1, 1]:
                        procedure.extend(Rsmallclockwise)
                    else:
                        procedure.append("finish")
                else:
                    if p7 == [1, 0]:
                        if p4 == [2, 0]:
                            procedure.extend(Rrrdluldrurdlurdllu)
                        else:
                            if p4 != [1, 1]:
                                procedure.extend(Rsmallclockwise)
                            else:
                                procedure.extend(R9874569)
                    else:
                        procedure.extend(R9874569)
            else:
                if p2!=[1,0]:
                    procedure.extend(R987452369)
                else:
                    p3=find_n_posi(state,3)
                    if p3==[1,1]:
                        procedure.extend(Rddrurull)
                        procedure.extend(Rddrurull)
                    elif p3==[2,0]:
                        procedure.extend(Rrrddluulddrruull)
                    else:
                        procedure.extend(R9852369)
    return procedure