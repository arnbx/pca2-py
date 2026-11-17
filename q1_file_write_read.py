f = open("notes.txt", "w")
f.write("Line one\nLine two\nLine three\n")
f.close()

f = open("notes.txt", "r")
print(f.read())
f.close()
