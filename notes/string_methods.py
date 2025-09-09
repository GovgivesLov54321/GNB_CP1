# GNB - 1st - ☑️ String Methods Notes

subject = "Computer Programming 1"

print(subject.upper())

print(subject.center(200))

# Stupid proofing
color = input("What's your favorite color?: ").strip().lower()
#lower() == all lower case
#upper() == all upper case
#capitalize() == captalizes first letter of first word
#title() == capitalizes first letter of every word
full_name = input("What's your first and last name?: ").strip().title()
#print("That's an... interesting name there; "+ full_name +".")
#print("That's cool. I also like the color " + color +".")
print("That's fire {full_name}! I also like the color {color}.".format(full_name = full_name, color = color))

#f-strings

#print(f"That's fire {full_name}! I also like the color {color}.")

pi = "3.14159"
#print(f"We all know pi is equal to {pi:.3f}.")
#print(pi.isdecimal())

sentence = "The quick brown fox jumps over the lazy dog!"
word = "sigma"
print(sentence.find(word))
start = (sentence.index(word)) #Where it begins
length = len(word)
print(sentence[start:start+length])
print(sentence.replace(word, "swims"))
print(sentence)