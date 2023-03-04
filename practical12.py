file = r"res\file.txt"

with open(file, 'w') as f:
    data = input("Write Data: ")
    f.write(data)

with open(file, 'r') as f:
    data = f.read()
    print(data)