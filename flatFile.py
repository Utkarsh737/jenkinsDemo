 
inp = [1,2,[3,4,[5,6,[7,8,9,[10]]]]]
def convert(l,data):
    for i in l:
        if type(i)==list:
            convert(i,data)
        else:
            data.append(i)
    return data

data=[]
data=convert(inp,data)
print(data)
