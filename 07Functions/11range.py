import os
os.system("cls")
# range()
print("range()")
# returns an object, can't be iterate over, works like list, but is immutable
# range(start,stop,step)
var=range(1,31,2)
print(f"range(1,31,2)= {range(1,31,2)}")
print(f"var={var}")
print(f"type(var)={type(var)}")
print(f"var.start={var.start}")
print(f"var.stop={var.stop}")
print(f"var.step={var.step}")

print(f"var.index(23)={var.index(23)}")

demo=range(6)
print(demo)
# print(next(demo))  # will show error
# print(f"var.index(30)={var.index(30)}")  # wwill give error sincee it doesnt have 30