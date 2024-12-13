# 10. Assume that obj already has a value of 42 when the code below starts 
# running. Which of the subsequent statements reassign the variable? 
# Which statements mutate the value of the object that obj references?
# Which statements do neither? If necessary, you can read the documentation.

obj = 42           # initialization

obj = 'ABcd'       # reassignment
obj.upper()        # neither
obj = obj.lower()  # reassignment
print(len(obj))    # neither
obj = list(obj)    # reassignment
obj.pop()          # mutation of list object
obj[2] = 'X'       # reassignment of element, mutation of list object
obj.sort()         # mutation
set(obj)           # neither
obj = tuple(obj)   # reassignment