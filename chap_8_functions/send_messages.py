def send_messages(to_be_sent, sent):
    """
    Simulate sending each message, until none are left.
    Move each message to "sent" after sending.
    """
    while to_be_sent:
        current_message = to_be_sent.pop()
        print(f"Sending message: {current_message}")
        sent.append(current_message)

def show_messages(messages):
    """Display each message in a list of messages."""
    for message in messages:
        print(message)


pending_messages = [
    "All's fair in love and war.",
    "A horse! A horse! My kingdom for a horse!",
    "If music be the food of love, play on."
]

sent_messages = []

send_messages(pending_messages, sent_messages)

print("\nThe following messages have been sent:")
show_messages(sent_messages)

print("\nMessages remaining:")
show_messages(pending_messages)
