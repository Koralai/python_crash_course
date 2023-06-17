# Create a list of places I'd like to visit.

destinations = ['paris', 'montreal', 'seoul', 'sydney', 'rome']
print(f"Original list order: {destinations}")

# Use the sorted() method. It doesn't permanently change the list.

print(sorted(destinations))
print(f"After sorted() method: {destinations}")

# Use the reverse() method. The list has been permanently changed.

destinations.reverse()
print(f"Reverse of the original order: {destinations}")

# Use the sort() method. Also a permanent change.

destinations.sort()
print(f"Alphabetical order: {destinations}")

destinations.sort(reverse=True)
print(f"Reverse alphabetical order: {destinations}")