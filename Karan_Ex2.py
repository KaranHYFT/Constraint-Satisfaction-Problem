#!/usr/bin/env python
# coding: utf-8

# In[1]:


from constraint import *
problem = Problem()


dog = ["Beany", "Cheetah", "Thor", "Suzie"]
breed=["Boxer", "Collie", "Shepherd", "Terrier"]
bestAt = ["Plank", "Poles", "Tire", "Tunnel"]


criteria = dog + breed + bestAt
problem.addVariables(criteria,[1,2,3,4])

# Values of all variables are different
problem.addConstraint(AllDifferentConstraint(), dog)
problem.addConstraint(AllDifferentConstraint(), breed)
problem.addConstraint(AllDifferentConstraint(), bestAt)

# The Boxer ranked 1 position after the Shepherd
# Boxer cannot be #1 as Shepherd is default 1 position ahead of him
problem.addConstraint(NotInSetConstraint([1]), ["Boxer"])
# Shepherd cannot be #4 as Boxer is default 1 position behind him
problem.addConstraint(NotInSetConstraint([4]), ["Shepherd"])
problem.addConstraint(lambda b, s: (b-s) == 1, ("Boxer","Shepherd"))

# None of them(Boxer/Shepherd) likes the tunnel, nor jumping through the tire
problem.addConstraint(NotInSetConstraint(["Boxer"]), ["Tunnel"])
problem.addConstraint(NotInSetConstraint(["Boxer"]), ["Tire"])
problem.addConstraint(NotInSetConstraint(["Shepherd"]), ["Tunnel"])
problem.addConstraint(NotInSetConstraint(["Shepherd"]), ["Tire"])


# Cheetah and the dog who loves the poles were 1st and 3rd
problem.addConstraint(NotInSetConstraint(["Cheetah"]), ["Poles"])
problem.addConstraint(InSetConstraint([1]), ["Cheetah"])
problem.addConstraint(InSetConstraint([3]), ["Poles"])


# Only the winning dog has the same initial letter in name and breed
problem.addConstraint(lambda c1,c2 : c1== c2, ["Cheetah","Collie"])
problem.addConstraint(NotInSetConstraint(["Beany"]), ["Boxer"])
problem.addConstraint(NotInSetConstraint(["Thor"]), ["Terrier"])
problem.addConstraint(NotInSetConstraint(["Suzie"]), ["Shepherd"])


# Thor doesn’t like the plank and didn’t come 2nd
problem.addConstraint(NotInSetConstraint(["Thor"]), ["Plank"])
problem.addConstraint(NotInSetConstraint([2]), ["Thor"])


# Cheetah either loves the tunnel or she came 4th
problem.addConstraint(lambda c3,t : c3== t, ["Cheetah","Tunnel"])
# Since Cheetah came 1st, she must love the tunnel


# The dog who loves the plank came 1 position after the dog who loves the poles
problem.addConstraint(NotInSetConstraint([1]), ["Plank"])
problem.addConstraint(NotInSetConstraint([4]), ["Poles"])


# Suzie is not a Shepherd and Beany doesn’t like the tunnel 
problem.addConstraint(lambda z13,z14 : z13!= z14, ["Suzie","Shepherd"])
# Tunnel is already allocated to Cheetah so no more constraints required

solution = problem.getSolutions()[0]

# in sequence of Ranking, Dog, Breed ,Best
ans = [[None for _ in range(4)] for _ in range(4)]

#print(solution)

for i in range(1,5):
    #print("i",i)
    ans[i-1][0]=i
    for x in solution:
        if solution[x] == i:
            if x in dog:
                ans[i-1][1]=x
            elif x in breed:
                ans[i-1][2]=x
            elif x in bestAt:
                ans[i-1][3]=x
            
            #print(i, x)
              
print("Raking  Dog        Breed       BestAt")
#print("Raking  Dog    Breed   BestAt")
for i in range (4):
    print(ans[i][0],"     ",ans[i][1], "   ",ans[i][2],"     ",ans[i][3])
#print(ans)


# In[ ]:




