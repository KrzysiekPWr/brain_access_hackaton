import oct2py
oc = oct2py.Oct2Py()

script = "function y = myScript(x)\n" \
         "    y = x-5" \
         "end"

with open("openibis.m","r+") as f:
    print(f.read())
    

# oc.myScript(7)

# x = oc.zeros(1,3)

# print(x)