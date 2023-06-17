prompt = "Tell me something, and I'll repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    
    if message.lower() == 'quit':   
        active = False              # If the user quits, stop running the loop
    else:
        print(message)