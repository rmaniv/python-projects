
print("")

validlist = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def encode(word):
    result = ""
    for char in range(len(word)):
        i = validlist.index(word[char]) + 2
        result += validlist[i]
    print(result)

def decode(code):
    result = ""
    for char in range(len(code)):
        i = validlist.index(code[char]) - 2
        result += validlist[i]
    print(result)

function = input("Select (Encode/Decode): ")

print("")

print("Only lower case alphabets and spaces are allowed.")

while True:
  if function.lower() == "encode":
    word = input("Enter text to be encoded: ")
    break
  elif function.lower() == "decode":
    code = input("Enter text to be decoded: ")
    break
  else:
    print("Invalid")
    quit()

print("")

if function.lower() == "encode":
    encode(word)
elif function.lower() == "decode":
    decode(code)
else:
    print("Invalid input")

print("")

x = input("Press any key to exit...")