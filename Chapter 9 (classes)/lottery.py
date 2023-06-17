"""A simple model of a lottery system"""

# Future enhancements:
# - Make sure each item in the ticket is unique
# - Match the winning ticket only for items contained, not for their order

from random import choice
    
def generate_ticket(options) -> str:
    """Returns a ticket with 4 items from the list of available options."""
    ticket_number = ''
    for _ in range(4):
        ticket_number += str((choice(options)))        
    return ticket_number.upper()

def main():
    my_options = (
        84, 82, 45, 7, 61, 33, 87, 36, 88, 94,
        'a', 'f', 'w', 'k'
    )
    
    # Create the winning ticket
    
    winning_ticket = generate_ticket(my_options)    
    print(f"If your ticket matches these numbers or letters, you win a prize: {winning_ticket}")
    
    # Keep buying tickets until you get a match with the winning ticket
        
    playing_lottery = True
    times_played = 0
    ticket_price = 1
    
    while playing_lottery is True:
        new_ticket = generate_ticket(my_options)
        times_played += 1
        
        if new_ticket == winning_ticket:
            
            money_spent = times_played*ticket_price
            
            print(f"I found the winning ticket: {new_ticket}."
                  f"\nIt only took me {times_played:,} tries at "
                  f"${ticket_price} per ticket, or "
                  f"${money_spent:,}.")    # Commas for thousands place 
            
            playing_lottery = False
            
if __name__ == '__main__':
    main()
