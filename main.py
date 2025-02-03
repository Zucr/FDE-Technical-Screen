

def sort(width, height, length, mass):    
    bulky = int((width * height * length) >= 1000000)
    heavy = int(mass >= 20)
    # no teranary? No problem I don't even need conditionals. Love me some branchless programs for faster code.
    return ["STANDARD", "SPECIAL", "REJECTED"][(bulky ^ heavy) + (bulky and heavy) * 2]
    
    


#testing stuff
print(sort(100, 10, 100, 19))
print(sort(100, 100, 100, 19))
print(sort(100, 100, 99, 20))
print(sort(100, 100, 100, 20))