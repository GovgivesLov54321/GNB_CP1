# GNB - 1st - ☑️*args and **kwargs Notes

#def hello(name, age):
  #  return f"hello {name}!"

#hello("Jeffery", 67)

#def hello(name, age):
   # return f"hello {name}!"

#hello(age = 67, name = "Sir")

#def hello(name = "Gov", age = 15):
    #return f"hello {name}! You are {age}."

#hello(())
#print(hello("Taiye", 13))
#print(hello("Sophie"))
#print(hello(age = 15))

def hello(*names, **kwargs): #turned parameter into list -- Normal positional arguments 1st, then, multiple positional arguments, then normal keyword arguments, then multiple keyword arguments -- * means all, takes all the items in list and puts them in "names"
    print(type(names))
    print(kwargs)
    for n in names:
        print(f"Hello {n} {kwargs['last_name']} ;O")

hello("Abby", "Darren", "Alondra", "Carter", "Cooper", last_name = "Bilbao", unc = "Bright", num_houses = 2)

def full_name(age, **names):
    if 'middle' in names.keys():
        return f"{names['first']} {names['middle']} {names['last']}"
    else: 
        return f"{names['first']} {names['last']}"
    
print(full_name(age = "16", first = "Ryker", last = "Garr"))
print(full_name(age = "16", first = "Maddox", middle = "Jake", last = "Collins"))

def summary(**story): #another example for kwargs
    sum = ""
    if "name" in story.keys():
        sum += f"{story['name']} is the main character of this story..."
    if "place" in story.keys():
        sum += f"The story takes place in {story['place']}..."
    if "conflict" in story.keys():
        sum += f"The problem is {story['conflict']}..."

    return(sum)

print(summary(name = "Mr. LeBron", place = "Mars", conflict = "The Huzz is home alone"))