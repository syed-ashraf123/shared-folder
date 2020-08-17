warlus=4
print(warlus)

print(walrus := True)

inputs = list()
while True:
    current = input("Write something: ")
    if current == "quit":
        break
    inputs.append(current)
    
inputs = list()
while (current := input("Write something: ")) != "quit":
    inputs.append(current)
