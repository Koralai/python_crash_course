# Create a list and modify it with the methods described in Chapter 3.
 
# Techniques to use:
    # Reassign the value of an item in the list
    # append(), insert()
    # del, pop(), remove()
    # sort(), sorted(), reverse()
    # len

# Set up the list and populate it.

print('What rhymes with the word "tool"?')

rhymes_with_tool = []

rhymes_with_tool.append('fool')
rhymes_with_tool.append('wool') 
rhymes_with_tool.append('cruel') 
rhymes_with_tool.append('dull') 
rhymes_with_tool.append('jewel')
rhymes_with_tool.append('school')
rhymes_with_tool.append('accrual') 

print(rhymes_with_tool)

# Revise the list.

print("\nI'll take out the last one. It's not very poetic.")
del rhymes_with_tool[-1]
print(rhymes_with_tool)

print("\nBrainstorming a few more...")
rhymes_with_tool.insert(0, 'duel')
rhymes_with_tool.insert(1, 'yule')
rhymes_with_tool.insert(5, 'gruel')
print(rhymes_with_tool)

print("\nChecking the quality of my rhymes...")
eye_rhyme = rhymes_with_tool.pop(3)
print(f'"{eye_rhyme.title()}" is an eye rhyme, not a true rhyme. Cut!')

half_rhyme = 'dull'
rhymes_with_tool.remove(half_rhyme)
print(f'"{half_rhyme.title()}" is not a full rhyme. Maybe leave it out.')

print(f'"{rhymes_with_tool[4].title()}" gives me an idea. I think I can come up with something better...')
rhymes_with_tool[4] = 'ghoul'

print(f"\nNow I have: {rhymes_with_tool}. Not bad.")

# Sort the finished list.

print(f"\nHere's how the list would look in alphabetical order: {sorted(rhymes_with_tool)}")

print(f"\nOr I could reverse the original order...")
rhymes_with_tool.reverse()
print(rhymes_with_tool)

print(f"\n...or use reverse alphabetical order, just for fun.")
rhymes_with_tool.sort(reverse=True)
print(rhymes_with_tool)

# Note the length of the finished list.

print(f'\nOkay, I have {len(rhymes_with_tool)} rhymes for the word "tool." Now, if only I knew what to write about...')