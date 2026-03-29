name = 'Zophie a cat'
#print(name)
newName = name[0:7] + 'the' + name[8:12]
#print(name[0:7])

turpleArray = ['Aaron', 18, 5.3]
#print(turpleArray[1:3])

turple = ('Aaron', 18, 19)
#turple[0] = "Sharon"

def eggs(parameter):
    parameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)