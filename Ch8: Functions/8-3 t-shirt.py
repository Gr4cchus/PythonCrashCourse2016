def make_shirt(size, message):
    """Display information about a pet."""
    print("\n The size of the shirt is", size, "and the message reads:", message)

make_shirt('Large', 'I <3 python')  # positional arguments
make_shirt(message="<3 python", size="Med")  # keyword arguments
