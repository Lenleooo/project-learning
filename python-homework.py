
def norm_name(name):
    return name[0].upper() + name[1:].lower()
inputs = ['adam','LISA','barT']
output = list(map(norm_name,inputs))
print(output)