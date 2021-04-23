age = False # can be assigned only True/False
chronic = False # can be assigned only True/False
immune = False # can be assigned only True/False
risk = age or chronic or immune
if risk==True:
     print ("You are in risky group")
else:
     print ("You are not in risky group")
