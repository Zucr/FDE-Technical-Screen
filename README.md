# RUN THE `main.py` PYTHON SCRIPT

## Instructions
```python
def sort(width, height, length, mass):    
  bulky = int((width * height * length) >= 1000000)
  heavy = int(mass >= 20)
  # no teranary? No problem I don't even need conditionals. Love me some branchless programs for faster code.
  return ["STANDARD", "SPECIAL", "REJECTED"][(bulky ^ heavy) + (bulky and heavy) * 2]

if __name__ == "__main__":
   # some examples insert whatever you want here for test points. incert your own data here or import into your own code base and use how you see fit.
  print(sort(100, 10, 100, 19))  # STANDARD
  print(sort(100, 100, 100, 19))  # SPECIAL
  print(sort(100, 100, 99, 20))   # SPECIAL
  print(sort(100, 100, 100, 20))  # REJECTED
 ```
In bash run this
```bash
python3 main.py
```
