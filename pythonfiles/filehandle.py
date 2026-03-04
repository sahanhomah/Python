decision=input("enter r to read, a to add texts , w to write from beginning and exit to quit: ")
while decision!="exit":
    if decision=="r":
     file = open("sahan.txt", "r")
     content=file.read()
     print("the story you have written is: ", content)
     file.close()
     decision=input("enter r to read, a to add texts , w to write from beginning and exit to quit: ")
    elif decision=="a":
     file = open("sahan.txt", "a")
     story=input("Enter your story: ")
     file.write("\n"+story)
     print("file append successfully")
     file.close()
     decision=input("enter r to read, a to add texts , w to write from beginning and exit to quit: ")
    elif decision=="w":
     file = open("sahan.txt", "w")
     story=input("Enter your story: ")
     file.write(story)
     print("file write successfully")
     file.close()
     decision=input("enter r to read, a to add texts , w to write from beginning and exit to quit: ")











