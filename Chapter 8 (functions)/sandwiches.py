def fill_sandwich(*ingredients):
    """Simulate filling a sandwich with a variable number of ingredients."""
    print("\nAdding these fillings to your sandwich:")
    for ingredient in ingredients:
        print(f" - {ingredient}")

fill_sandwich('ham')
fill_sandwich('pastrami', 'horseradish', 'mayonnaise')
fill_sandwich('tomato', 'red onion', 'pepperjack cheese', 'grillen chicken')