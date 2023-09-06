# parrot

# message = input("Tell me something and I'll read it back to you.:")
# print(message)

prompt = "Tell me something and I'll read it back to you: "
prompt += "\nEnter 'quit' to end program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
        


    
    