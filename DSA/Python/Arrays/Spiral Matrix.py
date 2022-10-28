#Problem Link: https://leetcode.com/problems/spiral-matrix/

def spiralOrder(l):
    CS = 0
    CE = len(l[0])-1
    RS = 0
    RE = len(l)-1
    ans =[]
    total_elements = len(l[0])*len(l)
    while total_elements>0:

        for x in range(CS,CE+1):
            ans.append(l[RS][x])

        RS=RS+1

        total_elements= total_elements-(CE-CS+1)
        if total_elements == 0:
            break

        for k in range(RS,RE+1):
            ans.append(l[k][CE])

        CE=CE-1

        total_elements=total_elements-(RE-RS+1)
        if total_elements == 0:
            break

        for m in range(CE,(CS-1),-1):
            ans.append(l[RE][m])

        RE=RE-1

        total_elements= total_elements-(CE-CS+1)
        if total_elements == 0:
            break

        for n in range(RE,(RS-1),-1):
            ans.append(l[n][CS])

        CS=CS+1
        total_elements= total_elements-(RE-RS+1)

    return ans